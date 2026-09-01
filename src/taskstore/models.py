"""Core domain models for taskflow."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


@dataclass
class Task:
    id: int
    title: str
    status: TaskStatus = TaskStatus.TODO
    tags: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)

    def mark_done(self) -> None:
        self.status = TaskStatus.DONE

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status.value,
            "tags": self.tags,
            "created_at": self.created_at.isoformat(),
        }
