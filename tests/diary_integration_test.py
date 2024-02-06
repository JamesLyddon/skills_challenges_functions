from lib.diary_entry import DiaryEntry
from lib.diary import Diary

"""
User Story:

I want to be able to keep a diary containing a list of diary entries.

Diary_entries should have:
- 2 strings - a title and content
- a method to count the number of words in the contents
- a method to estimate the time to read contents in minutes (int)
- a method to return the amount of content that could be read given
a wpm and amount of time in minutes

Diary should have:
- a list to hold diary_entries
- a method to add diary_entries to the list
- a method to return a list of all diary_entries in the diary
- a method to return the total word count of all diary_entries' contents combined
- a method to estimate the reading time of all diary_entries' content combined
- a method that returns the diary_entry with the closest reading time to that
specified without going over the allotted time

"""

"""
Create a new Diary
add some diary_entries
check Diary.all() returns all of the entries
"""

def test_add_entries_to_diary_and_list_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Contents 1")
    entry_2 = DiaryEntry("Title 2", "Contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    result = diary.all()
    assert result == [entry_1, entry_2]

"""
Create a new Diary
add some diary_entries
check count_words returns the correct word count for all contents
"""

def test_count_words_with_multiple_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title", "One Two Three Four")
    entry_2 = DiaryEntry("Title Title", "Five")
    entry_3 = DiaryEntry("Title Title Title", "")
    entry_4 = DiaryEntry("", "Six Seven")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.add(entry_4)
    assert diary.count_words() == 7

"""
Create a new Diary
add some diary_entries
check that reading_time() returns the correct int (rounded down)
for all commenst in the entries list
"""

def test_reading_time_for_multiple_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title", "one two three four five")
    entry_2 = DiaryEntry("Title", "one two three four five")
    entry_3 = DiaryEntry("Title", "one two")
    entry_4 = DiaryEntry("Title", "one two three")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.add(entry_4)
    assert diary.reading_time(5) == 3
    entry_5 = DiaryEntry("Title", "one")
    diary.add(entry_5)
    assert diary.reading_time(5) == 3
    assert diary.reading_time(4) == 4
    assert diary.reading_time(1) == 16
    assert diary.reading_time(16) == 1
    assert diary.reading_time(17) == 0
    
"""
Create a new Diary
add some diary_entries
check find_best_entry_for_reading_time() returns
a suitably long/short entry based on the time restraint
if two entries with same length return first encountered
"""

def test_find_best_entry():
    diary = Diary()
    entry_1 = DiaryEntry("Title", "one two three")
    entry_2 = DiaryEntry("Title", "one two")
    entry_3 = DiaryEntry("Title", "one two three four five six")
    entry_4 = DiaryEntry("Title", "one two three four")
    entry_5 = DiaryEntry("Title", "one two three four five")
    entry_6 = DiaryEntry("Title", "one two")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.add(entry_4)
    diary.add(entry_5)
    diary.add(entry_6)
    assert diary.find_best_entry_for_reading_time(1, 2) == entry_2
    assert diary.find_best_entry_for_reading_time(1, 3) == entry_1
    assert diary.find_best_entry_for_reading_time(2, 2) == entry_4
    assert diary.find_best_entry_for_reading_time(2, 5) == entry_3
    assert diary.find_best_entry_for_reading_time(1, 1) == "No suitable entry!"
