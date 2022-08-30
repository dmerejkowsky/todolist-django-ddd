from django.urls import path

from todos import views

urlpatterns = [
    path("", views.index),
    path("task", views.create_task),
    path("task/<int:id>", views.update_task),
]
