import abc

from task_manager.tasks import Task


class Repository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_task(self, description: str) -> None:
        pass

    @abc.abstractmethod
    def update_task_status(self, id: int, done: bool) -> None:
        pass

    @abc.abstractmethod
    def remove_task(self, id: int) -> None:
        pass

    @abc.abstractmethod
    def tasks(self) -> list[Task]:
        pass

    @abc.abstractmethod
    def load_tasks(self, tasks: list[Task]) -> None:
        pass

    def empty(self) -> bool:
        return len(self.tasks()) == 0
