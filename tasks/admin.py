from django.contrib import admin
from .models import Priority, Task, Status

admin.site.register(Task)
admin.site.register(Priority)
admin.site.register(Status)
