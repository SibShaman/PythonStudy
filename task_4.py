"""Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. """

# 15. Написать программу, получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [1, 2, 6, 24]


num = int(input('Введите количество чисел в последовательности: '))

my_list = []
my_list = [my_list[-1]
           for x in range(1, num+1) if not my_list.append(x*my_list[-1] if my_list else 1)]
print(my_list)
