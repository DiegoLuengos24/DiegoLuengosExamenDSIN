class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task:
            self.tasks.append(task)
            return True
        return False

    def get_tasks(self):
        return self.tasks