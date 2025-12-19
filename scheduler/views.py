from django.http import JsonResponse
from django.shortcuts import render
from .models import Task

# Импортируем алгоритмы
from .algorithms import (
    avl,
    bst,
    dp_scheduler,
    greedy,
    hash_table,
    heap_sort,
    linked_list,
    priority_queue,
    queues,
    quick_sort,
    round_robin,
    searching,
    sorting,
    stack
)

def index(request):
    tasks = Task.objects.all()
    return render(request, 'scheduler/index.html', {'tasks': tasks})


# ---------- PRIORITY QUEUE ----------
def run_priority(request):
    pq = priority_queue.PriorityTaskQueue()
    tasks = Task.objects.filter(status='waiting')

    for task in tasks:
        pq.add_task(task)

    result = []
    while not pq.is_empty():
        task = pq.get_next()
        if task:
            result.append(task.name)

    return JsonResponse({"priority_queue": result})


# ---------- ROUND ROBIN ----------
def run_round_robin(request):
    scheduler = round_robin.RoundRobinScheduler(quantum=3)
    tasks = Task.objects.filter(status='waiting')

    for task in tasks:
        scheduler.add_task(task)

    result = scheduler.run()
    return JsonResponse({"round_robin": result})


# ---------- HEAP SORT ----------
def run_heap_sort(request):
    tasks = list(Task.objects.all())
    sorted_tasks = heap_sort.heap_sort_tasks(tasks)
    return JsonResponse({"heap_sort": [t.name for t in sorted_tasks]})


# ---------- QUICK SORT ----------
def run_quick_sort(request):
    tasks = list(Task.objects.all())
    sorted_tasks = quick_sort.quick_sort(tasks)
    return JsonResponse({"quick_sort": [t.name for t in sorted_tasks]})


# ---------- SORTING ----------
def run_sorting(request):
    tasks = list(Task.objects.all())
    sorted_tasks = sorting.sort_by_priority(tasks)
    return JsonResponse({"sorting": [t.name for t in sorted_tasks]})


# ---------- AVL TREE ----------
def run_avl(request):
    tasks = list(Task.objects.all())
    root = None

    for task in tasks:
        root = avl.insert(root, task.priority, task)

    result = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.task.name)
        inorder(node.right)

    inorder(root)
    return JsonResponse({"avl": result})


# ---------- BST ----------
def run_bst(request):
    tasks = list(Task.objects.all())
    tree = bst.BST()
    root = None

    for task in tasks:
        root = tree.insert(root, task.priority, task)

    result = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.task.name)
        inorder(node.right)

    inorder(root)
    return JsonResponse({"bst": result})


# ---------- GREEDY ----------
def run_greedy(request):
    tasks = list(Task.objects.filter(status='waiting'))
    task = greedy.greedy_next_task(tasks)
    return JsonResponse({"greedy": task.name if task else None})


# ---------- DP SCHEDULER ----------
def run_dp_scheduler(request):
    tasks = list(Task.objects.all())
    result = dp_scheduler.schedule_dp(tasks, max_time=10)
    return JsonResponse({"dp_scheduler": result})


# ---------- QUEUE ----------
def run_queue(request):
    q = queues.TaskQueue()
    tasks = list(Task.objects.all())

    for task in tasks:
        q.add_task(task)

    result = []
    while not q.is_empty():
        task = q.get_next()
        if task:
            result.append(task.name)

    return JsonResponse({"queue": result})


# ---------- STACK ----------
def run_stack(request):
    s = stack.Stack()
    tasks = list(Task.objects.all())

    for task in tasks:
        s.push(task)

    result = []
    while not s.is_empty():
        task = s.pop()
        if task:
            result.append(task.name)

    return JsonResponse({"stack": result})


# ---------- SEARCHING ----------
def run_searching(request):
    tasks = list(Task.objects.all())
    found = searching.find_max_priority(tasks)
    return JsonResponse({"searching": found.name if found else None})


# ---------- HASH TABLE ----------
def run_hash_table(request):
    table = hash_table.TaskHashTable()
    tasks = list(Task.objects.all())

    for task in tasks:
        table.insert(task.name, task)

    return JsonResponse({"hash_table": list(table.keys())})