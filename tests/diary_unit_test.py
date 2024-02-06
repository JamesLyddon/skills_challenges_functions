from lib.diary import Diary
"""
Check diary initialises with an empty list
"""

def test_initialises_with_empty_list():
    diary = Diary()
    assert diary.entries == []
