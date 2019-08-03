class CalculatorModel:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self, num1, num2):
        result = num1 + num2
        return result

    def sub(self, num1, num2):
        result = num1 - num2
        return result

    def mul(self, num1, num2):
        result = num1 * num2
        return result

    def div(self, num1, num2):
        result = num1 / num2
        return result



