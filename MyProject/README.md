# My Task Manager

<p align="center">
  A lightweight Python task manager with both a CLI interface and a FastAPI backend.
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.13-blue">
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-API-009688">
  <img alt="Storage" src="https://img.shields.io/badge/Storage-JSON-orange">
  <img alt="Status" src="https://img.shields.io/badge/Status-Educational-lightgrey">
</p>

## Overview

My Task Manager is a small educational project written in Python. It lets you manage tasks in two ways:

- through a simple command-line interface
- through a REST API built with FastAPI

Both interfaces use the same task management logic and store data in `tasks.json`.

## Highlights

- create, list, complete, and delete tasks
- use the project either from the terminal or via HTTP
- keep task data between restarts
- simple file-based persistence with no database setup

## Tech Stack

- Python 3.13
- FastAPI
- Pydantic
- Uvicorn
- JSON file storage

## Project Layout

```text
.
|-- api.py             FastAPI application
|-- main.py            CLI entry point
|-- manager.py         core task logic
|-- models.py          Task dataclass
|-- schemas.py         API schemas
|-- storage.py         JSON load/save helpers
|-- tasks.json         local data storage
|-- requirements.txt   project dependencies
```

## How It Works

The project is split into small focused modules:

- `models.py` defines the `Task` data model
- `manager.py` contains `TaskManager`, which handles all task operations
- `storage.py` reads from and writes to `tasks.json`
- `main.py` provides the terminal interface
- `api.py` exposes the same functionality through HTTP endpoints

This keeps the business logic shared between the CLI and the API instead of duplicating it.

## Quick Start

### 1. Create a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Run the application

For the CLI:

```powershell
python main.py
```

For the API:

```powershell
uvicorn api:app --reload
```

## CLI Menu

When you run `main.py`, the application shows a menu with these actions:

- `1` Add task
- `2` Show tasks
- `3` Complete task
- `4` Delete task
- `5` Exit

## API Usage

Once the server is running, open:

- App: `http://127.0.0.1:8000`
- Swagger docs: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Check that the application is running |
| `GET` | `/tasks` | Get all tasks |
| `GET` | `/tasks/{task_id}` | Get one task by ID |
| `POST` | `/tasks` | Create a new task |
| `PATCH` | `/tasks/{task_id}/complete` | Mark a task as completed |
| `DELETE` | `/tasks/{task_id}` | Delete a task |

### Example: Create a Task

```json
{
  "title": "Write README",
  "description": "Describe project structure and launch steps"
}
```

### Example Response

```json
{
  "id": 3,
  "title": "Write README",
  "description": "Describe project structure and launch steps",
  "is_done": false
}
```

## Data Format

Tasks are stored in `tasks.json` as plain JSON objects:

```json
[
  {
    "id": 1,
    "title": "Task title",
    "description": "Task description",
    "is_done": false
  }
]
```

## Current Limitations

- data is stored in a single local JSON file
- no database or migrations
- no authentication
- no automated tests
- concurrent writes from CLI and API may conflict

## Future Improvements

- add automated tests
- add update/edit task support
- improve validation and error handling
- move to SQLite or PostgreSQL
- add Docker support
- add filtering and search

## Example Workflow

1. Start the API with `uvicorn api:app --reload`
2. Open `http://127.0.0.1:8000/docs`
3. Create a task with `POST /tasks`
4. View tasks with `GET /tasks`
5. Complete a task with `PATCH /tasks/{task_id}/complete`

## Author

**Ceremont**
