from task_manager.repository import Repository


def get_repository() -> Repository:
    from todos.repository import Repository as DjangoRepository

    return DjangoRepository()


repository = get_repository()
