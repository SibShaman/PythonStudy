""" Игра с конфетами, человек против компьютера"""
# 39). Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота




from random import randint


MAX_CANDY = 2021
MAX_VALUE = 28

# Определяем выигрышные позиции из количества конфет на столе
        # остается 28 (2021 - 28 = 1993) - проигрыш
        # остается 29 - берем 1  (2021 - 28 -1 = 1992)- выигрыш
point_win_list = []
point_win = MAX_CANDY
for i in range(0, MAX_CANDY):
    temp_point_win = point_win- MAX_VALUE - 1
    point_win = temp_point_win
    if point_win < 0:
        break
    point_win_list.append(point_win)

point_win_list = point_win_list[::-1]
print(point_win_list)


# Выбор первого хода
player_choice = randint(0,1)
# print(player_choice)

def bot_intellect(num, _list):    
    quantity_candy = 0
    for i in range(len(_list)):
        if _list[0] > num:
            quantity_candy = _list[0] - num
        elif _list[i] > num >_list[i-1]:
            quantity_candy = _list[i] - num
        elif _list[i] == num:
            quantity_candy = randint(1,28)
    return quantity_candy


# числовой ряд по ходам
count_candy = 0
while MAX_CANDY!=0:
    if player_choice == 1:
        while quantity_candy_player < 28:
            quantity_candy_player = int(input('Введите количество конфет которое хотите взять: '))
        else:
            print('Вы неправильно ввели количество конфет')
        count_candy+=quantity_candy_player
        print(f'на руках {count_candy} конфет из 2021')

        quantity_candy_bot = bot_intellect(count_candy, point_win_list)
        print(f'Бот взял {quantity_candy_bot} конфет')
        count_candy+=quantity_candy_bot
        print(f'на руках {count_candy} конфет из 2021')
    else:
        print('Ход бота, попробуй еще')
        break
