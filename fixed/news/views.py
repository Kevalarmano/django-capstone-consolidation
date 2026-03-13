"""
Views for the news app.
Provides full CRUD for Articles and Categories via the REST API.
"""
from rest_framework import generics, filters
from .models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/news/categories/        — List all categories
    POST /api/news/categories/        — Create a new category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/news/categories/<id>/  — Retrieve a category
    PUT    /api/news/categories/<id>/  — Update a category
    DELETE /api/news/categories/<id>/  — Delete a category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/news/articles/          — List all published articles
    POST /api/news/articles/          — Create a new article
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'author__username', 'category__name']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/news/articles/<id>/    — Retrieve an article
    PUT    /api/news/articles/<id>/    — Update an article
    DELETE /api/news/articles/<id>/    — Delete an article
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
