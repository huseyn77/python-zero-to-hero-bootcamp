# Factorial

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(5))


# Check even

def is_even(number):
    return number % 2 == 0

print(is_even(10))
print(is_even(7))