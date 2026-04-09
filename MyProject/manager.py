from models import Task

class TaskManager:
    def __init__(self) -> None:
        self.tasks: list[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: str) -> Task:
        task: Task = Task(
            id=self.next_id,
            title=title,
            description=description,
        )
        self.tasks.append(task)
        self.next_id += 1
        return task

    def show_tasks(self) -> list[Task]:
        return self.tasks.copy()

    def get_task_by_id(self, task_id: int) -> Task | None:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def complete_task(self, task_id: int) -> bool:
        task: Task | None = self.get_task_by_id(task_id)
        if task is None:
            return False
        task.is_done = True
        return True

    def delete_task(self, task_id: int) -> bool:
        task: Task | None = self.get_task_by_id(task_id)
        if task is None:
            return False
        self.tasks.remove(task)
        return True

    def load_tasks(self, tasks: list[Task]) -> None:
        self.tasks = tasks
        if self.tasks:
            self.next_id = max(task.id for task in self.tasks) + 1
        else:
            self.next_id = 1
