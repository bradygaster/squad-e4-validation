# Architecture

taskflow has three layers:

1. **Models** (`src/taskstore/models.py`) — `Task` dataclass and `TaskStatus` enum.
2. **Store** (`src/taskstore/store.py`) — in-memory dict keyed by task id.
3. **API** (`src/api/handlers.py`) — request handlers returning status/body dicts.

## Known gaps

- No persistence. The store is a plain dict.
- `TaskStore.delete` silently succeeds for unknown ids, while `get` raises.
- `TaskAPI.complete` does not catch `TaskNotFound`, so it propagates.
- No input validation on `create` — a missing `title` raises `KeyError`.
- No auth or rate limiting.
