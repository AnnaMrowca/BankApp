from model import calculate
from view import get_input, print_msg


def main_loop():
    var1 = get_input('Provide fist number: ')
    var2 = get_input('Provide second number: ')
    print_msg(calculate(var1, var2))
