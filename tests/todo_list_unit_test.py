from lib.todo_list import TodoList

"""
Initialises with an empty list called .todos
"""

def test_initialisation():
    tdlist = TodoList()
    assert tdlist.todos == []