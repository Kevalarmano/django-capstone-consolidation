from django.db import models

class Store(models.Model):
    """
    Represents a store created by a vendor.

    Attributes:
        name (str): The name of the store.
        description (str): Description of the store.
        created_at (datetime): Timestamp of store creation.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
