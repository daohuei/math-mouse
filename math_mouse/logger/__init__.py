import traceback
import logging
import sys


class Logger:
    def __init__(self, name):
        logging.basicConfig(
            format='[%(asctime)s][%(levelname)s] %(message)s',
            level=logging.INFO,
            datefmt='%m/%d/%Y %I:%M:%S %p'
        )
        self.logger = logging.getLogger(name)
        self.error = self.logger.error
        self.info = self.logger.info

    def __str__(self):
        return "Logger({})".format(self.name)
