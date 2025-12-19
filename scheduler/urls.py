from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Основные алгоритмы
    path('priority/', views.run_priority, name='priority'),
    path('round-robin/', views.run_round_robin, name='round_robin'),
    path('heap-sort/', views.run_heap_sort, name='heap_sort'),
    path('quick-sort/', views.run_quick_sort, name='quick_sort'),
    path('sorting/', views.run_sorting, name='sorting'),

    # Деревья
    path('avl/', views.run_avl, name='avl'),
    path('bst/', views.run_bst, name='bst'),

    # Планирование
    path('greedy/', views.run_greedy, name='greedy'),
    path('dp-scheduler/', views.run_dp_scheduler, name='dp_scheduler'),

    # Структуры данных
    path('queue/', views.run_queue, name='queue'),
    path('stack/', views.run_stack, name='stack'),
    path('hash-table/', views.run_hash_table, name='hash_table'),

    # Поиск
    path('searching/', views.run_searching, name='searching'),
]
