age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Access granted")

if age < 18 or not has_ticket:
    print("Access denied")