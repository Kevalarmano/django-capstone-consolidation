"""
Views for the users app.
Provides user registration and user detail endpoints.
"""
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserRegisterSerializer

User = get_user_model()


class UserListView(generics.ListAPIView):
    """
    GET /api/users/
    Returns a list of all registered users.
    """
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer


class UserRegisterView(generics.CreateAPIView):
    """
    POST /api/users/register/
    Registers a new user account.
    """
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                'message': 'User registered successfully.',
                'user': UserSerializer(user).data,
            },
            status=status.HTTP_201_CREATED,
        )


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/users/<id>/  — Retrieve a user
    PUT    /api/users/<id>/  — Update a user
    DELETE /api/users/<id>/  — Delete a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
