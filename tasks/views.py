#from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .forms import TaskForm
from .models import Task, Priority, Status

class TaskList(ListView):
    model = Task
    paginate_by = 10
    template_name = "tasks/task_list.html"
    ordering = ["priority__level", "deadline_date"]


class CreateTask(CreateView):
    model = Task
    template_name = "tasks/new_task.html"
    form_class = TaskForm
    success_url = reverse_lazy("create")

    def form_valid(self, form):
        messages.success(self.request, "Task created")
        return super().form_valid(form)