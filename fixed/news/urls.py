"""
URL patterns for the news app.
"""
from django.urls import path
from .views import (
    ArticleListCreateView,
    ArticleDetailView,
    CategoryListCreateView,
    CategoryDetailView,
)

urlpatterns = [
    path('articles/', ArticleListCreateView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]
