# Decorators and Generators Notes

## Topics covered
- Decorators
- Decorator arguments
- Multiple decorators
- Generators
- Generator expressions
- yield
- Iterators

## Key concepts

Decorators modify the behavior of functions.
Generators produce values lazily instead of storing everything in memory.

---

## Decorators

A decorator wraps another function.

Syntax:
@decorator_name

Benefits:
- Code reuse
- Logging
- Authentication
- Timing functions

---

## Decorator Structure

Typical pattern:
def decorator(func):
    def wrapper():
        ...
        func()
        ...
    return wrapper

---

## Multiple Decorators

Decorators can be stacked.

Example:
@decorator1
@decorator2

Execution happens from bottom to top.

---

## Generators

Generators produce values one at a time.

Created using:
yield

Benefits:
- Lower memory usage
- Better performance for large datasets

---

## yield

Unlike return:
- return ends function execution
- yield pauses execution

---

## Generator Expressions

List:
[x for x in range(10)]

Generator:
(x for x in range(10))

Generators are more memory efficient.

---

## Iterators

Objects that support:
- iter()
- next()

Generators are a special type of iterator.

---

## Iterator vs Generator

Iterator:
- Requires iter()
- Manages state manually

Generator:
- Uses yield
- State handled automatically

---

## Best Practices

- Use generators for large data streams
- Keep decorators focused on one task
- Use functools.wraps in production code
- Prefer generators when memory matters