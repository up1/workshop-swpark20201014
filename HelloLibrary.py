from robot.api import logger
from robot.api.deco import keyword

class HelloLibrary:
    def __init__(self):
        self._result = ''

    def say_hi_all(self, **names):
        for name, value in names.items():
            print('%s = %s' % (name, value))
            logger.console('\n%s = %s' % (name, value))

    @keyword('Try to send data with')
    def set_name(self, name='demo', age=18):
        self._result = 'Hi, %s' %(name)
    
    def result_should_be(self, expected):
        if self._result != expected:
           raise AssertionError('%s != %s' % (self._result, expected))

if __name__ == '__main__':
    h = HelloLibrary()
    h.set_name('somkiat')
    h.result_should_be('Hi, somkiat')