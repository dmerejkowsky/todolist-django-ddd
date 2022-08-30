import abc

from task_manager.todo_list import TodoList


class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self, todo_list: TodoList) -> None:
        pass


class Add(Command):
    def __init__(self, description: str) -> None:
        self.description = description

    def execute(self, todo_list: TodoList) -> None:
        todo_list.add_task(self.description)


class Check(Command):
    def __init__(self, id: int) -> None:
        self.id = id

    def execute(self, todo_list: TodoList) -> None:
        todo_list.update_task_status(self.id, done=True)


class UnCheck(Command):
    def __init__(self, id: int) -> None:
        self.id = id

    def execute(self, todo_list: TodoList) -> None:
        todo_list.update_task_status(self.id, done=False)


class Remove(Command):
    def __init__(self, id: int) -> None:
        self.id = id

    def execute(self, todo_list: TodoList) -> None:
        todo_list.remove_task(self.id)
