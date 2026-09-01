"""Minimal CLI entry point for taskflow."""

from __future__ import annotations

import sys

from taskstore import TaskStore


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    store = TaskStore()

    if not argv:
        print("usage: taskflow <add|list> [args]")
        return 1

    command = argv[0]
    if command == "add":
        task = store.add(" ".join(argv[1:]))
        print(f"created task {task.id}: {task.title}")
        return 0
    if command == "list":
        for task in store.list():
            print(f"{task.id}\t{task.status.value}\t{task.title}")
        return 0

    print(f"unknown command: {command}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
