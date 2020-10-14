class CalculatorLibrary:

    def __init__(self):
        self._data = ''

    def push_button(self, input):
        if input == '=':
            self._data += ''
        else:
            self._data += input

    def push_buttons(self, inputs):
        pass

    def result_should_be(self, expected):
        result = str(eval(self._data))
        if result != expected:
           raise AssertionError('%s != %s' % (result, expected))

if __name__ == '__main__':
    c = CalculatorLibrary()
    c.push_button('1')
    c.push_button('+')
    c.push_button('2')
    c.result_should_be('3')