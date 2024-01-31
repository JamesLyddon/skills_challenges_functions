import pytest
from lib.count_words import count_words

"""
Design
A function called count_words that takes a string as an argument and returns the number of words in that string.
"""

def test_empty_string_returns_0():
    assert count_words("") == 0

def test_single_word_string_returns_1():
    assert count_words("one") == 1

def test_two_word_string_returns_two():
    assert count_words("one two") == 2

def test_ten_word_string_returns_ten():
    assert count_words("one two three four five six seven eight nine ten") == 10

def test_irregular_white_space():
    assert count_words("    one    two    ") == 2

"""
Test for raised exceptions
"""

def test_int_passed_in_raises_exception():
    with pytest.raises(Exception) as e:
        count_words(1)
    err_msg = str(e.value)
    assert err_msg == "Argument must be a string."

def test_bool_passed_in_raises_exception():
    with pytest.raises(Exception) as e:
        count_words(True)
    err_msg = str(e.value)
    assert err_msg == "Argument must be a string."

def test_list_passed_in_raises_exception():
    with pytest.raises(Exception) as e:
        count_words([1, 2, 3])
    err_msg = str(e.value)
    assert err_msg == "Argument must be a string."