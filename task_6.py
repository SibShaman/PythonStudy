"""Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. """

# 17. Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


from random import randint

num = randint(10, 21)
list_one = [i for i in range(-num, num+1)]

print(list_one)
with open('file.txt', 'w+', encoding='utf8') as data:
    for i in range(1, (num//2)):
        data.write(f'{randint(0, num*2)}\n')


with open('file.txt', 'r', encoding='utf8') as final_data:
    list_two = [int(i[:-1]) for i in final_data]

print(list_two)

res = 1
for i in list_two:
    res *= list_one[i]
print(res)
