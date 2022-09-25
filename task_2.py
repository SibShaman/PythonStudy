""" Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

my_list = [2, 3, 4, 5, 6]

res_list = []

for i in range(len(my_list)):
    if len(my_list) == 0:
        break
    elif len(my_list) == 1:
        temp = pow(my_list[0], 2)
        my_list.pop(0)
    else:
        temp = my_list[0]*my_list[-1]
        my_list.pop(0)
        my_list.pop(-1)

    res_list.append(temp)

print(res_list)
