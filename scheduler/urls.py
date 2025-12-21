from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # CRUD задачи
    path('task/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),

    # Алгоритмы
    path('avl/', views.run_avl, name='avl'),
    path('bst/', views.run_bst, name='bst'),
    path('dijkstra/', views.run_dijkstra, name='dijkstra'),
    path('dp-scheduler/', views.run_dp_scheduler, name='dp_scheduler'),
    path('graph/', views.run_graph, name='graph'),
    path('greedy/', views.run_greedy, name='greedy'),
    path('hash-table/', views.run_hash_table, name='hash_table'),
    path('heap-sort/', views.run_heap_sort, name='heap_sort'),
    path('linked-list/', views.run_linked_list, name='linked_list'),
    path('priority-queue/', views.run_priority_queue, name='priority_queue'),
    path('queues/', views.run_queues, name='queues'),
    path('quick-sort/', views.run_quick_sort, name='quick_sort'),
    path('round-robin/', views.run_round_robin, name='round_robin'),
    path('searching/', views.run_searching, name='searching'),
    path('sorting/', views.run_sorting, name='sorting'),
    path('stack/', views.run_stack, name='stack'),
    path('tasks/reset/', views.reset_all_tasks, name='reset_all_tasks'),
]