class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        #   Returns err-msg if task is not a non-empty string
        if type(task) != str or task == "":
            raise Exception("Task must be a non-empty string.")
        self.task = task
        self.complete = False

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        self.complete = True
