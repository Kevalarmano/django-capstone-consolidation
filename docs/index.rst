Django News Capstone — Documentation
=====================================

Welcome to the Django News Capstone documentation. This project is a
REST API built with Django and Django REST Framework, supporting full
CRUD for news articles, categories, and users with JWT authentication.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   news
   users

Overview
--------

This project contains two Django apps:

- **news** — Manages ``Article`` and ``Category`` models with full CRUD via the REST API.
- **users** — Provides a custom ``CustomUser`` model extending ``AbstractUser``, with registration and management endpoints.

Authentication
--------------

The API uses JWT (JSON Web Tokens) via ``djangorestframework-simplejwt``.

- ``POST /api/token/``         — Obtain access and refresh tokens (login)
- ``POST /api/token/refresh/`` — Refresh an access token

API Endpoints
-------------

Users
~~~~~

- ``GET    /api/users/``           — List all users
- ``POST   /api/users/register/``  — Register a new user
- ``GET    /api/users/<id>/``      — Retrieve a user
- ``PUT    /api/users/<id>/``      — Update a user
- ``DELETE /api/users/<id>/``      — Delete a user

News Articles
~~~~~~~~~~~~~

- ``GET    /api/news/articles/``        — List all articles
- ``POST   /api/news/articles/``        — Create an article
- ``GET    /api/news/articles/<id>/``   — Retrieve an article
- ``PUT    /api/news/articles/<id>/``   — Update an article
- ``DELETE /api/news/articles/<id>/``   — Delete an article

Categories
~~~~~~~~~~

- ``GET    /api/news/categories/``        — List all categories
- ``POST   /api/news/categories/``        — Create a category
- ``GET    /api/news/categories/<id>/``   — Retrieve a category
- ``PUT    /api/news/categories/<id>/``   — Update a category
- ``DELETE /api/news/categories/<id>/``   — Delete a category

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
