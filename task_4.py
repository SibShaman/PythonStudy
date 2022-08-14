# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


num_quarter = int(input('Введите номер четверти плоскости: '))

a = [
    ((0, 2_147_483_647), (0, 2_147_483_647)), 
    ((0, -2_147_483_647), (0, 2_147_483_647)), 
    ((0, -2_147_483_647), (0, -2_147_483_647)), 
    ((0, 2_147_483_647), (0, -2_147_483_647))
]

if num_quarter == 1:
    print(f'в этой четверти координаты попадают в диапазон x = {a[0][0]}, y = {a[0][1]}')
elif num_quarter == 2:
    print(f'в этой четверти координаты попадают в диапазон x = {a[1][0]}, y = {a[1][1]}')
elif num_quarter == 3:
    print(f'в этой четверти координаты попадают в диапазон x = {a[2][0]}, y = {a[2][1]}')
elif num_quarter == 4:
    print(f'в этой четверти координаты попадают в диапазон x = {a[3][0]}, y = {a[3][1]}')
else:
    print('такой четверти не существует')  