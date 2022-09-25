"""Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. """

# 14. Подсчитать сумму цифр в вещественном числе.

num = input('Введите число которое вы хотите разложить и посчитать сумму: ')
temp_list = [int(i) for x, i in enumerate(num) if i != '.']
print(f'сумма цифр в вашем числе = {sum(temp_list)}')
