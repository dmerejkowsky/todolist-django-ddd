from pathlib import Path

from task_manager.parser import parse_command
from task_manager.repositories.json_db import JsonDB
from task_manager.repository import Repository


def display_tasks(repository: Repository) -> None:
    if repository.empty():
        print("No tasks yet")
    for task in repository.tasks():
        check_box = "[x]" if task.done else "[ ]"
        print(task.id, check_box, task.description)


def main() -> None:
    repository = JsonDB(Path("tasks.json"))
    display_tasks(repository)
    while True:
        line = input("> ")
        if line[0] == "q":
            break
        command = parse_command(line)
        command.execute(repository)
        display_tasks(repository)


if __name__ == "__main__":
    main()
