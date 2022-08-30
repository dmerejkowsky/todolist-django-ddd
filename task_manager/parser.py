from task_manager.commands import Add, Check, Command, Remove, UnCheck


def parse_command(line: str) -> Command:
    letter, rest = line[0], line[2:]
    if letter == "+":
        return Add(description=rest)
    id = int(rest)
    if letter == "-":
        return Remove(id=id)
    if letter == "x":
        return Check(id=id)
    if line[0] == "o":
        return UnCheck(id=id)

    raise ValueError(f"Invalid first character: {line[0]}")
