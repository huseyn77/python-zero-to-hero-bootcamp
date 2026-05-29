try:
    number = int(input("Enter number: "))
    result = 10 / number
    print(result)

except ValueError:
    print("Please enter a valid integer")

except ZeroDivisionError:
    print("Cannot divide by zero")