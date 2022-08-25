# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math


count =0
accurate = float(input('Введите необходимую точность: '))
while accurate<1:
    res = accurate*10
    accurate = res
    count+=1
print(round(math.pi, int(count)))
