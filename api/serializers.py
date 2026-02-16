from rest_framework import serializers
from .models import Store


class StoreSerializer(serializers.ModelSerializer):
    """Serializer for the Store model."""

    class Meta:
        model = Store
        fields = "__all__"
