import os
import sys

# Add project root to Python path
sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------
project = "Django Capstone"
author = "Keval"
release = "1.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"

# --- Django setup for autodoc (IMPORTANT) ---
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "capstone_project.settings")
import django
django.setup()
