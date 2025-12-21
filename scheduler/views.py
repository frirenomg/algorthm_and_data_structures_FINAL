from django.http import JsonResponse
from django.shortcuts import render
from .models import Task

# Импортируем модули алгоритмов целиком
from .algorithms import (
    avl,
    bst,
    dijkstra,
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
    stack,
    graph
)


def index(request):
    tasks = Task.objects.all()
    return render(request, 'scheduler/index.html', {'tasks': tasks})


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


# ---------- DIJKSTRA ----------
def run_dijkstra(request):
    tasks = list(Task.objects.all())
    graph_dict = {task.name: [] for task in tasks}
    for i, task in enumerate(tasks):
        for j in range(i + 1, len(tasks)):
            next_task = tasks[j]
            graph_dict[task.name].append((next_task.name, next_task.priority))
    start_task = tasks[0].name if tasks else None
    if not start_task:
        return JsonResponse({"dijkstra": {}})
    # вызываем функцию через модуль
    distances = dijkstra.dijkstra(graph_dict, start_task)
    return JsonResponse({"dijkstra": distances})


# ---------- TASK GRAPH ----------
def run_graph(request):
    tasks = list(Task.objects.all())
    g = graph.TaskGraph()
    for task in tasks:
        g.add_task(task.id)
    for i in range(1, len(tasks)):
        g.add_dependency(tasks[i].id, tasks[i - 1].id)
    start_task = tasks[0].id if tasks else None
    if not start_task:
        return JsonResponse({"graph_dfs": [], "graph_bfs": []})
    dfs_result = g.dfs(start_task)
    bfs_result = g.bfs(start_task)
    return JsonResponse({"graph_dfs": list(dfs_result), "graph_bfs": list(bfs_result)})


# ---------- DP SCHEDULER ----------
def run_dp_scheduler(request):
    tasks = list(Task.objects.all())
    result = dp_scheduler.schedule_dp(tasks, max_time=10)
    return JsonResponse({"dp_scheduler": result})


# ---------- GREEDY ----------
def run_greedy(request):
    tasks = list(Task.objects.filter(status='waiting'))
    task = greedy.greedy_next_task(tasks)
    return JsonResponse({"greedy": task.name if task else None})


# ---------- HASH TABLE ----------
def run_hash_table(request):
    table = hash_table.TaskHashTable()
    tasks = list(Task.objects.all())
    for task in tasks:
        table.insert(task.name, task)
    return JsonResponse({"hash_table": list(table.keys())})


# ---------- HEAP SORT ----------
def run_heap_sort(request):
    tasks = list(Task.objects.all())
    sorted_tasks = heap_sort.heap_sort_tasks(tasks)
    return JsonResponse({"heap_sort": [t.name for t in sorted_tasks]})


# ---------- LINKED LIST ----------
def run_linked_list(request):
    tasks = list(Task.objects.all())
    ll = linked_list.SinglyLinkedList()
    for task in tasks:
        ll.add(task.name)
    return JsonResponse({"linked_list": ll.to_list()})


# ---------- PRIORITY QUEUE ----------
def run_priority_queue(request):
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


# ---------- QUEUES ----------
def run_queues(request):
    q = queues.TaskQueue()
    tasks = list(Task.objects.all())
    for task in tasks:
        q.add_task(task)
    result = []
    while not q.is_empty():
        task = q.get_next()
        if task:
            result.append(task.name)
    return JsonResponse({"queues": result})


# ---------- QUICK SORT ----------
def run_quick_sort(request):
    tasks = list(Task.objects.all())
    sorted_tasks = quick_sort.quick_sort(tasks)
    return JsonResponse({"quick_sort": [t.name for t in sorted_tasks]})


# ---------- ROUND ROBIN ----------
def run_round_robin(request):
    scheduler = round_robin.RoundRobinScheduler(quantum=3)
    tasks = Task.objects.filter(status='waiting')
    for task in tasks:
        scheduler.add_task(task)
    result = scheduler.run()
    return JsonResponse({"round_robin": result})


# ---------- SEARCHING ----------
def run_searching(request):
    tasks = list(Task.objects.all())
    # вызываем через модуль, если функция есть
    found = getattr(searching, "find_max_priority", lambda x: None)(tasks)
    return JsonResponse({"searching": found.name if found else None})


# ---------- SORTING ----------
def run_sorting(request):
    tasks = list(Task.objects.all())
    sorted_tasks = sorting.sort_by_priority(tasks)
    return JsonResponse({"sorting": [t.name for t in sorted_tasks]})


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