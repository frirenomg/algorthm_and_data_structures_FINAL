# fill_db.py
import os
import django

# Настройка Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from scheduler.models import Task

# Список тестовых задач
tasks = [
    {"name": "Task1", "priority": 5, "execution_time": 4},
    {"name": "Task2", "priority": 3, "execution_time": 2},
    {"name": "Task3", "priority": 7, "execution_time": 3},
    {"name": "Task4", "priority": 2, "execution_time": 1},
    {"name": "Task5", "priority": 6, "execution_time": 5},
]

# Создание задач в базе
for t in tasks:
    Task.objects.create(
        name=t["name"],
        priority=t["priority"],
        execution_time=t["execution_time"]
    )

print(f"{len(tasks)} test tasks created successfully!")
