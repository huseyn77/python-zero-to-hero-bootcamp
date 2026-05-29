# File Handling Notes

## Topics covered
- Reading files
- Writing files
- Appending data
- File modes
- Context managers
- Working with paths
- File processing exercises

## Key concepts

File handling allows programs to store and retrieve persistent data.
Python provides built-in tools for working with files.

---

## Opening Files

Syntax:
open("filename", "mode")

Example:
file = open("example.txt", "r")

---

## File Modes

### Read mode
    "r"
Opens file for reading.

---

### Write mode
    "w"
Creates new file or overwrites existing file.

---

### Append mode
    "a"
Adds new data to existing file.

---

### Create mode
    "x"
Creates new file only if it does not already exist.

---

## Reading Methods

### read()

Reads entire file.

### readline()

Reads one line.

### readlines()

Reads all lines into a list.

---

## Writing Methods

### write()

Writes text to file.

---

## Context Manager

Recommended syntax:
with open(...) as file:

Benefits:
- Automatically closes file
- Cleaner syntax
- Prevents resource leaks

---

## pathlib Module

Used for safer path management.

Common methods:
- exists()
- name
- absolute()

---

## Best Practices

- Always close files
- Prefer using with statement
- Handle missing files carefully
- Use clear file names