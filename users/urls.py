"""
URL patterns for the users app.
"""
from django.urls import path
from .views import UserListView, UserRegisterView, UserDetailView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
