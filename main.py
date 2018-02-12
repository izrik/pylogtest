#!/usr/bin/env python3

import logging

import module1
import module2
import package1.module3
import package1.package2.module4

logging.basicConfig(level=logging.INFO)

logging.info('root logger in main.py')

logger = logging.getLogger(__name__)
logger.info('module level in main.py')

if __name__ == '__main__':
    logger.info('"if __name__ == \'__main__\':" in main.py')
    c1 = module1.Class1()
    c1.do_something()
    c2 = module1.Class2()
    c2.do_something()
    c3 = module2.Class3()
    c3.do_something()
    c4 = package1.module3.Class4()
    c4.do_something()
    c5 = package1.package2.module4.Class5()
    c5.do_something()
