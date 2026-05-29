# Error Handling Notes

## Topics covered
- try / except
- Multiple exceptions
- else block
- finally block
- Raising exceptions
- Custom exceptions
- Input validation

## Key concepts

Error handling prevents programs from crashing unexpectedly.
Python uses exceptions to signal runtime errors.

---

## try

Code that may cause an error is placed inside try.

Example:
try:
    risky_code()

---

## except

Handles exceptions.

Example:
except ValueError:

---

## Multiple Exceptions

Programs can handle different exception types separately.

Common exceptions:
- ValueError
- TypeError
- ZeroDivisionError
- FileNotFoundError

---

## else

Runs only if no exception occurs.

---

## finally

Runs no matter what.

Useful for:
- Closing files
- Cleaning resources

---

## raise

Used to trigger exceptions manually.

Example:
raise ValueError("Invalid value")

---

## Custom Exceptions

Create specific error types by inheriting from Exception.

Example:
class MyError(Exception):
    pass

---

## Input Validation

Exceptions can ensure user input is valid.

Used to:
- Prevent crashes
- Improve reliability
- Guide user correction

---

## Best Practices

- Catch specific exceptions
- Avoid broad except blocks
- Use meaningful error messages
- Validate external input