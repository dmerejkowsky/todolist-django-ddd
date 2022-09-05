import pytest

from task_manager.repositories.in_memory import InMemoryRepository


@pytest.fixture
def test_repository() -> InMemoryRepository:
    return InMemoryRepository()
