from fastapi import FastAPI, HTTPException

from manager import TaskManager
from models import Task
from schemas import TaskCreate, TaskResponse
from storage import load_tasks, save_tasks

app = FastAPI(title="My Task Manager")
manager = TaskManager()
manager.load_tasks(load_tasks())


def task_to_response(task: Task) -> TaskResponse:
    return TaskResponse(
        id=task.id,
        title=task.title,
        description=task.description,
        is_done=task.is_done,
    )


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Welcome to the My Task Manager!"}


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks() -> list[TaskResponse]:
    tasks: list[Task] = manager.show_tasks()
    return [task_to_response(task) for task in tasks]


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int) -> TaskResponse:
    task: Task | None = manager.get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_to_response(task)


@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate) -> TaskResponse:
    if not task.title.strip() or not task.description.strip():
        raise HTTPException(status_code=400, detail="Task title or description is required")

    new_task: Task = manager.add_task(task.title, task.description)
    save_tasks(manager.show_tasks())
    return task_to_response(new_task)


@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int) -> dict[str, str]:
    success: bool = manager.complete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")

    save_tasks(manager.show_tasks())
    return {"message": "Task completed"}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> dict[str, str]:
    success: bool = manager.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")

    save_tasks(manager.show_tasks())
    return {"message": "Task deleted"}
