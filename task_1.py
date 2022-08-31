"""Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. """

# 11. Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

N = int(input('Введите количество чисел в последовательности: '))
my_list = [pow(-3, i-1) for i in range(1, N+1)]
print(my_list)
