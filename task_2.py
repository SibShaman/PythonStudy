# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

nature_num = int(input('Введите число которое необходимо разложить на множители: '))

res_list = []

for i in range(2, nature_num+1):
    if nature_num%i == 0:
        res_list.append(i)

print(res_list)
