class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")


def main():
    student = Student("Huseyn")
    student.introduce()


if __name__ == "__main__":
    main()