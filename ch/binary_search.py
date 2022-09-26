
def search(value: int, arr: list[int]) -> int | None:
    left = 0
    right = len(arr) - 1
    middle = 0
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] < value:
            left = middle + 1
        elif arr[middle] > value:
            right = middle - 1
        else:
            return middle

    # if we are here, no value was found
    return None


def test_case_one():
    arr = [1, 3, 4, 5, 6, 7, 9, 10, 15, 20, 25, 50]
    value = 3
    expected = 1
    assert search(value, arr) == expected


def test_case_two():
    arr = [1, 3, 4, 5, 6, 7, 9, 10, 15, 20, 25, 50]
    value = 1
    expected = 0
    assert search(value, arr) == expected


def test_case_three():
    arr = [1, 3, 4, 5, 6, 7, 9, 10, 15, 20, 25, 50]
    value = 50
    expected = 11
    assert search(value, arr) == expected


def test_case_four():
    arr = [1, 3, 4, 5, 6, 7, 9, 10, 15, 20, 25, 50]
    value = 51
    expected = None
    assert search(value, arr) == expected


def test_case_five():
    arr = []
    value = 50
    expected = None
    assert search(value, arr) == expected


def test_case_six():
    arr = [9]
    value = 9
    expected = 0
    assert search(value, arr) == expected


if __name__ == "__main__":
    test_case_three()
