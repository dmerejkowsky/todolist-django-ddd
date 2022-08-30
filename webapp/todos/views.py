from django.http import HttpRequest, HttpResponse

from webapp import env


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello")


def create_task(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)
    description = request.POST.get("description")
    if not description:
        return HttpResponse("Missing description in body", status=400)

    env.repository.add_task(description)

    return HttpResponse("Task created", status=201)


def update_task(request: HttpRequest, id: int) -> HttpResponse:

    if request.method == "DELETE":
        env.repository.remove_task(id)
        return HttpResponse("Task deleted", status=200)

    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)

    new_status = request.POST.get("done")
    if not new_status:
        return HttpResponse("Missing 'done' in body", status=400)

    env.repository.update_task_status(id, done=bool(new_status))
    return HttpResponse("Task updated", status=200)