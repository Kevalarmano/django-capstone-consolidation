# Django News Capstone

A Django REST Framework API for managing news articles and users.

---

## Project Structure

```
django-capstone-consolidation/
├── project/          # Django project settings & root URLs
├── news/             # News articles and categories app
├── users/            # Custom user model and registration app
├── docs/             # Sphinx documentation
├── manage.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## Authentication (JWT)

This API uses JWT tokens for authentication via `djangorestframework-simplejwt`.

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/token/` | Login — obtain access & refresh tokens |
| POST | `/api/token/refresh/` | Refresh an access token |

**Example login request:**
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

Use the returned `access` token in the `Authorization` header for protected endpoints:
```
Authorization: Bearer <access_token>
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/users/` | List all users |
| POST | `/api/users/register/` | Register a new user |
| GET/PUT/DELETE | `/api/users/<id>/` | Retrieve / update / delete a user |
| GET | `/api/news/articles/` | List all articles |
| POST | `/api/news/articles/` | Create a new article |
| GET/PUT/DELETE | `/api/news/articles/<id>/` | Retrieve / update / delete an article |
| GET | `/api/news/categories/` | List all categories |
| POST | `/api/news/categories/` | Create a new category |
| GET/PUT/DELETE | `/api/news/categories/<id>/` | Retrieve / update / delete a category |

---

## Setup — Virtual Environment

```bash
# 1. Clone the repo
git clone https://github.com/Kevalarmano/django-capstone-consolidation
cd django-capstone-consolidation

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create a superuser (optional)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

The API will be available at: `http://localhost:8000`

---

## Setup — Docker

```bash
# Build and run the container
docker build -t django-news-capstone .
docker run -p 8000:8000 django-news-capstone
```

Or using Docker Compose:

```bash
docker-compose up --build
```

The API will be available at: `http://localhost:8000`

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DEBUG` | `True` | Enable/disable debug mode |
| `SECRET_KEY` | (set in settings.py) | Django secret key — change in production |

---

## Running Tests

```bash
python manage.py test
```

---

## Sphinx Documentation

The generated documentation is located in `docs/_build/html/`. Open `docs/_build/html/index.html` in a browser to view it.

To regenerate the documentation:

```bash
cd docs
sphinx-build -b html . _build/html
```

---


