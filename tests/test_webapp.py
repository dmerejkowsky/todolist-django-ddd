from typing import Any

import pytest

from todos.models import Task


def test_index(client: Any) -> None:
    response = client.get("/todos/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_task(client: Any) -> None:
    response = client.post("/todos/task", data={"description": "new task"})
    assert response.status_code == 201

    tasks = Task.objects.all()
    assert len(tasks) == 1, "expected one task to be created"


@pytest.mark.django_db
def test_update_task(client: Any) -> None:
    task_1 = Task.objects.create(description="one", done=False)
    task_2 = Task.objects.create(description="two", done=False)

    response = client.post(f"/todos/task/{task_1.id}", data={"done": "True"})
    assert response.status_code == 200

    task_1.refresh_from_db()
    assert task_1.done
    task_2.refresh_from_db()
    assert not task_2.done


@pytest.mark.django_db
def test_delete_task(client: Any) -> None:
    task_1 = Task.objects.create(description="one", done=False)
    task_2 = Task.objects.create(description="two", done=False)  # noqa: F841

    response = client.delete(f"/todos/task/{task_1.id}")
    assert response.status_code == 200

    assert list(Task.objects.all().order_by("id")) == [task_1]
