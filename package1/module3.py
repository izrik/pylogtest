
import logging


class Class4(object):
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.logger.info('This is the class 4 constructor')

    def do_something(self):
        self.logger.info('doing something')


