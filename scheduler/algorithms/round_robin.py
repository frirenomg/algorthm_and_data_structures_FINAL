class RoundRobinScheduler:
    def __init__(self, quantum):
        self.quantum = quantum
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({
            "task": task,
            "remaining": task.execution_time
        })

    def run(self):
        order = []
        queue = self.tasks.copy()

        while queue:
            current = queue.pop(0)
            task = current["task"]

            time_slice = min(self.quantum, current["remaining"])
            current["remaining"] -= time_slice

            order.append(task.name)

            if current["remaining"] > 0:
                queue.append(current)
            else:
                task.status = 'finished'
                task.save()

        return order