from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField()
    execution_time = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('waiting', 'Waiting'),
            ('running', 'Running'),
            ('finished', 'Finished')
        ],
        default='waiting'
    )

    def __str__(self):
        return f"{self.name} (priority={self.priority})"
