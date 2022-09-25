""" Задайте список из вещественных чисел.
Напишите программу, которая найдёт разницу между максимальным
и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""


my_list = [1.12, 1.2, 3.1, 5, 10.01]
res_list = []

for i in range(len(my_list)):
    temp = int(my_list[i])
    res = round(abs(my_list[i] - temp), 2)*100
    if res != 0:
        res_list.append(int(res))

main_res = (max(res_list) - min(res_list))/100

print(main_res)
