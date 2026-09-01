"""In-memory task storage.

There is no persistence layer yet. Everything is lost on restart.
"""

from __future__ import annotations

from .models import Task, TaskStatus


class TaskNotFound(Exception):
    pass


class TaskStore:
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def add(self, title: str, tags: list[str] | None = None) -> Task:
        task = Task(id=self._next_id, title=title, tags=tags or [])
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get(self, task_id: int) -> Task:
        if task_id not in self._tasks:
            raise TaskNotFound(f"no task with id {task_id}")
        return self._tasks[task_id]

    def list(self, status: TaskStatus | None = None) -> list[Task]:
        tasks = list(self._tasks.values())
        if status is not None:
            tasks = [t for t in tasks if t.status == status]
        return tasks

    def complete(self, task_id: int) -> Task:
        task = self.get(task_id)
        task.mark_done()
        return task

    def delete(self, task_id: int) -> None:
        # NOTE: silently succeeds when the task does not exist
        self._tasks.pop(task_id, None)
