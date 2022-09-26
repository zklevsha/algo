"""
Write a function that accepts an array of strings and returns the first
duplicate value it finds. For example, if the array is ["a", "b", "c", "d", "c", "e",
"f"], the function should return "c", since it`s duplicated within the array.
(You can assume that there`s one pair of duplicates within the array.)
Make sure the function has an efficiency of O(N).
"""


from typing import List


def find_duplicate(array: List[str]):
    """
    Searching for duplicates
    """
    count_letters = {}
    for i in array:
        if i in count_letters:
            count_letters[i] = count_letters[i] + 1
        else:
            count_letters[i] = 1

    for letter, count in count_letters.items():
        if count > 1:
            return letter

    return None


def test_one():
    array = ["a", "b", "c", "d", "c", "e", "f"]
    result = "c"
    assert find_duplicate(array) == result


def test_two():
    array = ["a", "a", "c", "d", "c", "e", "f"]
    result = "a"
    assert find_duplicate(array) == result


def test_three():
    array = ["a", "b", "c", "d", "e", "f"]
    result = None
    assert find_duplicate(array) == result
