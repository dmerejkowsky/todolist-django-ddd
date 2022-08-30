from task_manager.parser import parse_command
from task_manager.repositories.in_memory import InMemoryRepository
from task_manager.repository import Repository


def display_tasks(repository: Repository) -> None:
    if repository.empty():
        print("No tasks yet")
    for task in repository.tasks():
        check_box = "[x]" if task.done else "[ ]"
        print(task.id, check_box, task.description)


def main() -> None:
    repository = InMemoryRepository()
    display_tasks(repository)
    while True:
        line = input("> ")
        if line[0] == "q":
            break
        command = parse_command(line)
        command.execute(repository)
        display_tasks(repository)
