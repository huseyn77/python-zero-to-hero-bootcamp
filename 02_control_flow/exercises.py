number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


total = 0

for i in range(1, 11):
    total += i

print("Sum:", total)