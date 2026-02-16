from rest_framework import viewsets
from .models import Store
from .serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    """CRUD API for Store."""
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
