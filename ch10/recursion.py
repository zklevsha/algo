
def factorial(value: int) -> int:
    if value == 1:
        return 1
    else:
        return value * factorial(value-1)


def sum(low: int, high: int) -> int:
    if low == high:
        return 1
    return high + sum(low, high - 1)


def test_factorial():
    assert factorial(5) == 120


def test_sum():
    assert sum(1, 100) == 5050
