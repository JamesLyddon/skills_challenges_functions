class TaskMaster:
    def __init__(self):
        self._tasks = []

    def add_task(self, text):
        if type(text) != str or text == "":
            raise Exception("Task must be a non-empty string.")
        self._tasks.append(text)
    
    def list_tasks(self):
        if len(self._tasks) == 0:
            raise Exception("No tasks to do!")
        print("[---TODO---]")
        for idx, item in enumerate(self._tasks):
            print(f"{idx + 1}: {item}")

    def mark_task_complete(self, number):
        if number > len(self._tasks):
            raise Exception("Task does not exist.")
        if number < 1 or type(number) != int or self._tasks == []:
            raise Exception("Please enter the task's list number (non-zero and non-negative integer).")
        self._tasks.pop(number - 1)
        if len(self._tasks) >= 1:
            self.list_tasks()
        else:
            print("All tasks complete!")