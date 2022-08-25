# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def rk():
    return randint(1, 100)

degree = int(input('Введите натуральную степень k: '))

temp_list = []
for i in range(0, degree+1):
    if i == 0:
        temp_list.append(f'+ {rk()}')
    elif i == 1:
        temp_list.append(f'{rk()}*x')
    else:
        temp_list.append(f'{rk()}*x**{i} +')
temp_list = (reversed(temp_list))
result_str = ' '.join(temp_list)

print(f'{result_str} = 0')
