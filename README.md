cat > README.md <<'EOF'
# Django Capstone Consolidation (DRF API)

This project demonstrates:
- A Django REST Framework API
- Git workflow (branches/merges)
- Sphinx documentation generation
- Docker container setup

## Requirements
- Python 3.12+
- pip
- (Optional) Docker + Docker Compose

## Setup (Local / Codespaces)
```bash
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
