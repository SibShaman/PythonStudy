""" Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так:
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

ratio = int(input('Введите коэффициент: '))
res_list = []
def fib(n):
    if n==0:
        return 0
    if n==1 or n==2 or n==-1:
        return 1
    if n>2:
        return fib(n-1) + fib(n-2)
    if n==-2:
        return -1
    if n<-2:
        return fib(n+2) - fib(n+1)


for i in range(-ratio, ratio):
    if i>0:
        res_list.append(fib(i+1))
    else:
        res_list.append(fib(i))

print(res_list)