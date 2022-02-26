def get_value():
    return input()

def show_result(x, op, y, res):
    record = f'{x} {op} {y} = {res}'
    print(record)
    return record