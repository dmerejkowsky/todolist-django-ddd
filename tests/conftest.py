import pytest

import webapp.env
from task_manager.repositories.in_memory import InMemoryRepository


@pytest.fixture
def test_repository() -> InMemoryRepository:
    webapp.env.repository = InMemoryRepository()
    return webapp.env.repository
