
"""
Write a function that returns the first non-duplicated character in a string.
For example, the string, "minimum" has two characters that only exist
once—the "n" and the "u", so your function should return the "n", since it
occurs first. The function should have an efficiency of O(N).
"""
import pytest


def find_unique(string: str) -> str:
    """
    find unique
    """
    letter_count: dict[str, int] = {}
    for letter in string:
        try:
            letter_count[letter] = letter_count[letter]+1
        except KeyError:
            letter_count[letter] = 1
    for letter, count in letter_count.items():
        if count == 1:
            return letter
    raise ValueError(f'string {string} does not contains unique value')


def test_one():
    """
    test one
    """
    string = "minimum"
    result = "n"
    assert find_unique(string) == result


def test_two():
    """
    test two
    """
    string = "nn"
    error_msg = f'string {string} does not contains unique value'
    with pytest.raises(ValueError, match=error_msg):
        find_unique(string)
