import heapq
from itertools import count

class PriorityTaskQueue:
    def __init__(self):
        self.heap = []
        self.counter = count()

    def add_task(self, task):
        # Используем отрицательный приоритет для max-heap
        heapq.heappush(self.heap, (-task.priority, next(self.counter), task))

    def get_next(self):
        if self.heap:
            return heapq.heappop(self.heap)[2]
        return None

    def is_empty(self):
        return len(self.heap) == 0