def print_last_digit(number):
    if number < 0:
        print(str(-number % 10), end='')
        return (-number % 10)
    print(str(number % 10), end='')
    return (number % 10)
