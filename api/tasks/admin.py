from django.contrib import admin
from .models import *


@admin.register(Tasks)
class HikeAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "status"]


@admin.register(TasksStatus)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ["description"]
