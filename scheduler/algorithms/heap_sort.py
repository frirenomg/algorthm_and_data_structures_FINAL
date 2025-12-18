import heapq
from itertools import count

def heap_sort_tasks(tasks):
    """
    Сортировка задач по приоритету (heap sort)
    """
    counter = count()
    heap = [(-task.priority, next(counter), task) for task in tasks]
    heapq.heapify(heap)
    sorted_tasks = []
    while heap:
        sorted_tasks.append(heapq.heappop(heap)[2])
    return sorted_tasks
