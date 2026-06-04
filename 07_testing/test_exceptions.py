import unittest


def divide(a, b):
    return a / b


class TestExceptions(unittest.TestCase):

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()