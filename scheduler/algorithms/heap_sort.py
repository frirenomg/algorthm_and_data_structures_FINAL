import heapq
from itertools import count

def heap_sort_tasks(tasks):
    """
    Heap Sort для задач.
    Сортировка по priority (по убыванию).
    Используется counter для стабильности.
    """
    counter = count()

    # Формируем кучу: мин-куча с отрицательным приоритетом для сортировки по убыванию
    heap = [(-task.priority, next(counter), task) for task in tasks]
    heapq.heapify(heap)

    sorted_tasks = []
    while heap:
        sorted_tasks.append(heapq.heappop(heap)[2])

    return sorted_tasks
