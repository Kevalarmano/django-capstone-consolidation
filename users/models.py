"""
Custom user model for the Django News Capstone.
Extends AbstractUser to add a bio field.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Extended user model with a bio field.
    Used as the AUTH_USER_MODEL for this project.
    """
    bio = models.TextField(blank=True, null=True, help_text="A short biography of the user.")

    def __str__(self):
        return self.username
