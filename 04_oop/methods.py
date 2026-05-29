class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"


student = Student("Huseyn")

print(student.introduce())