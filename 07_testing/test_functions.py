def multiply(a, b):
    return a * b


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(5, 0) == 0


test_multiply()

print("Function tests passed")