def greedy_next_task(tasks):
    best = None
    for task in tasks:
        if not best or task.priority > best.priority:
            best = task
    return best
