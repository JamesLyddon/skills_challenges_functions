import pytest
from lib.grammar_stats import GrammarStats

def test_initialisation():
    gs = GrammarStats()
    assert gs != None
    assert gs._END_CHARS == ('.', '?', '!')
    assert gs.tests == 0
    assert gs.passed == 0

def test_check_method_with_empty_string_raises_exception():
    gs = GrammarStats()
    with pytest.raises(Exception) as e:
        gs.check("")
    err_msg = str(e.value)
    assert err_msg == "Text input must be a non-empty string."

def test_check_method_with_non_string_raises_exception():
    gs = GrammarStats()
    with pytest.raises(Exception) as e:
        gs.check([1,2])
    err_msg = str(e.value)
    assert err_msg == "Text input must be a non-empty string."

def test_check_method_with_none_raises_exception():
    gs = GrammarStats()
    with pytest.raises(Exception) as e:
        gs.check(None)
    err_msg = str(e.value)
    assert err_msg == "Text input must be a non-empty string."

def test_check_method_with_length_1_returns_false():
    gs = GrammarStats()
    result = gs.check("F")
    assert result == False

def test_check_method_with_two_correct_chars_returns_true():
    gs = GrammarStats()
    result = gs.check("Q?")
    assert result == True

def test_check_method_returns_true_for_uppercase_first_punctuation_correct_last():
    gs = GrammarStats()
    result_one = gs.check("Hey there.")
    result_two = gs.check("What's up!")
    result_three = gs.check("Do what!?")
    assert result_one == True
    assert result_two == True
    assert result_three == True

def test_check_method_returns_false_for_incorrect_first_character():
    gs = GrammarStats()
    result_one = gs.check("hey there!")
    result_two = gs.check(" ey there!")
    result_three = gs.check("!ey there!")
    assert result_one == False
    assert result_two == False
    assert result_three == False

def test_check_method_returns_false_for_incorrect_last_character():
    gs = GrammarStats()
    result_one = gs.check("Hey there ")
    result_two = gs.check("Hey there,")
    result_three = gs.check("Hey thereH")
    assert result_one == False
    assert result_two == False
    assert result_three == False

def test_check_method_increments_tests_pass_or_fail():
    gs = GrammarStats()
    assert gs.tests == 0
    gs.check("Hey there!")
    assert gs.tests == 1
    gs.check("hey there")
    assert gs.tests == 2

def test_check_method_increments_passed_on_pass_only():
    gs = GrammarStats()
    assert gs.passed == 0
    gs.check("Hey there!")
    gs.check("hey there")
    gs.check("Woozle wazzle?")
    gs.check("1")
    assert gs.passed == 2

def test_percentage_good_raises_exception_when_no_tests_run():
    gs = GrammarStats()
    with pytest.raises(Exception) as e:
        gs.percentage_good()
    err_msg = str(e.value)
    assert err_msg == "You haven't checked any sentences yet."

def test_percentage_good_returns_int_for_percentages_of_tests_passed():
    gs = GrammarStats()
    gs.check("Hey there!")
    assert gs.percentage_good() == 100
    gs.check("hey")
    assert gs.percentage_good() == 50
    gs.check("h")
    assert gs.percentage_good() == 33