while True:
    try:
        age = int(input("Enter your age: "))

        if age < 0:
            raise ValueError

        break

    except ValueError:
        print("Please enter a valid positive number")

print("Age accepted:", age)