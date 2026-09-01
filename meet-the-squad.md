# Meet Your Squad

**Naming mode:** Descriptive

## The Team

| Name | Role | Specialty | How to talk to them |
|------|------|-----------|----------------------|
| Lead | Lead | Architecture & task breakdown across store/API/CLI | Assign an issue with label `squad:lead` |
| Backend | Backend Engineer | `TaskStore`, `TaskAPI`, CLI implementation & bug fixes | Assign an issue with label `squad:backend` |
| Tester | Test Engineer | pytest coverage for store & API edge cases | Assign an issue with label `squad:tester` |
| Security | Security Engineer | Auth, input validation, rate limiting | Assign an issue with label `squad:security` |
| Docs | DevRel/Docs | README & architecture docs upkeep | Assign an issue with label `squad:docs` |

## How to Work With Your Squad

- Assign an issue by adding a `squad:{name}` label (color `9B8FCC`) matching the specialist you want, e.g. `squad:backend`.
- Iterate on planning with `/squad research`, `/squad plan`, `/squad triage`, and `/squad implement` comment commands.
- See `.squad/routing.md` for the full work-type → specialist routing table.

## What Happened Here

taskflow is a small Python task-tracking service with three layers: an in-memory `TaskStore` and `Task`/`TaskStatus` models, an HTTP `TaskAPI` handler layer, and a thin CLI entry point. Tests use pytest against `src/`. There is no CI/CD configured, no persistence, and no auth — `docs/architecture.md` lists several concrete known gaps (silent delete of unknown ids, uncaught `TaskNotFound` in `complete`, missing input validation on `create`, no auth/rate limiting).

Given the small, single-package layout and the concrete list of known gaps, the team is sized at 5: a Lead for architecture/prioritization, a Backend Engineer to own the store/API/CLI fixes, a Test Engineer to cover the edge cases before/after fixes land, a Security Engineer to address the auth/validation gaps, and Docs to keep `README.md`/`docs/architecture.md` in sync as gaps close. Descriptive naming was used since no themed universe was requested.

---
*Cast on 2026-09-01*
