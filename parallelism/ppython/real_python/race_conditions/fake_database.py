import concurrent.futures
import logging
import time


class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self):
        logging.info("starting update")
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info('id(self) %s', id(self))
        logging.info("finishing update")



if __name__ == "__main__":
    format = "%(thread)d %(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update)
    logging.info("Testing update. Ending value is %d.", database.value)
