import logging
import os
import sys

# from avro.io import
from configparser import ConfigParser
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka.avro import AvroConsumer, AvroProducer
from confluent_kafka.serialization import StringDeserializer
from confluent_kafka.serialization import StringSerializer

from .transformation_engine import TransformationEngine
from .utils import get_absolute_file_path, load_schema_from_file

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TransformEvents:
    def __init__(self, file_path):
        self.props_file_path = file_path

    def load_env_properties(self, file_path):
        config = ConfigParser()
        config.read(file_path)
        return config['DEFAULT']

    def build_consumer_properties(self, group_id, env_props):
        consumer_props = {}
        consumer_props['group.id'] = group_id
        consumer_props['enable.auto.commit'] = True
        consumer_props['auto.offset.reset'] = 'earliest' # what is this??
        consumer_props['bootstrap.servers'] = env_props['bootstrap.servers']
        consumer_props['schema.registry.url'] = env_props['schema.registry.url']
        # consumer_props['key.deserializer.class'] = StringDeserializer
        # consumer_props['key.serializer.class'] = StringSerializer
        # consumer_props[]
        print('consumer props')
        print(consumer_props)
        return consumer_props

    def build_producer_properties(self, env_props):
        producer_props = {}
        producer_props['acks'] = 'all'
        producer_props['bootstrap.servers'] = env_props['bootstrap.servers']
        # producer_props[]
        # not yet supported in python??
        producer_props['schema.registry.url'] = env_props['schema.registry.url']
        return producer_props

    def create_raw_movie_consumer(self, consumer_props):
        return AvroConsumer(consumer_props)

    def create_movie_producer(self, producer_props):
        schema_file_name = 'parsed-movies.avsc'
        schema_file_path = get_absolute_file_path(schema_file_name)
        key_schema, value_schema = load_schema_from_file(schema_file_path)
        return AvroProducer(producer_props,
                            default_key_schema=key_schema,
                            default_value_schema=value_schema)

    def create_topics(self, kafka_config):
        config = {'bootstrap.servers': kafka_config['bootstrap.servers']}
        admin_client = AdminClient(config)
        topics = []
        topics.append(
            NewTopic(kafka_config['input.topic.name'],
                     int(kafka_config['input.topic.partitions']),
                     int(kafka_config['input.topic.replication.factor'])))
        topics.append(
            NewTopic(kafka_config['output.topic.name'],
                     int(kafka_config['input.topic.partitions']),
                     int(kafka_config['input.topic.replication.factor'])))
        admin_client.create_topics(topics)
        logger.info(f'Created topics {topics}')

    def delete_topics(self, kafka_config):
        config = {'bootstrap.servers': kafka_config['bootstrap.servers']}
        admin_client = AdminClient(config)
        topics = []
        topics.append(kafka_config['input.topic.name'])
        topics.append(kafka_config['output.topic.name'])
        admin_client.delete_topics(topics)
        logger.info(f'Deleted topics {topics}')

    def start_transformation(self):
        config = ConfigParser()
        props_file_path = get_absolute_file_path(self.props_file_path)
        config.read(props_file_path)
        kafka_config = config['kafka']
        config_dict = {}

        for k, v in kafka_config.items():
            config_dict[k] = v
        self.delete_topics(config_dict)
        self.create_topics(config_dict)

        input_topic = kafka_config['input.topic.name']
        output_topic = kafka_config['output.topic.name']
        consumer_props = self.build_consumer_properties('inputGroup',
                                                        kafka_config)
        raw_consumer = self.create_raw_movie_consumer(consumer_props)
        producer_props = self.build_producer_properties(kafka_config)
        producer = self.create_movie_producer(producer_props)

        trans_engine = TransformationEngine(input_topic, output_topic,
                                            raw_consumer, producer)
        trans_engine.start()


if __name__ == '__main__':
    file_path = sys.argv[1]
    te = TransformEvents(file_path)
    te.start_transformation()
