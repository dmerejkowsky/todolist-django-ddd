class Command:
    pass


class Add(Command):
    def __init__(self, description: str) -> None:
        self.description = description


class Check(Command):
    def __init__(self, id: int) -> None:
        self.id = id


class UnCheck(Command):
    def __init__(self, id: int) -> None:
        self.id = id
