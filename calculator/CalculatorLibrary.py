class CalculatorLibrary:
    def push_button(self, input):
        pass

    def push_buttons(self, inputs):
        pass

    def result_should_be(self, expected):
        pass

if __name__ == '__main__':
    c = CalculatorLibrary()
    c.push_button('1')
    c.push_button('+')
    c.push_button('2')
    c.result_should_be('3')