class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Hello")


class Student(Person):
    def study(self):
        print("Studying Python")


student = Student("Huseyn")

student.speak()
student.study()