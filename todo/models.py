from django.db import models

class List(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=255, unique=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    description = models.TextField(null=False, blank=False)
    deadline = models.DateTimeField(null=False, blank=False)
    order = models.IntegerField(null=False, blank=False)
    is_starred = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['list', 'order'], name='unique_task_order_within_list')
        ]
