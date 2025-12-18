from django.http import JsonResponse
from django.shortcuts import render
from .models import Task

# Импортируем модули алгоритмов
from .algorithms import (
    avl, bst, dijkstra, dp_scheduler, graph, greedy, hash_table,
    heap_sort, linked_list, priority_queue, queues, quick_sort,
    round_robin, searching, sorting, stack
)

def index(request):
    tasks = Task.objects.all()
    return render(request, 'scheduler/index.html', {'tasks': tasks})

def run_priority(request):
    pq = priority_queue.PriorityTaskQueue()
    tasks = Task.objects.filter(status='waiting')
    for task in tasks:
        pq.add_task(task)
    executed = []
    while True:
        task = pq.get_next()
        if not task:
            break
        task.status = 'finished'
        task.save()
        executed.append(task.name)
    return JsonResponse({"priority": executed})

def run_round_robin(request):
    scheduler = round_robin.RoundRobinScheduler(quantum=3)
    tasks = Task.objects.filter(status='waiting')
    for task in tasks:
        scheduler.add_task(task)
    result = scheduler.run()
    return JsonResponse({"round_robin": result})

def run_heap_sort(request):
    tasks = list(Task.objects.all())
    sorted_tasks = heap_sort.heap_sort_tasks(tasks)
    data = [t.name for t in sorted_tasks]
    return JsonResponse({"heap_sort": data})

def run_quick_sort(request):
    tasks = list(Task.objects.all())
    sorted_tasks = quick_sort.quick_sort(tasks)
    data = [t.name for t in sorted_tasks]
    return JsonResponse({"quick_sort": data})

def run_sorting(request):
    tasks = list(Task.objects.all())
    sorted_tasks = sorting.insertion_sort(tasks)  # пример сортировки из модуля sorting
    data = [t.name for t in sorted_tasks]
    return JsonResponse({"sorting": data})

# Остальные алгоритмы
def run_avl(request):
    tasks = list(Task.objects.all())
    root = None
    for task in tasks:
        root = avl.insert(root, task.priority, task)
    # in-order обход
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
    # in-order обход
    result = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.task.name)
        inorder(node.right)
    inorder(root)
    return JsonResponse({"bst": result})

def run_greedy(request):
    tasks = list(Task.objects.filter(status='waiting'))
    task = greedy.greedy_next_task(tasks)
    return JsonResponse({"greedy": task.name if task else None})

def run_dp_scheduler(request):
    tasks = list(Task.objects.all())
    result = dp_scheduler.schedule_dp(tasks, max_time=10)  # пример: max_time=10
    return JsonResponse({"dp_scheduler": result})

def run_queues(request):
    tq = queues.TaskQueue()
    tasks = list(Task.objects.all())
    for task in tasks:
        tq.add_task(task)
    result = []
    while not tq.is_empty():
        result.append(tq.get_next().name)
    return JsonResponse({"queue": result})

def run_stack(request):
    st = stack.Stack()
    tasks = list(Task.objects.all())
    for task in tasks:
        st.push(task)
    result = []
    while st.data:
        result.append(st.pop().name)
    return JsonResponse({"stack": result})

# Можно добавить ещё graph, dijkstra, linked_list, hash_table, searching по аналогии
