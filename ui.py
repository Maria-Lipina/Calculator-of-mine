import calc
import logger as log

def get_value():
    return input()

print("Добро пожаловать!\nВыражение задается следующим образом: 1. Первое число, 2. Операция над этим числом, 3. аргумент для операции:")
x_in = get_value()

print("Операция (для извлечения корня - sqrt, для возведения в степень - pow): ")
op_in = get_value()

print("Второе число (аргумент для операции над первым): ")
y_in = get_value()

# result = get.value
print(f"Результат:{x_in}{op_in}{y_in} = result")
