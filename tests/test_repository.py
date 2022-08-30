from task_manager.repositories.in_memory import InMemoryRepository


def test_starts_empty() -> None:
    repository = InMemoryRepository()
    assert repository.empty()
