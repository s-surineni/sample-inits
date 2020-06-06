import os

from confluent_kafka import avro


def get_absolute_file_path(props_file_path):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    props_file_path = os.path.join(dir_path, props_file_path)
    return props_file_path


def load_schema_from_file(file_path):
    key_schema_string = """
    {"type": "string"}
    """
    key_schema = avro.loads(key_schema_string)
    value_schema = avro.load(file_path)
    return key_schema, value_schema
