from task_manager.commands import Add, Check, UnCheck, Remove
from task_manager.todo_list import Task, TodoList


def test_add_one_task() -> None:
    todo_list = TodoList()
    add_command = Add(description="Learn Python")
    add_command.execute(todo_list)

    assert todo_list.tasks() == [Task(id=1, description="Learn Python", done=False)]


def test_add_two_tasks() -> None:
    todo_list = TodoList()
    add_command = Add(description="Learn Python")
    add_command.execute(todo_list)
    add_command = Add(description="Learn TDD")
    add_command.execute(todo_list)

    assert todo_list.tasks() == [
        Task(id=1, description="Learn Python", done=False),
        Task(id=2, description="Learn TDD", done=False),
    ]


def test_check_first_task() -> None:
    todo_list = TodoList()
    task_one = Task(id=1, description="one", done=False)
    task_two = Task(id=2, description="two", done=False)

    todo_list.load_tasks([task_one, task_two])

    check_command = Check(id=1)
    check_command.execute(todo_list)

    assert todo_list.tasks() == [
        Task(id=1, description="one", done=True),
        Task(id=2, description="two", done=False),
    ]


def test_uncheck_second_task() -> None:
    todo_list = TodoList()
    task_one = Task(id=1, description="one", done=False)
    task_two = Task(id=2, description="two", done=True)

    todo_list.load_tasks([task_one, task_two])

    uncheck_command = UnCheck(id=2)
    uncheck_command.execute(todo_list)

    assert todo_list.tasks() == [
        Task(id=1, description="one", done=False),
        Task(id=2, description="two", done=False),
    ]


def test_remove_task() -> None:
    todo_list = TodoList()
    task_one = Task(id=1, description="one", done=False)
    task_two = Task(id=2, description="two", done=False)
    todo_list.load_tasks([task_one, task_two])

    remove_command = Remove(id=2)
    remove_command.execute(todo_list)

    assert todo_list.tasks() == [Task(id=1, description="one", done=False)]
