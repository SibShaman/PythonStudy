""" Игра с конфетами, человек против компьютера"""
# 39). Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

from random import randint


MAX_CANDY = 120
MAX_VALUE = 28

# Определяем выигрышные позиции из количества конфет на столе
        # остается 28 (2021 - 28 = 1993) - проигрыш
        # остается 29 - берем 1  (2021 - 28 -1 = 1992)- выигрыш
def bot_intellect(num):
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
    quantity_candy = 0
    for i in range(len(point_win_list)):
        if point_win_list[0] > num:
            quantity_candy = point_win_list[0] - num
        elif point_win_list[i] > num > point_win_list[i-1]:
            quantity_candy = point_win_list[i] - num
        elif point_win_list[i] == num:
            quantity_candy = randint(1,28)
    return quantity_candy


# Выбор первого хода
player_choice = randint(0,1)
# if player_choice == 1:
#     print('Вы ходите первым ')
# else:
#     print('Вы проиграли жеребьевку, первый ход за ботом')

# числовой ряд по ходам
count_candy = 0
while MAX_CANDY>count_candy:
    if player_choice == 1:
        # ход игрока
        while True:
            quantity_candy_player = int(input('Введите количество конфет которое хотите взять: '))
            if quantity_candy_player < 29 and quantity_candy_player > 0:
                break
            else:
                print('Вы неправильно ввели число, поробуйте еще раз ')
        count_candy+=quantity_candy_player
        print(f'на руках {count_candy} конфет из 2021')
        # ход компьютера
        quantity_candy_bot = bot_intellect(count_candy)
        print(f'Бот взял {quantity_candy_bot} конфет')
        count_candy+=quantity_candy_bot
        print(f'на руках {count_candy} конфет из 2021')
    elif player_choice == 0:
        # ход компьютера
        quantity_candy_bot = bot_intellect(count_candy)
        print(f'Бот взял {quantity_candy_bot} конфет')
        count_candy+=quantity_candy_bot
        print(f'на руках {count_candy} конфет из 2021')
        # ход игрока
        while True:
            quantity_candy_player = int(input('Введите количество конфет которое хотите взять: '))
            if quantity_candy_player < 29 and quantity_candy_player > 0:
                break
            else:
                print('Вы неправильно ввели число, попробуйте еще раз ')
        count_candy+=quantity_candy_player
        print(f'на руках {count_candy} конфет из 2021')
else:
    print('Вы вышли за пределы диапазона')
