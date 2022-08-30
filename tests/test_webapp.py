from typing import Any


def test_index(client: Any) -> None:
    client.get("/")
