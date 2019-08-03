from calculator.model import CalculatorModel

class CalculatorController:
    def __init__(self):
        self.num1 = int(input('숫자를  입력하세요 \n'))
        self.num2 = int(input('숫자를  입력하세요 \n'))
        self.op = input('연산자를 입력하세요 \n')
        self.calc = CalculatorModel(self.num1, self.num2)

    def execute(self):
        if self.op == '+':
            result = self.calc.add(self.num1,self.num2)
            print(result)
        elif self.op == '-':
            result = self.calc.sub(self.num1, self.num2)
            print(result)
        elif self.op == '*':
            result = self.calc.mul(self.num1, self.num2)
            print(result)
        elif self.op == '/':
            result = self.calc.div(self.num1, self.num2)
            print(result)
