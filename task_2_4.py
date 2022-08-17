# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint


num = int(input('Введите число: '))

_list = []
for i in range(1, num+1):
    _list.append(randint(-num, num))

print(_list)