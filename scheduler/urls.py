from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Алгоритмы
    path('priority/', views.run_priority, name='priority'),
    path('round-robin/', views.run_round_robin, name='round_robin'),
    path('heap-sort/', views.run_heap_sort, name='heap_sort'),
    path('quick-sort/', views.run_quick_sort, name='quick_sort'),
    path('sorting/', views.run_sorting, name='sorting'),
    path('greedy/', views.run_greedy, name='greedy'),
    path('avl/', views.run_avl, name='avl'),
    path('bst/', views.run_bst, name='bst'),
    path('dp-scheduler/', views.run_dp_scheduler, name='dp_scheduler'),
    path('queue/', views.run_queues, name='queue'),
    path('stack/', views.run_stack, name='stack'),

    # Если добавишь graph, dijkstra, linked_list, hash_table, searching, 
    # добавь их здесь аналогично
]
