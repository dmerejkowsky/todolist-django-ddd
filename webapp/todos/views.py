from django.http import HttpRequest, HttpResponse

from task_manager.commands import Add, Check, Command, Remove, UnCheck
from webapp import env


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello")


def create_task(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)
    description = request.POST.get("description")
    if not description:
        return HttpResponse("Missing description in body", status=400)

    command = Add(description)
    command.execute(env.repository)

    return HttpResponse("Task created", status=201)


def update_task(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == "DELETE":
        remove_command = Remove(id)
        remove_command.execute(env.repository)

        return HttpResponse("Task deleted", status=200)

    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)

    new_status = request.POST.get("done")
    if not new_status:
        return HttpResponse("Missing 'done' in body", status=400)

    if new_status:
        update_command: Command = Check(id)
    else:
        update_command = UnCheck(id)

    update_command.execute(env.repository)
    return HttpResponse("Task updated", status=200)
