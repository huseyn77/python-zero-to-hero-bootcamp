def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Huseyn", age=18)