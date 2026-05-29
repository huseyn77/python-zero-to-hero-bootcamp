class NegativeNumberError(Exception):
    pass


def check_number(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed")


try:
    check_number(-5)
except NegativeNumberError as error:
    print(error)