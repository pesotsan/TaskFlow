import datetime
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "deadline_date", "priority"]
        widgets = {
            "deadline_date": forms.DateInput(attrs={"type": "date"})
        }

    def clean_deadline_date(self):
        deadline = self.cleaned_data["deadline_date"]
        if deadline < datetime.date.today():
            raise forms.ValidationError("Invalid date. It is a past date.")
        return deadline
