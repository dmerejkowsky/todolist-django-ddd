from task_manager.todo_list import TodoList
from task_manager.parser import parse_command


def display_todo_list(todo_list: TodoList) -> None:
    if todo_list.empty():
        print("No tasks yet")
    for task in todo_list.tasks():
        check_box = "[x]" if task.done else "[ ]"
        print(task.id, check_box, task.description)


def main() -> None:
    todo_list = TodoList()
    display_todo_list(todo_list)
    while True:
        line = input("> ")
        if line[0] == "q":
            break
        command = parse_command(line)
        command.execute(todo_list)
        display_todo_list(todo_list)
