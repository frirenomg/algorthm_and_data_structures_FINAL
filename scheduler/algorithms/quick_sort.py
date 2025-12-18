def quick_sort(tasks):
    if len(tasks) <= 1:
        return tasks
    pivot = tasks[len(tasks)//2].priority
    left = [t for t in tasks if t.priority < pivot]
    mid = [t for t in tasks if t.priority == pivot]
    right = [t for t in tasks if t.priority > pivot]
    return quick_sort(left) + mid + quick_sort(right)
