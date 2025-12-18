from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority', 'execution_time', 'status')
    list_filter = ('status',)
