from task_manager.commands import Add, Check, Command, UnCheck


def parse_command(line: str) -> Command:
    letter, rest = line[0], line[2:]
    if letter == "+":
        return Add(description=rest)
    if letter == "x":
        id = int(rest)
        return Check(id=id)
    if line[0] == "o":
        id = int(rest)
        return UnCheck(id=id)

    raise ValueError(f"Invalid first character: {line[0]}")
