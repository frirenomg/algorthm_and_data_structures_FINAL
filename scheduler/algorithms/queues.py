class TaskQueue:
    def __init__(self):
        self.data = []

    def add_task(self, task):
        self.data.append(task)

    def get_next(self):
        if self.data:
            return self.data.pop(0)
        return None

    def is_empty(self):
        return len(self.data) == 0