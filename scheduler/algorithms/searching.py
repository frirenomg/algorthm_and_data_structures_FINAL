def linear_search(tasks, task_id):
    for task in tasks:
        if task.id == task_id:
            return task
    return None
