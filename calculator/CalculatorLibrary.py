class CalculatorLibrary:

    def __init__(self):
        self._data = ''

    def push_button(self, input):
        if input == '=':
            self._data += ''
        elif input == 'C':
            self._data = ''
        else:
            self._data += input

    def result_should_be(self, expected):
        if self._data == '':
            return

        result = str(eval(self._data))
        if result != expected:
           raise AssertionError('%s != %s' % (result, expected))

    def push_buttons(self, inputs):
        for input in inputs:
            self.push_button(input)

if __name__ == '__main__':
    c = CalculatorLibrary()
    c.push_button('1')
    c.push_button('+')
    c.push_button('2')
    c.result_should_be('3')