from django.urls import include, path

urlpatterns = [
    path("todos/", include("todos.urls")),
]
