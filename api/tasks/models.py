from django.db import models

# from django.conf import settings

# User = settings.AUTH_USER_MODEL


class TasksStatus(models.Model):
    description = models.CharField(max_length=50, null=False)


class Tasks(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True)
    status = models.ForeignKey(TasksStatus, null=False, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    user = models.IntegerField(default=1, null=False)
