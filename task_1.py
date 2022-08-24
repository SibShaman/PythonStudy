# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math


accurate = int(input('Введите необходимую точность: '))
print(round(math.pi, accurate))
