from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

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

# ---------- TASK LIST + ADD ----------
def index(request):
    tasks = Task.objects.all()

    # Форма добавления новой задачи
    if request.method == 'POST' and 'add_task' in request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()

    return render(request, 'scheduler/index.html', {'tasks': tasks, 'form': form})

# ---------- EDIT TASK ----------
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'scheduler/edit_task.html', {'form': form, 'task': task})

def reset_all_tasks(request):
    Task.objects.all().update(status='waiting')
    return redirect('index')

# ---------- DELETE TASK ----------
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('index')

# ---------- ALGORITHMS ----------
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
    distances = dijkstra.dijkstra(graph_dict, start_task)
    return JsonResponse({"dijkstra": distances})

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

def run_dp_scheduler(request):
    tasks = list(Task.objects.all())
    result = dp_scheduler.schedule_dp(tasks, max_time=10)
    return JsonResponse({"dp_scheduler": result})

def run_greedy(request):
    tasks = list(Task.objects.filter(status='waiting'))
    task = greedy.greedy_next_task(tasks)
    return JsonResponse({"greedy": task.name if task else None})

def run_hash_table(request):
    table = hash_table.TaskHashTable()
    tasks = list(Task.objects.all())
    for task in tasks:
        table.insert(task.name, task)
    return JsonResponse({"hash_table": list(table.keys())})

def run_heap_sort(request):
    tasks = list(Task.objects.all())
    sorted_tasks = heap_sort.heap_sort_tasks(tasks)
    return JsonResponse({"heap_sort": [t.name for t in sorted_tasks]})

def run_linked_list(request):
    tasks = list(Task.objects.all())
    ll = linked_list.SinglyLinkedList()
    for task in tasks:
        ll.add(task.name)
    return JsonResponse({"linked_list": ll.to_list()})

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

def run_quick_sort(request):
    tasks = list(Task.objects.all())
    sorted_tasks = quick_sort.quick_sort(tasks)
    return JsonResponse({"quick_sort": [t.name for t in sorted_tasks]})

def run_round_robin(request):
    scheduler = round_robin.RoundRobinScheduler(quantum=3)
    tasks = Task.objects.filter(status='waiting')
    for task in tasks:
        scheduler.add_task(task)
    result = scheduler.run()
    return JsonResponse({"round_robin": result})

def run_searching(request):
    tasks = list(Task.objects.all())
    found = getattr(searching, "find_max_priority", lambda x: None)(tasks)
    return JsonResponse({"searching": found.name if found else None})

def run_sorting(request):
    tasks = list(Task.objects.all())
    sorted_tasks = sorting.sort_by_priority(tasks)
    return JsonResponse({"sorting": [t.name for t in sorted_tasks]})

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