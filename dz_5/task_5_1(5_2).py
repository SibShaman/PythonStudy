# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.


num_user = int(input("Введите число: "))

num_gen = [i for i in range(1, num_user+1, 2)]
print(num_gen)