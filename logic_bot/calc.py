"""Логика для расчета результата по комплексным числам и вещественным"""


def calc_complex(num_one: complex, num_two: complex, operator):
    """ Operators for complex number"""
    if operator == '+':
        return num_one + num_two
    if operator == '-':
        return num_one - num_two
    if operator == '*':
        return num_one * num_two
    if operator == '/':
        return num_one / num_two


def calc_float(num_one: float, num_two: float, operator):
    """ Operators for float number"""
    if operator == '+':
        return num_one + num_two
    if operator == '-':
        return num_one - num_two
    if operator == '*':
        return num_one * num_two
    if operator == '/':
        return num_one / num_two
