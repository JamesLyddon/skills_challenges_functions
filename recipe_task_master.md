## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

nouns = task
verbs = add task to list, see list of tasks

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

nouns = task
verbs = mark as complete (delete entirely? or just remove from 'incomplete' list into 'complete' list)

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TaskMaster:
    # User-facing properties:
    #   task: string e.g. "walk the dog before work"
    #   tasks: list of task strings e.g. ["walk the dog before work", "book dentist appointment"]

    def __init__(self, name):
        # Parameters:
        #   self._tasks = []
        # Side effects:
        #   none
        pass # No code here yet

    def add_task(self, text):
        # Parameters:
        #   text: string representing a single task
        # Returns:
        #   None
        # Side-effects
        #   creates task string and adds it to self.tasks list
        #   throws the exception "Task must be a non-empty string" if text argument is not a non-empty string
        pass # No code here yethecking self._taskself):
        # Returns:
        #   self._tasks list
        # Side-effects:
        #   None

    def list_tasks(self):
        # Returns:
        #   None
        # Side-effects:
        #   prints a numbered line by line display of tasts to complete
        #   raises exception "No tasks to do!" if list is empty
        pass # No code here yet

    def mark_task_complete(self, number):
        # Returns:
        #   None
        # Side-effects:
        #   Throws exception "Task does not exist." if no such task in tasks
        #   deletes task string from list
        #   calls list_tasks(self) to display change 
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Check initialises correctly and creates self.tasks = []
"""
def test_initialisation():
    tm = TaskMaster()
    assert tm != None
    assert tm._tasks == []

"""
Check add_task("") throws the exception "Task must be a non-empty string."
"""
def test_add_task_as_empty_string():
    tm = TaskMaster()
    with pytest.raises(Exception) as e:
        tm.add_task("")
    err = str(e.value)
    assert err == "Task must be a non-empty string."

"""
Check add_task(1) throws the exception "Task must be a non-empty string."
"""
def test_add_task_as_empty_string():
    tm = TaskMaster()
    with pytest.raises(Exception) as e:
        tm.add_task(1)
    err = str(e.value)
    assert err == "Task must be a non-empty string."

"""
Check add_task("walk the dog") adds string "walk the dog" to the list of tasks
by checking self._tasks
"""
def test_add_task_successfully():
    tm = TaskMaster()
    tm.add_task("walk the dog")
    result = tm._tasks
    assert result == ["walk the dog"]
"""
Check add_task() called 3 times adds 3 tasks to the list of tasks
by calling list_tasks()
"""
def test_add_3_tasks_successfully():
    tm = TaskMaster()
    tm.add_task("walk the dog")
    tm.add_task("pay phone bill")
    tm.add_task("buy milk")
    result = tm._tasks
    assert result = ["walk the dog", "pay phone bill", "buy milk"]

"""
Check list_tasks() raises the exception "No tasks to do!" if list is empty 
"""
def test_list_tasks_raises_exception_when_list_empty():
    tm = TaskMaster()
    with pytest.raises(Exception) as e:
        tm.list_tasks()
    err = str(e.value)
    assert err = "No tasks to do!"

"""
Check mark_task_complete succefully removes a task from the list
"""
def test_mark_task_complete_removes_task_from_list():
    tm = TaskMaster()
    tm.add_task("walk the dog")
    tm.add_task("pay phone bill")
    tm.add_task("buy milk")
    tm.mark_task_complete(2)
    result = tm._tasks
    assert result = ["walk the dog", "buy milk"]

"""
Check mark_task_complete raises the exception "Task does not exist." if index is out of bounds
"""
def test_mark_task_complete_raises_exception_if_out_of_bounds():
    tm = TaskMaster()
    tm.add_task("walk the dog")
    tm.add_task("pay phone bill")
    tm.add_task("buy milk")
    with pytest.raises(Exception) as e:
        tm.mark_task_complete(7)
    err = str(e.value)
    assert err = "Task does not exist."

"""
Check mark_task_complete raises the exception "Task does not exist." if task list is empty
"""
def test_mark_test_complete_on_empty_list():
    tm = TaskMaster()
    with pytest.raises(Exception) as e:
        tm.mark_task_complete(1)
    err = str(e.value)
    assert err = "Task does not exist."

"""
Check mark_task_complete raises the exception "Please enter the task's list number (non-zero and non-negative integer)." if given 0
"""
def test_mark_test_complete_0():
    tm = TaskMaster()
    with pytest.raises(Exception) as e:
        tm.mark_task_complete(0)
    err = str(e.value)
    assert err = "Please enter the task's list number (non-zero and non-negative integer)."

"""
Check mark_task_complete raises the exception "Please enter the task's list number (non-zero and non-negative integer)." if given -1
"""
def test_mark_test_complete_0():
    tm = TaskMaster()
    with pytest.raises(Exception) as e:
        tm.mark_task_complete(-1)
    err = str(e.value)
    assert err = "Please enter the task's list number (non-zero or negative)."

```
