import json
from pathlib import Path
from typing import Any

from task_manager.repositories.in_memory import InMemoryRepository
from task_manager.tasks import Task


def serialize(task: Task) -> dict[str, Any]:
    return {"id": task.id, "description": task.description, "done": task.done}


def deserialize(d: dict[str, Any]) -> Task:
    return Task(id=d["id"], description=d["description"], done=d["done"])


class JsonDB(InMemoryRepository):
    def __init__(self, json_path: Path) -> None:
        super().__init__()
        self.json_path = json_path
        self.load()

    def load(self) -> None:
        if self.json_path.exists():
            with self.json_path.open("r") as f:
                serialized = json.load(f)
            tasks = [deserialize(d) for d in serialized]
            self.load_tasks(tasks)

    def save(self) -> None:
        serialized = [serialize(t) for t in self.tasks()]
        with self.json_path.open("w") as f:
            json.dump(serialized, f, indent=2)

    def add_task(self, description: str) -> None:
        super().add_task(description)
        self.save()

    def update_task_status(self, id: int, done: bool) -> None:
        super().update_task_status(id, done)
        self.save()

    def remove_task(self, id: int) -> None:
        super().remove_task(id)
        self.save()
