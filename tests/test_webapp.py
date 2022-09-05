import pytest
from flask import Flask

from app import create_app, get_repo
from task_manager.repositories.in_memory import InMemoryRepository
from task_manager.tasks import Task


@pytest.fixture
def app() -> Flask:
    app = create_app()
    app.testing = True
    return app


def test_index(app: Flask) -> None:
    with app.test_client() as client:
        response = client.get("/tasks")
        assert response.status_code == 200
        json = response.get_json()
        assert json == {"tasks": []}


def test_create_task(app: Flask) -> None:
    with app.test_client() as client:
        response = client.post("/task", json={"description": "new task"})
        assert response.status_code == 201

        repo = get_repo()
        tasks = repo.tasks()
        assert len(tasks) == 1, "expected one task to be created"


def test_update_task(app: Flask) -> None:
    with app.test_client() as client:
        with app.app_context():
            repo = get_repo()
            task_1 = Task(id=1, description="one", done=False)
            task_2 = Task(id=2, description="two", done=False)
            repo.load_tasks([task_1, task_2])

            response = client.post(f"/task/{task_1.id}", json={"done": "True"})
            assert response.status_code == 200

            tasks = repo.tasks()
            task_1, task_2 = tasks
            assert task_1.done
            assert not task_2.done


"""
def test_delete_task(client: Any, test_repository: InMemoryRepository) -> None:
    task_1 = Task(id=1, description="one", done=False)
    task_2 = Task(id=2, description="two", done=False)
    test_repository.load_tasks([task_1, task_2])

    response = client.delete(f"/todos/task/{task_1.id}")
    assert response.status_code == 200

    tasks = test_repository.tasks()
    assert tasks == [task_2]
    """
