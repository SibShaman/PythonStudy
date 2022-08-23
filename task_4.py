""" Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""

your_num = int(input('Введите число которое необходимо перевести в двоичную систему'))

res_list = []
while your_num > 0:
    a = your_num%2
    b = your_num//2
    your_num = b
    res_list.append(a)

print(*reversed(res_list))
