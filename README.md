# taskflow

A small task-tracking service written in Python. Provides an in-memory task
store, a thin HTTP API layer, and a CLI entry point.

## Layout

- `src/taskstore/` — core domain model and storage
- `src/api/` — HTTP handlers
- `tests/` — unit tests (pytest)

## Running tests

```bash
python -m pytest tests/ -q
```

## Status

Early. Storage is in-memory only; there is no persistence, no auth, and
error handling is inconsistent across the API layer.
