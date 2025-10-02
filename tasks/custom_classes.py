from enum import Enum
from typing import List, Tuple

class TaskStatus(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELLED = 4

    @staticmethod
    def get_status_choices() -> List[Tuple[int, str]]:
        """
        Devuelve una lista con los pares (value, name) de los estados.
        """
        return [(status.value, status.name) for status in TaskStatus]


class TaskPriority(Enum):
    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4

    @staticmethod
    def get_priority_choices() -> List[Tuple[int, str]]:
        """
        Devuelve una lista con los pares (value, name) de las prioridades
        """
        return [(priority.value, priority.name) for priority in TaskPriority]