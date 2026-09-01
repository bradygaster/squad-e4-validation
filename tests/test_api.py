import json

from api import TaskAPI
from taskstore import TaskStore


def make_api() -> TaskAPI:
    return TaskAPI(TaskStore())


def test_create_returns_201():
    api = make_api()
    response = api.create(json.dumps({"title": "hello"}))
    assert response["status"] == 201
    assert response["body"]["title"] == "hello"


def test_get_missing_returns_404():
    api = make_api()
    assert api.get(42)["status"] == 404


def test_complete_marks_done():
    api = make_api()
    created = api.create(json.dumps({"title": "x"}))
    task_id = created["body"]["id"]
    assert api.complete(task_id)["body"]["status"] == "done"
