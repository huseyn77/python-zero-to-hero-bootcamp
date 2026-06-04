def is_even(number):
    return number % 2 == 0


def test_is_even():
    assert is_even(2) is True
    assert is_even(7) is False
    assert is_even(10) is True


test_is_even()

print("Exercise tests passed")