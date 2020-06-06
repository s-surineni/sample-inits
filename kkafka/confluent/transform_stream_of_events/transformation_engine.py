import logging

from .utils import get_absolute_file_path

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TransformationEngine:
    def __init__(self, input_topic, output_topic, raw_consumer, producer):
        self.input_topic = input_topic
        self.output_topic = output_topic
        self.raw_consumer = raw_consumer
        self.producer = producer

    def convert_raw_movie(self, raw_movie):
        print('raw_movie', raw_movie)
        title_parts = raw_movie['title'].split('::')
        title = title_parts[0]
        release_year = int(title_parts[1])
        movie = {'id': raw_movie['id'],
                 'title': title,
                 'release_year': release_year,
                 'genre': raw_movie['genre']}
        return movie

    def start(self):
        self.raw_consumer.subscribe([self.input_topic])
        print('input topic', self.input_topic)
        try:
            while True:
                record = self.raw_consumer.poll(5)
                # for a_rec in records:
                movie = self.convert_raw_movie(record.value())
                self.producer.produce(topic=self.output_topic,
                                      key=record.key(),
                                      value=movie)
        except Exception:
            logger.exception('Error while transforming events')
