from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import *


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = TasksSerializer

    def get_queryset(self):
        activeStatus = TasksStatus.objects.get(description="Active")
        return Tasks.objects.filter(status=activeStatus)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        status = TasksStatus.objects.get(description="Active")
        serializer.save(user=1, status=status)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        newStatus = TasksStatus.objects.get(description__icontains="inactive")
        instance = self.get_object()
        instance.status = newStatus
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
