def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


print(safe_divide(10, 2))
print(safe_divide(10, 0))


try:
    with open("missing.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")