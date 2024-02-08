class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todos.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return [todo for todo in self.todos if not todo.complete]

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return [todo for todo in self.todos if todo.complete]

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self.todos: todo.mark_complete()