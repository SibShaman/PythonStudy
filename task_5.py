# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


from curses.ascii import isdigit
from itertools import zip_longest


with open('file_one.txt', 'r', encoding='utf-8') as first, \
    open('file_two.txt', 'r', encoding='utf-8') as second:
    
    temp_one = first.readline()
    first_list = temp_one.split(' ')

    temp_two = second.readline()
    second_list = temp_two.split(' ')

    res_list_one = []
    for i in first_list[::2]:
        a = i.split('*x')
        for j in a:
            if j.isdigit():
                res_list_one.append(j)
    
    res_list_one = res_list_one[:-1]        

    res_list_two = []
    for i in second_list[::2]:
        a = i.split('*x')
        for j in a:
            if j.isdigit():
                res_list_two.append(j)
    
    res_list_two = res_list_two[:-1]
    res_list = zip_longest(res_list_one, res_list_two)

    res = [(int(i[0]) + int(i[1])) for i in res_list]
    res = list(reversed(res))

    res_res_list = []
    for i in range(len(res)):
        if i == 0:
            res_res_list.append(f'{res[i]} = 0')
        elif i == 1:
            res_res_list.append(f'{res[i]}*x + ')
        else:
            res_res_list.append(f'{res[i]}*x**{i} + ')

    res_res_list = reversed(res_res_list)
    res_str = ''.join(res_res_list)


    print(res_list_one)
    print(res_list_two)
    print(res)
    print(res_str)
    
with open('file_three.txt', 'w', encoding='utf8') as result:
    result.write(res_str)