# Functions Notes

## Topics covered
- Function definition
- Parameters
- Arguments
- Return values
- Default parameters
- *args
- **kwargs
- Lambda functions
- map()
- filter()
- Variable scope

## Key concepts

Functions organize code into reusable blocks.

They improve:
- readability
- modularity
- maintainability

---

## Defining Functions

Syntax:

def function_name():
    pass

---

## Parameters and Arguments

Parameters define expected input.
Arguments are actual values passed.

Example:
def greet(name):
    print(name)

---

## Return Values

Functions can return data using:
return

---

## Default Parameters

Provide fallback values.

Example:
def greet(name="Guest"):
    ...

---

## *args

Accept multiple positional arguments.

Example:
def add(*args):
    return sum(args)

---

## **kwargs

Accept multiple keyword arguments.

Example:
def info(**kwargs):
    ...

---

## Lambda Functions

Anonymous one-line functions.

Example:
lambda x: x * 2

---

## map()

Applies function to each element.

---

## filter()

Filters elements based on condition.

---

## Variable Scope

### Local scope
Accessible only inside function

### Global scope
Accessible throughout file

---

## Best Practices

- Keep functions small
- Use descriptive names
- Return values instead of printing when possible
- Avoid excessive nesting