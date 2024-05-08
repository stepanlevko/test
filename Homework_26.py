while True:
    class Calc:

        def __init__(self, summ, sub, prod, div, sq, sqr):
            self.summ = summ # +
            self.sub = sub # -
            self.prod = prod # *
            self.div = div # /
            self.sq = sq # **2
            self.sqr = sqr # **0.5

        try:
            def summ(self, other):
                res = self + other
                return res
        except NameError:
            pass

        try:
            def sub(self, other):
                res = self - other
                return res
        except NameError:
            pass

        try:
            def prod(self, other):
                res = self * other
                return res
        except NameError:
            pass

        try:
            def div(self, other):
                res = self / other
                return res
        except ZeroDivisionError:
            res = 0

        try:
            def sq(self):
                res = self ** 2
                return res
        except ValueError:
            other = 1
        try:
            def sqr(self):
                res = self ** 0.5
                return res
            raise IndexError
        except IndexError:
            pass
        else:
            print('Відємне число під коренем')

    value_1 = self = float(input('Введіть перше число: '))
    operation = input('Введіть операцію: ')
    try:
        value_2 = other = float(input('Введіть друге число: '))
    except ValueError:
        pass

    if operation == '+':
        print('Результат: ', Calc.summ(self, other))
    elif operation == '-':
        print('Результат: ', Calc.sub(self, other))
    elif operation == '*':
        print('Результат: ', Calc.prod(self, other))
    elif operation == '/':
        print('Результат: ', Calc.div(self, other))
    elif operation == '**2':
        print('Результат: ', Calc.sq(self))
    elif operation == '**0.5':
        print('Результат: ', Calc.sqr(self))
    else:
        print('Некоректне введення')

    continue



