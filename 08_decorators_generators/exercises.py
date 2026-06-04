def logger(func):
    def wrapper():
        print(f"Running {func.__name__}")
        func()
    return wrapper


@logger
def test():
    print("Testing")


test()


# Generator

def even_numbers(limit):
    for number in range(limit):
        if number % 2 == 0:
            yield number


for number in even_numbers(10):
    print(number)