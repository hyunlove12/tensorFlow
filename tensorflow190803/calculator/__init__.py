from calculator.controller import CalculatorController
#패키지  + 클래스
'''
if __name__ == '__main__':
    num1 = int(input('첫번째 수 \n'))
    calc = CalculatorModel(2,3)
    result = calc.add(int(num1),6)
    print('계산결과 %d' % result)
'''
if __name__ == '__main__':
    calc = CalculatorController()
    calc.execute()

