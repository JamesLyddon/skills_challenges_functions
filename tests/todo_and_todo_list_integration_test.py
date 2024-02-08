from lib.todo import Todo
from lib.todo_list import TodoList

"""
Test .add() adds a given Todo object to the list .todos
"""

def test_add_todo():
    tdlist = TodoList()
    todo = Todo("walk the dog")
    tdlist.add(todo)
    assert tdlist.todos[0] == todo

def test_multiple_add_operations():
    tdlist = TodoList()
    todo_1 = Todo("walk the dog")
    todo_2 = Todo("feed the cat")
    todo_3 = Todo("buy some milk")
    tdlist.add(todo_1)
    tdlist.add(todo_2)
    tdlist.add(todo_3)
    assert tdlist.todos[0].task == "walk the dog"
    assert tdlist.todos[1].task == "feed the cat"
    assert tdlist.todos[2].task == "buy some milk"

"""
Test .incomplete() returns all tasks where .complete == False
"""

def test_incomplete_returns_list_of_incomplete_todos():
    tdlist = TodoList()
    todo_1 = Todo("walk the dog")
    todo_2 = Todo("feed the cat")
    todo_3 = Todo("buy some milk")
    tdlist.add(todo_1)
    tdlist.add(todo_2)
    tdlist.add(todo_3)
    assert tdlist.todos[0].task == "walk the dog"
    assert tdlist.todos[1].task == "feed the cat"
    assert tdlist.todos[2].task == "buy some milk"
    tdlist.todos[0].mark_complete()
    tdlist.todos[2].mark_complete()
    incomplete = tdlist.incomplete()
    assert len(incomplete) == 1
    assert incomplete[0].task == "feed the cat"

"""
Test .complete() returns all tasks where .complete == True
"""

def test_complete_returns_list_of_complete_todos():
    tdlist = TodoList()
    todo_1 = Todo("walk the dog")
    todo_2 = Todo("feed the cat")
    todo_3 = Todo("buy some milk")
    tdlist.add(todo_1)
    tdlist.add(todo_2)
    tdlist.add(todo_3)
    assert tdlist.todos[0].task == "walk the dog"
    assert tdlist.todos[1].task == "feed the cat"
    assert tdlist.todos[2].task == "buy some milk"
    tdlist.todos[0].mark_complete()
    tdlist.todos[2].mark_complete()
    complete = tdlist.complete()
    assert len(complete) == 2
    assert complete[0].task == "walk the dog"
    assert complete[1].task == "buy some milk"

"""
Test .giveup makes all todos as complete
"""

def test_giveup_marks_all_todos_complete():
    tdlist = TodoList()
    todo_1 = Todo("walk the dog")
    todo_2 = Todo("feed the cat")
    todo_3 = Todo("buy some milk")
    tdlist.add(todo_1)
    tdlist.add(todo_2)
    tdlist.add(todo_3)
    assert tdlist.todos[0].complete == False
    assert tdlist.todos[1].complete == False
    assert tdlist.todos[2].complete == False
    tdlist.give_up()
    assert tdlist.todos[0].complete == True
    assert tdlist.todos[1].complete == True
    assert tdlist.todos[2].complete == True
