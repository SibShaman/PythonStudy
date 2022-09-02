""" Methods for complex num"""


def calc(num_one: complex, num_two: complex, operator):
    """ Operators for complex number"""
    if operator == '+':
        return num_one + num_two
    if operator == '-':
        return num_one - num_two
    if operator == '*':
        return num_one * num_two
    if operator == '/':
        return num_one / num_two
