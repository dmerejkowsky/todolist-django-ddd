from task_manager.commands import Add, Check, UnCheck
from task_manager.parser import parse_command


def test_parse_add() -> None:
    line = "+ Learn Python"
    command = parse_command(line)
    assert isinstance(command, Add)
    assert command.description == "Learn Python"


def test_parse_check() -> None:
    line = "x 1"
    command = parse_command(line)
    assert isinstance(command, Check)
    assert command.id == 1


def test_parse_uncheck() -> None:
    line = "o 2"
    command = parse_command(line)
    assert isinstance(command, UnCheck)
    assert command.id == 2
