"""HTTP-ish handlers for the task API.

Error handling is inconsistent here: some paths return an error dict,
others let the underlying exception propagate.
"""

from __future__ import annotations

import json

from taskstore import TaskStatus, TaskStore
from taskstore.store import TaskNotFound


class TaskAPI:
    def __init__(self, store: TaskStore) -> None:
        self.store = store

    def create(self, body: str) -> dict:
        payload = json.loads(body)
        title = payload["title"]
        task = self.store.add(title, payload.get("tags"))
        return {"status": 201, "body": task.to_dict()}

    def get(self, task_id: int) -> dict:
        try:
            task = self.store.get(task_id)
        except TaskNotFound:
            return {"status": 404, "body": {"error": "not found"}}
        return {"status": 200, "body": task.to_dict()}

    def list(self, status: str | None = None) -> dict:
        parsed = TaskStatus(status) if status else None
        tasks = self.store.list(parsed)
        return {"status": 200, "body": [t.to_dict() for t in tasks]}

    def complete(self, task_id: int) -> dict:
        task = self.store.complete(task_id)
        return {"status": 200, "body": task.to_dict()}

    def delete(self, task_id: int) -> dict:
        self.store.delete(task_id)
        return {"status": 204, "body": None}
