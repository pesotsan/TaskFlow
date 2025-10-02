from django.db import models
from typing import List, Tuple
from enum import Enum


class Classification(Enum):
    ACTIVE = 1
    FINISHED = 2
    CANCELLED =3

    @staticmethod
    def get_choices() -> List[Tuple[int, str]]:
        return [(classif.value, classif.name) for classif in Classification]


class Status(models.Model):
    title = models.CharField(max_length=15)
    classification = models.PositiveSmallIntegerField(choices=Classification.get_choices)
    flow_order = models.IntegerField()
    is_editable = models.BooleanField()
    color = models.IntegerField()

    def __str__(self) -> str:
        return self.title


class Priority(models.Model):
    title = models.CharField(max_length=15)
    level = models.PositiveSmallIntegerField()
    color = models.IntegerField()
    description = models.CharField(max_length=75)

    def __str__(self) -> str:
        return self.title


class Task(models.Model):
    
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    creation_date = models.DateField(auto_now=True)
    deadline_date = models.DateField()
    completed_date = models.DateField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title



    



