from task_manager.repository import Repository
from task_manager.tasks import Task


class InMemoryRepository(Repository):
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}

    def empty(self) -> bool:
        return bool(self._tasks) is False

    def load_tasks(self, tasks: list[Task]) -> None:
        for task in tasks:
            self._tasks[task.id] = task

    def tasks(self) -> list[Task]:
        return list(self._tasks.values())

    def add_task(self, description: str) -> None:
        max_id = max(self._tasks.keys(), default=0)
        new_task = Task(id=max_id + 1, description=description, done=False)
        self._tasks[new_task.id] = new_task

    def update_task_status(self, id: int, done: bool) -> None:
        matching_task = self._tasks[id]
        matching_task.done = done

    def remove_task(self, id: int) -> None:
        del self._tasks[id]

    def reset(self) -> None:
        self._tasks = {}
