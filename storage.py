import json
from dataclasses import asdict

from models import Task


def save_tasks(tasks: list[Task], filename: str = "tasks.json") -> None:
    data: list[dict[str, int | str | bool]] = [asdict(task) for task in tasks]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_tasks(filename: str = "tasks.json") -> list[Task]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data: list[dict[str, int | str | bool]] = json.load(f)
        return [Task.from_dict(item) for item in data]
    except FileNotFoundError:
        return []
