# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;




from enum import unique


_str = '(1+2)*4'

# print(eval(_str))

# _list = []
# for i in _str:
#     if i.isdigit():
#         _list.append(int(i))
#     else:
#         _list.append(i)
# print(_list)

# res = 0

# if _str.find('*') or _str.find('/'):
#     if _str.find('*') != -1:
#         a = _str.find('*')   
#         res = int(_str[a-1]) * int(_str[a+1])

#     else:
#         a = _str.find('/')   
#         res = int(_str[a-1]) / int(_str[a+1])


# print(res)

# if _str.find('+') or _str.find('-'):
#     if _str.find('+') != -1:
#         a = _str.find('+')
#         if a == 3:
#             res = res + int(_str[4])
#         else:
#             res = res + int(_str[a-1])
    
#     else:
#         a = _str.find('-')
#         if a  == 3:
#             res = res - int(_str[4])
#         else:
#             res = int(_str[a-1]) - res
# print(res)


#         a. Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9.



# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

_list = [1, 2, 3, 5, 1, 5, 3, 10]
a = [i for i in _list if _list.count(i) == 1 ]
print(a)

b = list(filter(lambda x: _list.count(x) == 1, _list ))
print(b)
