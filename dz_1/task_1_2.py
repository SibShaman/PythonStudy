# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, 
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# # К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
# # * Решить задачу под пунктом b, не создавая новый список.


def sum_digit(num):
    result = 0
    while num!=0:
        result += int(num) % 10
        num//=10
    return result

first_list = [i**3 for i in range(1, 1001, 2)]
# print(first_list)                                             # все print закомментированные использовались только для проверки
a = list(filter(lambda x: sum_digit(x)%7==0 , first_list))      # можно было вынести в отдельную функцию, 
                                                                # но не стал так как код короткий и больше lamda нигде не понадобится
# print(a)        
print(f'сумма чисел кратных 7 из первого задания {sum(a)}')            

first_list = [i**3+17 for i in range(1, 1001, 2)]
# print(first_list)   
b = list(filter(lambda x: sum_digit(x)%7==0 , first_list))
# print(b)        
print(f'сумма чисел кратных 7 из второго задания {sum(b)}')    






