from tabnanny import check
import pytest

"""
Write a linter to check open and closed brases
Exception#1: brackets are not closed: "(var x = 2;" 
Exception#2: brackets are not opened: "var x = 2;)"
Exception#3: brackets type mismatch: (var x = [1, 2, 3)]; 
"""

from stack import Stack


class ErrorBracketsNotClosed(Exception):
    """
    Raised when brackets not closed: "(var x = 2;" 
    """


class ErrorBracketsNotOpened(Exception):
    """
    Raised when brackets not opened: "var x = 2;)" 
    """


class ErrorBracketsTypeMismatch(Exception):
    """
    Raised when brackets does not match: (var x = [1, 2, 3)]; 
    """


def check_string(string: str):
    stack = Stack()
    brackets = {"[": {"is_open": True, "sibling": "]"},
                "]": {"is_open": False, "sibling": "["},
                "(": {"is_open": True, "sibling": "]"},
                ")": {"is_open": False, "sibling": "("},
                "{": {"is_open": True, "sibling": "}"},
                "}": {"is_open": False, "sibling": "{"}}

    for s in string:
        if s not in brackets.keys():
            continue

        bracket_info = brackets[s]
        if bracket_info['is_open']:
            stack.push(s)
        else:
            stack_bracket = stack.pop()
            if not stack_bracket:
                # Stack is empty, which means that brackets was not opened
                raise ErrorBracketsNotOpened
            if stack_bracket != bracket_info["sibling"]:
                # backet from stack does not match closing bracket
                raise ErrorBracketsTypeMismatch

    # if after iteration, stack is not empty, bracket was not closed
    value = stack.pop()
    if value:
        raise ErrorBracketsNotClosed


def test_bracket_not_closed():
    string = "(var x = 2;"
    with pytest.raises(ErrorBracketsNotClosed):
        check_string(string)


def test_bracket_not_opened():
    string = "var x = { y: [1, 2, 3] })"
    with pytest.raises(ErrorBracketsNotOpened):
        check_string(string)


def test_bracket_mismatch():
    string = "(var x = [1, 2, 3)]"
    with pytest.raises(ErrorBracketsTypeMismatch):
        check_string(string)


def test_good_string():
    string = "(var x = {y: [1,2,3]})"
    check_string(string)
