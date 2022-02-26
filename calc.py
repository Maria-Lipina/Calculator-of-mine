operation = {
    '+': lambda x,y: x+y,
    '-': lambda x,y: x-y,
    '/': lambda x,y: x/y,
    '*': lambda x,y: x*y
    }

def calculate(x, op, y):
    return operation[op](x,y)