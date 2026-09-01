import pytest

from taskstore import TaskStatus, TaskStore
from taskstore.store import TaskNotFound


def test_add_assigns_incrementing_ids():
    store = TaskStore()
    first = store.add("write docs")
    second = store.add("fix bug")
    assert first.id == 1
    assert second.id == 2


def test_get_missing_raises():
    store = TaskStore()
    with pytest.raises(TaskNotFound):
        store.get(99)


def test_complete_sets_status():
    store = TaskStore()
    task = store.add("ship it")
    store.complete(task.id)
    assert store.get(task.id).status is TaskStatus.DONE


def test_list_filters_by_status():
    store = TaskStore()
    store.add("one")
    done = store.add("two")
    store.complete(done.id)
    assert len(store.list(TaskStatus.DONE)) == 1
