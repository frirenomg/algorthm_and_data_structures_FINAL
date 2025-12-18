class RoundRobinScheduler:
    def __init__(self, quantum):
        self.quantum = quantum
        self.tasks = []

    def add_task(self, task):
        # Копируем execution_time, чтобы не менять оригинал в базе
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
            remaining = current["remaining"]

            # "выполняем" задачу на quantum
            time_slice = min(self.quantum, remaining)
            current["remaining"] -= time_slice

            # добавляем в порядок выполнения каждый раз, когда задача обрабатывается
            order.append(task.name)

            # если задача ещё не закончена, возвращаем её в конец очереди
            if current["remaining"] > 0:
                queue.append(current)
            else:
                # отмечаем задачу как выполненную
                task.status = 'finished'
                task.save()

        return order
