# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет


def first_way():
    your_day = int(input('Введите номер дня недели'))

    if  your_day > 7:
        print('Нет такого дня недели') 
    elif your_day != 6 and your_day != 7:
        print('Нет - это рабочий день')     
    else:
        print('Да - это выходной день')


def second_way():
    my_week = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }

    your_day = int(input('Введите номер дня недели'))
    
    if  your_day > 7:
        return 'Нет такого дня недели'
    elif your_day != 6 and your_day != 7:
        return f'Нет {my_week[your_day]} - это рабочий день'
    else:
        return f'Да {my_week[your_day]} - это выходной день'


print(first_way())
print(second_way())