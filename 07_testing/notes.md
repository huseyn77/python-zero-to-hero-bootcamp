# Testing Notes

## Topics covered
- Assertions
- Function testing
- Class testing
- unittest framework
- setUp()
- tearDown()
- Exception testing

## Key concepts

Testing verifies that code behaves as expected.

Benefits:
- Detect bugs early
- Improve reliability
- Simplify maintenance
- Increase confidence in code changes

---

## Assertions

Assertions check whether a condition is true.

Example:
assert 2 + 2 == 4

If the condition is false, Python raises an AssertionError.

---

## Testing Functions

Functions should be tested with:
- Normal input
- Edge cases
- Invalid input

Example:
def add(a, b):
    return a + b

assert add(2, 3) == 5

---

## Testing Classes

Objects and methods should be verified.

Example:
calculator = Calculator()
assert calculator.add(2, 3) == 5

---

## unittest Module

Python includes a built-in testing framework.

Import:
import unittest
Create tests by inheriting from:
unittest.TestCase

---

## Common Assertions

assertEqual(a, b)
assertTrue(condition)
assertFalse(condition)
assertRaises(Exception)

---

## setUp()

Runs before every test.
Used to prepare test data.

Example:
def setUp(self):
    self.data = [1, 2, 3]

---

## tearDown()

Runs after every test.
Used for cleanup.

Example:
def tearDown(self):
    self.data = None

---

## Testing Exceptions

Verify that code raises expected errors.

Example:
with self.assertRaises(ValueError):
    function()

---

## Best Practices

- Write small focused tests
- Test edge cases
- Use descriptive test names
- Keep tests independent
- Automate testing whenever possible

---

## Real-World Testing Tools

Popular Python testing libraries:
- unittest
- pytest
- nose2

pytest is currently the most widely used testing framework.