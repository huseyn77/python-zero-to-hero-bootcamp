try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
else:
    print("Success:", number)
finally:
    print("Execution finished")