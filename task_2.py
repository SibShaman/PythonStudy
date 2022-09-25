# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

from math import fabs


nature_num = int(input('Введите число которое необходимо разложить на множители: '))

res_list = []

def simple(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
    return flag


for i in range(2, nature_num+1):
    if nature_num%i == 0 and simple(i):
        res_list.append(i)

print(res_list)
