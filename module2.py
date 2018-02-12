
import logging


class Class3(object):
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.logger.info('This is the class 3 constructor')

    def do_something(self):
        self.logger.info('doing something')


