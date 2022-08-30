from task_manager.todo_list import TodoList


def test_starts_empty() -> None:
    todo_list = TodoList()
    assert not todo_list.tasks()
