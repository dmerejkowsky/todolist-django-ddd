from pathlib import Path
from typing import Tuple

from flask import Flask, Response, current_app, g, jsonify, request

from task_manager.commands import Add, Check, Command, UnCheck
from task_manager.repositories.in_memory import InMemoryRepository
from task_manager.repositories.json_db import JsonDB
from task_manager.repository import Repository


def get_repo() -> Repository:
    if "db" not in g:
        if current_app.testing:
            g.db = InMemoryRepository()
        else:
            g.db = JsonDB(Path("tasks.json"))
    return g.db  # type: ignore[no-any-return]


def create_app(testing: bool = False) -> Flask:
    app = Flask("task_manager")

    @app.route("/hello")
    def hello() -> str:
        return "hello"

    @app.route("/tasks")
    def tasks() -> Response:
        repo = get_repo()
        return jsonify({"tasks": repo.tasks()})

    @app.route("/task", methods=["POST"])
    def create_task() -> Tuple[str, int]:
        body = request.json
        if not body:
            return "Invalid json in request", 400

        description = body.get("description")
        if not description:
            return "'description' missing in json body", 400

        repo = get_repo()
        cmd = Add(description)
        cmd.execute(repo)

        return "created", 201

    @app.route("/task/<int:id>", methods=["POST"])
    def update_task(id: int) -> Tuple[str, int]:
        body = request.json
        if not body:
            return "Invalid json in request", 400

        done = body.get("done")
        if not done:
            return "'done' missing in json body", 400

        if done:
            cmd: Command = Check(id)
        else:
            cmd = UnCheck(id)

        repo = get_repo()
        cmd.execute(repo)

        return "{}", 200

    return app
