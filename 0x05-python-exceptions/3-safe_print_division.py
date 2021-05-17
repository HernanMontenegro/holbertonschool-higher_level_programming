#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0
    zero = False
    try:
        res = a / b
    except ZeroDivisionError:
        zero = True
    finally:
        print("Inside result: ", end="")
        if (zero):
            print("{}".format(None))
            return None
        print("{}".format(res))
        return res
