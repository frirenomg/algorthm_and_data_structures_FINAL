import heapq
from itertools import count

def heap_sort_tasks(tasks):
    counter = count()

    heap = [(-task.priority, next(counter), task) for task in tasks]
    heapq.heapify(heap)

    sorted_tasks = []
    while heap:
        sorted_tasks.append(heapq.heappop(heap)[2])

    return sorted_tasks
