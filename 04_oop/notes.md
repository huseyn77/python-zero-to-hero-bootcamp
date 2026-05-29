# OOP Notes

## Topics covered
- Classes
- Constructors
- Attributes
- Methods
- Inheritance
- Polymorphism
- Encapsulation
- Special methods
- __name__ and __main__

## Key concepts
Object-oriented programming organizes code into reusable objects.

## Classes
A class is a blueprint for creating objects.

## Constructor
The __init__ method initializes object attributes.

## Inheritance
Allows one class to inherit functionality from another.

## Polymorphism
Different classes can implement the same method differently.

## Encapsulation
Restricts direct access to internal data.

## Special methods
Python provides built-in methods such as:
- __init__
- __str__
- __len__

## __name__ and __main__

Every Python file has a built-in variable called __name__.

When a file is run directly:

__name__ = "__main__"

When a file is imported as a module:

__name__ = module name

Used to control which code executes only when the script is run directly.

Example:

if __name__ == "__main__":
    main()