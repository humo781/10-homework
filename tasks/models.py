from django.db import models
from django.urls import reverse
from django.utils import timezone


class Task(models.Model):
    task_title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(default=timezone.now)

    def get_detail_url(self):
        return reverse('tasks:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('tasks:update', args=[self.pk])
