from lib.make_snippet import make_snippet

"""
When less that 6 words should return string as it was passed in
"""

def test_for_empty_string():
    result = make_snippet("")
    assert result == ""

def test_for_one_word_phrase():
    result = make_snippet("one")
    assert result == "one"

def test_for_three_word_phrase():
    result = make_snippet("one two three")
    assert result == "one two three"

def test_for_5_word_phrase():
    result = make_snippet("one two three four five")
    assert result == "one two three four five"

"""
When 6 words or more should return first five words followed by '...'
"""

def test_for_6_word_phrase():
    result = make_snippet("one two three four five six")
    assert result == "one two three four five..."

def test_for_10_word_phrase():
    result = make_snippet("one two three four five six seven eight nine ten")
    assert result == "one two three four five..."