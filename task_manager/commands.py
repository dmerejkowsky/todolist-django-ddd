import abc

from task_manager.repository import Repository


class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self, repository: Repository) -> None:
        pass


class Add(Command):
    def __init__(self, description: str) -> None:
        self.description = description

    def execute(self, repository: Repository) -> None:
        repository.add_task(self.description)


class Check(Command):
    def __init__(self, id: int) -> None:
        self.id = id

    def execute(self, repository: Repository) -> None:
        repository.update_task_status(self.id, done=True)


class UnCheck(Command):
    def __init__(self, id: int) -> None:
        self.id = id

    def execute(self, repository: Repository) -> None:
        repository.update_task_status(self.id, done=False)


class Remove(Command):
    def __init__(self, id: int) -> None:
        self.id = id

    def execute(self, repository: Repository) -> None:
        repository.remove_task(self.id)
