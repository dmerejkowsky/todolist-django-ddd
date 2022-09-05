from task_manager.repositories.in_memory import InMemoryRepository
from task_manager.tasks import Task


def test_starts_empty() -> None:
    repository = InMemoryRepository()
    assert repository.empty()


def test_create_task() -> None:
    repository = InMemoryRepository()
    repository.add_task("learn python")

    (task,) = repository.tasks()
    assert task.description == "learn python"
    assert not task.done


def test_update_task_status() -> None:
    repository = InMemoryRepository()
    task = Task(id=1, description="some description", done=False)
    repository.load_tasks([task])
    repository.update_task_status(id=1, done=True)

    (task,) = repository.tasks()
    assert task.done


def test_remove_task() -> None:
    repository = InMemoryRepository()
    task_1 = Task(id=1, description="one", done=False)
    task_2 = Task(id=2, description="two", done=False)
    repository.load_tasks([task_1, task_2])

    repository.remove_task(id=1)

    (task,) = repository.tasks()
    assert task.id == 2
