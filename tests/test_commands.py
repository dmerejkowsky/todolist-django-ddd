import pytest

from task_manager.commands import Add, Check, Remove, UnCheck
from task_manager.repositories.in_memory import InMemoryRepository
from task_manager.tasks import Task


def test_add_one_task() -> None:
    repository = InMemoryRepository()
    add_command = Add(description="Learn Python")
    add_command.execute(repository)

    assert repository.tasks() == [Task(id=1, description="Learn Python", done=False)]


def test_add_two_tasks() -> None:
    repository = InMemoryRepository()
    add_command = Add(description="Learn Python")
    add_command.execute(repository)
    add_command = Add(description="Learn TDD")
    add_command.execute(repository)

    assert repository.tasks() == [
        Task(id=1, description="Learn Python", done=False),
        Task(id=2, description="Learn TDD", done=False),
    ]


def test_check_first_task() -> None:
    repository = InMemoryRepository()
    task_one = Task(id=1, description="one", done=False)
    task_two = Task(id=2, description="two", done=False)

    repository.load_tasks([task_one, task_two])

    check_command = Check(id=1)
    check_command.execute(repository)

    assert repository.tasks() == [
        Task(id=1, description="one", done=True),
        Task(id=2, description="two", done=False),
    ]


def test_uncheck_second_task() -> None:
    repository = InMemoryRepository()
    task_one = Task(id=1, description="one", done=False)
    task_two = Task(id=2, description="two", done=True)

    repository.load_tasks([task_one, task_two])

    uncheck_command = UnCheck(id=2)
    uncheck_command.execute(repository)

    assert repository.tasks() == [
        Task(id=1, description="one", done=False),
        Task(id=2, description="two", done=False),
    ]


def test_remove_task() -> None:
    repository = InMemoryRepository()
    task_one = Task(id=1, description="one", done=False)
    task_two = Task(id=2, description="two", done=False)
    repository.load_tasks([task_one, task_two])

    remove_command = Remove(id=2)
    remove_command.execute(repository)

    assert repository.tasks() == [Task(id=1, description="one", done=False)]


def test_error_when_trying_to_mark_non_existing_task_as_done() -> None:
    repository = InMemoryRepository()
    check_command = Check(id=1)

    with pytest.raises(ValueError):
        check_command.execute(repository)
