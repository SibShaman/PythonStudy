"""Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. """

# 16. Задать список из n чисел последовательности и вывести на экран их сумму.

from functools import reduce


num = int(input('Введите количество чисел в последовательности: '))
sum_num = reduce(lambda x, y: x+y, range(1, num+1))
print(f'Сумма чисел в последовательности = {sum_num}')
