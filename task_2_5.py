# Реализуйте алгоритм перемешивания списка.


import random

my_list = [3, 6, 8, 9, 12, 65, 32]
print('Оргинальный список: ' + str(my_list))

random.shuffle(my_list)
print('Перемешанный список: ' + str(my_list))

res = random.sample(my_list, len(my_list))
print('Перемешанный список: ' + str(res))