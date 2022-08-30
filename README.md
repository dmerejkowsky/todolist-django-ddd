# Hexa in Django

An example of using hexagonal architecture with Django

We "prove" the architecture works by:

* Having both a CLI and a Web API
* Having both a DB backed by a JSON file and the Django ORM

## The Good

We can write end-to-end tests using the Django test client, *without* hitting the django DB, which
could speed things up.

We never have to call `refresh_from_db()` in the tests (which often happens when writing tests using the django ORM directly)

In `tests/test_repository.py` we check that both implementations of the `Repository` work the same way.

## The Bad

Django requires *two* folders, one for the "project", and an other for the "app".

So here, `task_manager` contains the core stuff, `webapp` the Django project and `todos` the Django app.


## The Ugly

We mutate `webapp.env.repository` (a global!) during the tests, when the `test_repository` fixture
is used
