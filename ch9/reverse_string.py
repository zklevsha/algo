"""
Write a function that uses a stack to reverse a string. (For example, "abcde"
would become "edcba".) You can work with our earlier implementation of
the Stack class.
"""

from stack import Stack


def reverse(string: str) -> str:
    stack = Stack()
    for letter in string:
        stack.push(letter)

    reversed = []
    while True:
        letter = stack.pop()
        if not letter:
            break
        reversed.append(letter)
    return "".join(reversed)


def test():
    string = "abcde"
    result = "edcba"
    assert reverse(string) == result
