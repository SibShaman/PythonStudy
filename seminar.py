# 27. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# my_string = '1 23 45 67 8 9'
# temp = list(map(int, my_string.split(' ')))

# max_num = temp[0]
# min_num = temp[0]

# for i in range(1, len(temp)):
#     if temp[i]>max_num:
#         max_num = temp[i]

#     if temp[i]<min_num:
#        min_num = temp[i]


# print(max_num)
# print(min_num)


# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#     1. с помощью математических формул нахождения корней квадратного уравнения
#     2. с помощью дополнительных библиотек Python

"""
import math

A = 3.2
B = -7.8
C = 1

res = B**2 - 4*A*C
print(res) 

res = math.pow(B, 2) - 4*A*C
print(res)

if res>0:
    X = round((-B+math.sqrt(res))/(2*A),2)
    Y = round((-B-math.sqrt(res))/(2*A),2)
    print(f'{X} {Y}') 
elif res == 0:
    X = -B/(2*A)
    print(f'{X}')
else:
    print('нет решения')
"""


# A = 3.2
# B = -7.8
# C = 1

# res = B**2 - 4*A*C
# print(res) 

# if res>0:
#     X = round((-B+(res**0.5))/(2*A),2)
#     Y = round((-B-(res**0.5))/(2*A),2)
#     print(f'{X} {Y}')
# elif res == 0:
#     X = -B/(2*A)
#     print(f'{X}')
# else:
#     print('нет решения')


# 29. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

first_num = int(input('Введите 1 число: '))
second_num = int(input('Введите 2 число: '))
a = first_num
b = second_num

while first_num != second_num:
    if first_num > second_num:
        first_num = first_num - second_num
    else:
        second_num = second_num - first_num

nok = (a*b)//first_num
print(nok)