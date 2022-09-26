def double_array(array: list[int], index: int):
    if index < len(array):
        array[index] = array[index] * 2
        index += 1
        double_array(array, index)


def test_double_array():
    array = [2, 3, 5]
    result = [4, 6, 10]
    double_array(array, 0)
    assert array == result
