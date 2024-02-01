import pytest
from lib.estimate_read_time import estimate_read_time
from data.sample_text import *

def test_empty_string_at_200wpm():
    result = estimate_read_time("")
    assert result == "At 200wpm this 0 word text would take you 0 minutes and 0 seconds to read."

def test_200_words_at_200wpm():
    result = estimate_read_time(sample_200)
    assert result == "At 200wpm this 200 word text would take you 1 minute and 0 seconds to read."

def test_100_words_at_200wpm():
    result = estimate_read_time(sample_100)
    assert result == "At 200wpm this 100 word text would take you 0 minutes and 30 seconds to read."

def test_723_words_at_200wpm():
    result = estimate_read_time(sample_723)
    assert result == "At 200wpm this 723 word text would take you 3 minutes and 37 seconds to read."

def test_200_words_at_47wpm():
    result = estimate_read_time(sample_200, 47)
    assert result == "At 47wpm this 200 word text would take you 4 minutes and 15 seconds to read."

def test_723_words_at_300wpm():
    result = estimate_read_time(sample_723, 300)
    assert result == "At 300wpm this 723 word text would take you 2 minutes and 25 seconds to read."

# Test singular case for minute and second if value is 1

def test_200_words_at_198wpm():
    result = estimate_read_time(sample_200, 198)
    assert result == "At 198wpm this 200 word text would take you 1 minute and 1 second to read."

# Test for None as text argument
    
def test_for_none_for_text():
    with pytest.raises(Exception) as e:
        estimate_read_time(None)
    err_msg = str(e.value)
    assert err_msg == "Text sample must be a string."


# Test for [] as text argument
    
def test_for_list_for_text():
    with pytest.raises(Exception) as e:
        estimate_read_time([1, 2, 3])
    err_msg = str(e.value)
    assert err_msg == "Text sample must be a string."
    
#  Test for string as wpm argument
    
def test_for_string_for_wpm():
    with pytest.raises(Exception) as e:
        estimate_read_time(sample_200, "150")
    err_msg = str(e.value)
    assert err_msg == "Words per Minute must be a non-zero integer."