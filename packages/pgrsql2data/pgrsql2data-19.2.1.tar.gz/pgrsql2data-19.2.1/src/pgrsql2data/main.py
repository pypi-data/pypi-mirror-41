import csv
import json
import re
from collections import OrderedDict

import fastavro
from geomet import wkb, wkt


def convert_wkb_to_wkt(strip_srid=True):
    def func(wkb_hex_value):
        geom = wkb.loads(bytes.fromhex(wkb_hex_value))
        if strip_srid:
            geom.pop("meta")
            geom.pop("crs")
        return wkt.dumps(geom)

    return func


class FieldType:
    def __init__(self, type_converter, avro_data_type, null_value="null"):
        self._type_converter = type_converter
        self._avro_data_type = avro_data_type
        self._null_value = null_value

    def __call__(self, value):
        if value == self._null_value:
            return None
        return self._type_converter(value)

    def __repr__(self):
        return self._avro_data_type

    @property
    def avro_type(self):
        return ["null", self._avro_data_type]


class TableSchema:
    def __init__(self, name=None, fields=None):
        self.name = None
        if fields:
            self._fields = OrderedDict(fields)
        else:
            self._fields = OrderedDict()

    def keys(self):
        return self._fields.keys()

    def get_converter(self, field):
        return self._fields.get(field, str)

    def get_avro_schema(self):
        fields = [{"name": k, "type": v.avro_type} for k, v in self._fields.items()]
        schema = {
            "doc": "PgRouting compatible OpenStreetMap data",
            "name": "PgRouting Data",
            "namespace": "osm2po",
            "type": "record",
            "fields": fields,
        }
        return fastavro.parse_schema(schema)

    def add_fields(self, fields):
        self._fields.update(fields)


class DDLConverter:
    _SQL_TABLE_TYPE_MAPPING = {
        "integer": FieldType(int, "int"),
        "bigint": FieldType(int, "long"),
        "character varying": FieldType(str, "string"),
        "double precision": FieldType(float, "double"),
    }

    def __init__(self, input_file, output_file, output_format):
        self.input_file = input_file
        self.output_file = output_file
        self.output_format = output_format

    def parse_insert_values(self, values, table_schema):
        csv_data = csv.DictReader(
            [values], fieldnames=table_schema.keys(), dialect="sql"
        )
        data = next(csv_data)
        data = {k: table_schema.get_converter(field=k)(v) for k, v in data.items()}
        return data

    def convert(self):
        records = []
        table_schema = TableSchema()
        csv.register_dialect("sql", skipinitialspace=True, quotechar="'")
        with open(self.input_file, "r") as in_fp:
            for line in in_fp:
                if line.lower().startswith("create table"):
                    fields = self._get_fields_from_create_table_ddl(line)
                    table_schema.add_fields(fields)
                if line.lower().startswith("select addgeometrycolumn"):
                    field = self._get_geometry_field_from_ddl(line)
                    table_schema.add_fields(field)
                insert_line = re.search(r"^\((?P<values>.+?)\)[;,]?$", line)
                if insert_line:
                    values = insert_line.group("values")
                    records.append(self.parse_insert_values(values, table_schema))
        if self.output_format == "csv":
            self.write_to_csv(self.output_file, records, table_schema)
        if self.output_format == "json":
            self.write_to_json(self.output_file, records, table_schema)
        if self.output_format == "avro":
            self.write_to_avro(self.output_file, records, table_schema)

    def write_to_csv(self, output_file, records, table_schema):
        with open(output_file, "w") as out_fp:
            csv_writer = csv.DictWriter(
                out_fp,
                fieldnames=table_schema.keys(),
                quotechar='"',
                quoting=csv.QUOTE_NONNUMERIC,
            )
            csv_writer.writeheader()
            csv_writer.writerows(records)

    def write_to_json(self, output_file, records, table_schema):
        with open(output_file, "w") as out_fp:
            for record in records:
                out_fp.write(json.dumps(record) + "\n")

    def write_to_avro(self, output_file, records, table_schema):
        with open(output_file, "wb") as out_fp:
            schema = table_schema.get_avro_schema()
            fastavro.writer(out_fp, schema, records)

    def _get_geometry_field_from_ddl(self, ddl):
        ddl_match = re.search(
            (
                r"^SELECT AddGeometryColumn\("
                r"'(?P<table_name>.+?)'"
                r", '(?P<column_name>.+?)'"
                r", (?P<srid>\d+?)"
                r", '(?P<type>.+?)'"
                r", (?P<dimension>\d+?)"
                r"\);$"
            ),
            ddl,
            re.IGNORECASE,
        )
        if ddl_match:
            field_name = ddl_match.group("column_name")
            return {
                field_name: FieldType(convert_wkb_to_wkt(strip_srid=True), "string")
            }

    def _get_fields_from_create_table_ddl(self, ddl):
        ddl_match = re.search(
            r"^CREATE TABLE (?P<table_name>.+?)\((?P<fields>.+?)\)[;,]?$", ddl
        )
        if ddl_match:
            text_fields = ddl_match.group("fields")
            fields = OrderedDict(
                map(self._parse_create_table_field, text_fields.split(","))
            )
            return fields

    def _parse_create_table_field(self, field):
        field_name, _, sql_type = field.strip().partition(" ")
        return (
            field_name,
            self._SQL_TABLE_TYPE_MAPPING.get(sql_type, FieldType(str, "string")),
        )
