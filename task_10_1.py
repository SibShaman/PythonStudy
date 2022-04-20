# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |

# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.


from itertools import zip_longest


class Matrix:
    def __init__(self, my_list):
       self.my_list = my_list
    

    def __add__(self, other):
        result_matrix = []      
        for x,y in zip_longest(self.my_list, other.my_list, fillvalue=0):
            result = list(map(lambda x: x[0]+x[1], zip_longest(x, y, fillvalue=0)))
            result_matrix.append(result)
        return Matrix(result_matrix)


    def __str__(self) -> str:
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''


matrix_one = [
                [31, 22], 
                [37, 43], 
                [51, 86]
]
matrix_two = [
                [3, 5, 32],
                [2, 4, 6],
                [-1, 64, -8]]

a = Matrix(matrix_one)
b = Matrix(matrix_two)

print(b.__add__(a))
print(a.__add__(b))