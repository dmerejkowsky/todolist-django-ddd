from task_manager.repository import Repository as BaseRepository
from task_manager.tasks import Task

from .models import Task as TaskModel


class Repository(BaseRepository):
    def add_task(self, description: str) -> None:
        TaskModel.objects.create(description=description, done=False)

    def update_task_status(self, id: int, done: bool) -> None:
        task = TaskModel.objects.get(id=id)
        task.done = done
        task.save()

    def remove_task(self, id: int) -> None:
        pass

    def tasks(self) -> list[Task]:
        pass
