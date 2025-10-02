from django.urls import path
from . import views

urlpatterns = [
    path("", views.TaskList.as_view(), name="list"),
    path("new_task", views.CreateTask.as_view(), name="create"),
]
