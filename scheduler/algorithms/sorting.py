def sort_by_priority(tasks):
    tasks = tasks.copy()
    for i in range(1, len(tasks)):
        key = tasks[i]
        j = i - 1
        while j >= 0 and tasks[j].priority > key.priority:
            tasks[j + 1] = tasks[j]
            j -= 1
        tasks[j + 1] = key
    return tasks
