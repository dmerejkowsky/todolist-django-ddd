from typing import Any

from task_manager.repositories.in_memory import InMemoryRepository
from task_manager.tasks import Task


def test_index(client: Any) -> None:
    response = client.get("/todos/")
    assert response.status_code == 200


def test_create_task(client: Any, test_repository: InMemoryRepository) -> None:
    response = client.post("/todos/task", data={"description": "new task"})
    assert response.status_code == 201

    tasks = test_repository.tasks()
    assert len(tasks) == 1, "expected one task to be created"


def test_update_task(client: Any, test_repository: InMemoryRepository) -> None:
    task_1 = Task(id=1, description="one", done=False)
    task_2 = Task(id=2, description="two", done=False)
    test_repository.load_tasks([task_1, task_2])

    response = client.post(f"/todos/task/{task_1.id}", data={"done": "True"})
    assert response.status_code == 200

    tasks = test_repository.tasks()
    task_1, task_2 = tasks
    assert task_1.done
    assert not task_2.done


def test_delete_task(client: Any, test_repository: InMemoryRepository) -> None:
    task_1 = Task(id=1, description="one", done=False)
    task_2 = Task(id=2, description="two", done=False)
    test_repository.load_tasks([task_1, task_2])

    response = client.delete(f"/todos/task/{task_1.id}")
    assert response.status_code == 200

    tasks = test_repository.tasks()
    assert tasks == [task_2]
