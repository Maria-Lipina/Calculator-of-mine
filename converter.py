import string
from fractions import Fraction

import ui

xin = ui.get_value()
# opin = ui.get_value()
# yin = ui.get_value()

def convert(arg:str): #У этого метода есть серьезный недостаток, который угробил мне весь вечер: он работает только с правильно переданными аргументами и не обрабатывает ошибки, которые могут возникнуть при вводе. Но я сломала всю маковку на вопросе "Как прогнать по всем проверкам?"
    if arg.isdigit(): return int(arg)
    if ('+' in arg) and (arg[-1].isalpha):
        arg = arg.replace(arg[-1], '')
        check = arg.replace('+', '')
        numparts = arg.split('+')
        return complex(numparts[0])

# А ещё стало понятно, что в зависимости от типа числа - разные стратегии конвертации НЕЛЬЗЯ смешивать в один метод. Дробям не нужно все то, что нужно проверять для комплексных (а они главная боль, да)

# if xin.isdigit(): 
# cond1 = xin.isdigit() #Для целых
# cond2 = ('+' in xin) and (xin[-1].isalpha) #Для комплексных
# cond3 = ',' in xin #заменить на .
# cond4 = '/' in xin #сделать дробь (убрать то, что до и после)

# print(cond1)
# print(bool(xin[-1].isalpha))

# test = complex(5.1, 8)
# print(test)
