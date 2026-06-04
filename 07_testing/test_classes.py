class Calculator:
    def add(self, a, b):
        return a + b


def test_calculator():
    calc = Calculator()

    assert calc.add(2, 3) == 5
    assert calc.add(10, 10) == 20


test_calculator()

print("Class tests passed")