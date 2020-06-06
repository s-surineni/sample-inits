import logging

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TransformationEngine:
    def __init__(self, input_topic, output_topic, raw_consumer, producer):
        self.input_topic = input_topic
        self.output_topic = output_topic
        self.raw_consumer = raw_consumer
        self.producer = producer

    def convert_raw_movie(raw_movie):
        title_parts = raw_movie.getTitile().split('::')
        title = title_parts[0]
        release_year = int(title_parts[1])

        return Movie(raw_movie.getId, title, release_year,
                     raw_movie.getGenre())

    def start(self):
        self.raw_consumer.subscribe([self.input_topic])

        try:
            while True:
                records = self.raw_consumer.poll(0.1)
                for a_rec in records:
                    movie = self.convert_raw_movie(a_rec.value())
                    transformed_record = ProducerRecord(self.output_topic,
                                                        movie)
                    self.producer.send(transformed_record)
        except Exception:
            logger.exception('Error while transforming events')
