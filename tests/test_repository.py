from typing import Type

import pytest

from task_manager.repositories.in_memory import InMemoryRepository
from task_manager.repository import Repository as BaseRepository
from task_manager.tasks import Task
from todos.repository import Repository as DjangoRepository


@pytest.mark.django_db
@pytest.mark.parametrize("repo_class", [DjangoRepository, InMemoryRepository])
def test_starts_empty(repo_class: Type[BaseRepository]) -> None:
    repository = repo_class()
    assert repository.empty()


@pytest.mark.django_db
@pytest.mark.parametrize("repo_class", [DjangoRepository, InMemoryRepository])
def test_create_task(repo_class: Type[BaseRepository]) -> None:
    repository = repo_class()
    repository.add_task("learn python")

    (task,) = repository.tasks()
    assert task.description == "learn python"
    assert not task.done


@pytest.mark.django_db
@pytest.mark.parametrize("repo_class", [DjangoRepository, InMemoryRepository])
def test_update_task_status(repo_class: Type[BaseRepository]) -> None:
    repository = repo_class()
    task = Task(id=1, description="some description", done=False)
    repository.load_tasks([task])
    repository.update_task_status(id=1, done=True)

    (task,) = repository.tasks()
    assert task.done


@pytest.mark.django_db
@pytest.mark.parametrize("repo_class", [DjangoRepository, InMemoryRepository])
def test_remove_task(repo_class: Type[BaseRepository]) -> None:
    repository = repo_class()
    task_1 = Task(id=1, description="one", done=False)
    task_2 = Task(id=2, description="two", done=False)
    repository.load_tasks([task_1, task_2])

    repository.remove_task(id=1)

    (task,) = repository.tasks()
    assert task.id == 2
