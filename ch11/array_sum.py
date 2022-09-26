def array_sum(array: list[int]) -> int:
    if not array:
        return 0
    if len(array) == 1:
        return array[0]
    return array[0] + array_sum(array[1:])


def test_one():
    array = []
    sum = 0
    assert array_sum(array) == sum


def test_two():
    array = [1]
    sum = 1
    assert array_sum(array) == sum


def test_three():
    array = [1, 2, 3]
    sum = 6
    assert array_sum(array) == sum
