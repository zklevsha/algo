import pytest
"""
Write a function that accepts a string that contains all the letters of the
alphabet except one and returns the missing letter. For example, the string,
"the quick brown box jumps over a lazy dog" contains all the letters of the alphabet
except the letter, "f". The function should have a time complexity of O(N).
"""


def find_missing_letter(string: str) -> str:
    """
    serarching missing letter
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    alphabet_count = {i: 0 for i in alphabet}
    for i in string:
        try:
            alphabet_count[i] = alphabet_count[i]+1
        except KeyError as exc:
            raise ValueError(f"{i} is not an alphabet letter") from exc
    for letter, count in alphabet_count.items():
        if count == 0:
            return letter
    raise ValueError(f"string {string} contains all letters from alphabet")


def test_one():
    """
    first test
    """
    string = "the quick brown box jumps over a lazy dog"
    result = "f"
    assert find_missing_letter(string) == result


def test_two():
    """
    second test
    """
    string = "the quick brown box jumps over a lazy dog f"
    err_msg = f'string {string} contains all letters from alphabet'
    with pytest.raises(ValueError, match=err_msg):
        find_missing_letter(string)
