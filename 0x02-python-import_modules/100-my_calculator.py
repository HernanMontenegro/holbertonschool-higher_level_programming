#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    av = sys.argv;
    av_len = len(av)
    first = 0
    second = 0

    if (av_len != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif (av[2] != "+" and av[2] != "-" and av[2] != "*" and av[2] != "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    first = int(av[1])
    second = int(av[3])

    if (av[2] == "+"):
        print("{:d} + {:d} = {:d}".format(first, second, first + second))
    if (av[2] == "-"):
        print("{:d} - {:d} = {:d}".format(first, second, first - second))
    if (av[2] == "*"):
        print("{:d} * {:d} = {:d}".format(first, second, first * second))
    if (av[2] == "/"):
        print("{:d} / {:d} = {:d}".format(first, second, first / second))
