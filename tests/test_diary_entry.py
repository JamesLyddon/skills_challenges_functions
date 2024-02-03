import pytest
from lib.diary_entry import DiaryEntry

"""
When passed two string for title and content
Creates a new DiaryEntry object instance with correct values
"""

def test_instantiate():
    entry = DiaryEntry("Entry title", "Entry contents")
    assert entry.title == "Entry title"
    assert entry.contents == "Entry contents"

"""
When .format() is called on an object
Returns a formatted string with correct values
"""

def test_format_returns_correctly():
    entry = DiaryEntry("Entry title", "Entry contents")
    result = entry.format()
    assert result == "Entry title: Entry contents"

"""
When .count_words() is called on an object
Returns the total words in the entry (title count + contents count)
"""

def test_count_words_returns_correct_number():
    entry = DiaryEntry("One Two", "One Two Three")
    result = entry.count_words()
    assert result == 5

"""
When .reading_time(wpm) is called on an object with an int
Return the (word count / wpm rate) as an int representing minutes
"""

def test_reading_time_calculates_correctly():
    entry = DiaryEntry("One Two Three Four Five", "One Two Three Four Five")
    result = entry.reading_time(2)
    assert result == 5

"""
When ,reading_chunk(wpm, minutes) is called it should
Return a section of the content that could be read in that time
"""

def test_reading_chunk_returns_first_section():
    entry = DiaryEntry("One Two Three", "Four Five Six Seven Eight Nine Ten")
    result = entry.reading_chunk(1, 5)
    assert result == "One Two Three Four Five"

"""
When ,reading_chunk(wpm, minutes) is called twice it should
Return a section of the content, then return the next section from where the last section ended
"""

def test_reading_chunk_returns_subsequent_sections():
    entry = DiaryEntry("One Two Three", "Four Five Six Seven Eight Nine Ten")
    result_one = entry.reading_chunk(1, 5)
    result_two = entry.reading_chunk(1, 5)
    assert result_one == "One Two Three Four Five"
    assert result_two == "Six Seven Eight Nine Ten"

"""
Test again for 3 consecutive reads, the last overflowing bounds
"""

def test_reading_chunk_returns_three_subsequent_sections():
    entry = DiaryEntry("One Two Three", "Four Five Six Seven Eight Nine Ten")
    result_one = entry.reading_chunk(1, 3)
    result_two = entry.reading_chunk(1, 3)
    result_three = entry.reading_chunk(1, 5)
    assert result_one == "One Two Three"
    assert result_two == "Four Five Six"
    assert result_three == "Seven Eight Nine Ten"

"""
Test again for 3 consecutive reads, the last overflowing bounds
Then check a 4th read starts from the beginning again
"""

def test_reading_chunk_returns_three_subsequent_sections_and_fourth_starts_from_scratch():
    entry = DiaryEntry("One Two Three", "Four Five Six Seven Eight Nine Ten")
    result_one = entry.reading_chunk(1, 3)
    result_two = entry.reading_chunk(1, 3)
    result_three = entry.reading_chunk(1, 5)
    result_four = entry.reading_chunk(1, 3)
    assert result_one == "One Two Three"
    assert result_two == "Four Five Six"
    assert result_three == "Seven Eight Nine Ten"
    assert result_four == "One Two Three"