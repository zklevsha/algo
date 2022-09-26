# Write a function that returns the intersection of two arrays.
# The intersection is a third array that contains all values contained within the first two
# arrays. For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8] is [2, 4].
# Your function should have a complexity of O(N). (If your programming
# language has a built-in way of doing this, don’t use it. The idea is to build
# the algorithm yourself.


def intersection(a, b):
    index_a = {i: True for i in a}
    index_b = {i: True for i in b}
    if len(a) < len(b):
        result = [i for i in a if i in index_b]
    else:
        result = [i for i in b if i in index_a]
    return result


def test_one():
    a = [1, 2, 3, 4, 5]
    b = [0, 2, 4, 6, 8]
    res = [2, 4]
    assert intersection(a, b) == res


def test_two():
    a = []
    b = [0, 2, 4, 6, 8]
    res = []
    assert intersection(a, b) == res
