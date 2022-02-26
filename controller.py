import ui
import converter as con
import calc
import logger as l

def get_number():
    num = con.conversion(ui.get_value())
    if num == 'nan':
        get_number()
    else: return num

def get_operation():
    op = ui.get_value()
    if op in ['+', '-', '*', '/']:
        return op
    else: get_operation()

def button_click():
    number1 = get_number()
    operate = get_operation()
    number2 = get_number()
    result = calc.calculate(number1, operate, number2)
    l.log_it(ui.show_result(number1, operate, number2, result))