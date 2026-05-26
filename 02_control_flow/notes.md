# Control Flow Notes

## Topics covered
- Conditional statements
- Comparison operators
- Logical operators
- for loops
- while loops
- range()
- break
- continue

## Key concepts

Control flow determines how code executes depending on conditions.

---

## Conditional Statements

Used for decision making.

Syntax:

if
elif
else

Example:

if age >= 18:
    print("Adult")

---

## Comparison Operators

- ==
- !=
- >
- <
- >=
- <=

These return Boolean values.

---

## Logical Operators

### and
Both conditions must be true.

### or
At least one condition must be true.

### not
Reverses Boolean value.

---

## for Loops

Used to iterate through sequences.

Example:
for item in items:
    print(item)

---

## while Loops

Repeat while condition is true.

Example:
while count < 5:
    count += 1

---

## range()

Generates sequences of numbers.

Examples:
range(5)
range(1, 10)
range(0, 20, 2)

---

## break

Stops loop execution immediately.

---

## continue

Skips current iteration.

---

## Nested Control Flow

Conditions can exist inside loops.
Loops can exist inside conditions.

---

## Best Practices

- Avoid infinite loops
- Keep conditions simple
- Use descriptive variable names
- Use break carefully