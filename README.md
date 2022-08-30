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

There's a quite a lot of duplication between the tests.


## The Ugly

We mutate `webapp.env.repository` (a global!) during the tests, when the `test_repository` fixture
is used
