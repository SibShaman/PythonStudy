"""Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. """

# 16. Задать список из n чисел последовательности и вывести на экран их сумму.


num = int(input('Введите количество чисел в последовательности: '))
sum_one = [round((1+(1/x))**x, 2) for x in range(1, num+1)]
# sum_num = reduce(lambda x, y: x+y, range(1, num+1))
print(sum_one)
print(f'Сумма чисел в последовательности = {sum(sum_one)}')
