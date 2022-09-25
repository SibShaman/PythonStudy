# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint


num = int(input('Введите количество элементов списка: '))

with open('file.txt', 'w+') as data: 
    for i in range(1, num+1):
        a = randint(-num, num)
        data.write(str(a) + '\n')

pos = 1
temp_list = []
while pos != 0:
    pos = int(input('Введите позиции которые вы хотите перемножить или 0 для выхода: '))
    temp_list.append(pos) 
    if pos>num:
        print('Вы вышли за пределы диапазона, попробуйте еще или 0 для выхода ')
        temp_list.remove(pos)
    elif pos == 0:
        temp_list.remove(pos)
        break

res = 1
with open ('file.txt', 'r') as final_data:
    for i, line in enumerate(final_data):    
        if (i+1) in temp_list:
            res *= int(line)

print(res)
    