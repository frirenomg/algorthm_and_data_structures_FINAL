import heapq
from itertools import count

class PriorityTaskQueue:
    def __init__(self):
        self.heap = []
        self.counter = count()  # Чтобы избежать ошибок сравнения объектов

    def add_task(self, task):
        heapq.heappush(self.heap, (-task.priority, next(self.counter), task))

    def get_next(self):
        if self.heap:
            return heapq.heappop(self.heap)[2]
        return None
