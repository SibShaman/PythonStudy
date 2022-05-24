# 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так, например:
    # def val_checker...
    #     ...
    # @val_checker(lambda x: x > 0)
    # def calc_cube(x):
    #    return x ** 3

    # >>> a = calc_cube(5)
    # 125
    # >>> a = calc_cube(-5)
    # Traceback (most recent call last):
    #   ...
    #     raise ValueError(msg)
    # ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?



from functools import wraps


def val_cheker(temp_func): 
    def val_decor(func):
        @wraps(func)
        def dekor_cheker(x):
            try:
                if temp_func(x):
                    return func(x)
                else:
                    raise ValueError

            except ValueError:
                return f'wrong val {x}'
                  
        

        return dekor_cheker
    return val_decor

 
@val_cheker(lambda x: x > 0)
def calc_cube(x):
    return x**3


print(calc_cube(-5))
