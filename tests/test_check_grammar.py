import pytest
from lib.check_grammar import check_grammar

def test_empty_string():
    with pytest.raises(Exception) as e:
        check_grammar("")
    err_msg = str(e.value)
    assert err_msg == "Text argument must be a non-empty string."

def test_lower_first_char():
    assert check_grammar("hi there!") == False

def test_missing_punctuation():
    assert check_grammar("Hi there") == False

def test_incorrect_punctuation():
    assert check_grammar("Hi there,") == False

def test_none_argument_exception():
    with pytest.raises(Exception) as e:
        check_grammar(None)
    err_msg = str(e.value)
    assert err_msg == "Text argument must be a non-empty string."

def test_int_argument_exception():
    with pytest.raises(Exception) as e:
        check_grammar(1)
    err_msg = str(e.value)
    assert err_msg == "Text argument must be a non-empty string."

def test_list_argument_exception():
    with pytest.raises(Exception) as e:
        check_grammar([])
    err_msg = str(e.value)
    assert err_msg == "Text argument must be a non-empty string."

def test_correct_grammar_exclamation():
    assert check_grammar("Hi there!") == True

def test_correct_grammar_question_mark():
    assert check_grammar("Hello? Who's there?") == True

def test_correct_grammar_full_stop():
    assert check_grammar("Ah, there you are.") == True






