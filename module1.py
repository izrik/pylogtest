
import logging


class Class1(object):
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.logger.info('This is the class 1 constructor')

    def do_something(self):
        self.logger.info('doing something')



class Class2(object):
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.logger.info('This is the class 2 constructor')

    def do_something(self):
        self.logger.info('doing something')

