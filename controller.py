""" controller """
import ui
import complex_calc
import float_calc


def calc_complex():
    """Method complex"""
    num_one = ui.input_num(complex)
    operator = ui.input_operator(str)
    num_two = ui.input_num(complex)
    res = complex_calc.calc(num_one, num_two, operator)
    ui.show_answer(res)


def calc_float():
    """Method float"""
    num_one = ui.input_num(float)
    operator = ui.input_operator(str)
    num_two = ui.input_num(float)
    res = float_calc.calc(num_one, num_two, operator)
    ui.show_answer(res)
