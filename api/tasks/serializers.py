from rest_framework import serializers
from .models import Tasks, TasksStatus


class TasksStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksStatus
        fields = "__all__"


class TasksSerializer(serializers.ModelSerializer):
    status = TasksStatusSerializer(required=False)
    user = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tasks
        fields = ["id", "name", "description", "status", "user"]
