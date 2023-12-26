from django.urls import include, path
from rest_framework import routers
from .views import TasksViewSet

router = routers.DefaultRouter()
router.register(r"tasks", TasksViewSet, basename="tasks")

urlpatterns = [path("", include(router.urls))]
