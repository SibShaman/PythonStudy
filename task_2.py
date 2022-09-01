"""Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. """

# 12. Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

N = int(input('Введите количество чисел в последовательности: '))

my_list_one = list(range(1, N+1))
my_list_two = list(map(lambda x: 3*x+1, my_list_one))

my_dict = dict(zip(my_list_one, my_list_two))
print(my_dict)
