import pytest
from lib.todo import Todo

"""
Given a string
Returns a Todo object with self.task as string and self.complete as False
"""

def test_give_string():
    todo = Todo("walk the dog")
    # assert todo.task == "walk the dog"
    # assert todo.complete == False
    assert todo.__dict__ == {"task":"walk the dog", "complete": False}

"""
Give an empty string
Raises an exception
"""

def test_give_empty_string():
    with pytest.raises(Exception) as e:
        todo = Todo("")
    err_msg = str(e.value)
    assert err_msg == "Task must be a non-empty string."

"""
Check .mark_complete() sets .complete to True
"""

def test_mark_complete():
    todo = Todo("buy milk")
    assert todo.complete == False
    todo.mark_complete()
    assert todo.complete == True