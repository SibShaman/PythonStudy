# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

your_day = int(input('Введите номер дня недели'))

if  your_day > 7:
    print('Нет такого дня недели') 
elif your_day != 6 and your_day != 7:
    print('Нет - это рабочий день')     
else:
    print('Да - это выходной день')


