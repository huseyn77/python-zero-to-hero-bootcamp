def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper


def exclamation(func):
    def wrapper():
        return func() + "!"
    return wrapper


@exclamation
@uppercase
def greet():
    return "hello"


print(greet())