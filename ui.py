""" User Interface"""


def input_num(num):
    """ input num"""
    if num is complex:
        return complex(num)
    if num is float:
        return float(num)


def input_operator(oper):
    """ input operator"""
    return oper


def show_answer(answer):
    """ Show answer"""
    print(answer)
