from lib.diary_entry import DiaryEntry
"""
Check diary entry initialises with title and contents arguments
stored in properties
"""

def test_initialises_with_title_and_contents():
    entry = DiaryEntry("Title text", "Contents text")
    assert [entry.title, entry.contents] == ["Title text", "Contents text"]

"""
Check count_words() returns an int representing the words
in the entry's contents
"""

def test_count_words():
    entry_1 = DiaryEntry("Title", "one two three")
    entry_2 = DiaryEntry("Title Title", "one")
    entry_3 = DiaryEntry("Title", "")
    assert entry_1.count_words() == 3
    assert entry_2.count_words() == 1
    assert entry_3.count_words() == 0

"""
Check reading_time() returns 
correct time in minutes as an int (floats rounded down)
"""

def test_reading_time_returns_minutes_int_correctly():
    entry_1 = DiaryEntry("Title", "One Two Three Four Five Six")
    entry_2 = DiaryEntry("", "One Two Three Four")
    entry_3 = DiaryEntry("Title Title", "")
    entry_4 = DiaryEntry("Title", "One Two Three")
    assert entry_1.reading_time(1) == 6
    assert entry_2.reading_time(2) == 2
    assert entry_3.reading_time(2) == 0
    assert entry_4.reading_time(2) == 1