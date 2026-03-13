"""Tests for the news app."""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Article, Category

User = get_user_model()


class CategoryModelTest(TestCase):
    """Test cases for the Category model."""

    def test_create_category(self):
        """Test creating a category."""
        cat = Category.objects.create(name='Technology', description='Tech news')
        self.assertEqual(str(cat), 'Technology')
        self.assertEqual(cat.name, 'Technology')

    def test_category_ordering(self):
        """Test categories are ordered by name."""
        Category.objects.create(name='Sport')
        Category.objects.create(name='Politics')
        cats = list(Category.objects.values_list('name', flat=True))
        self.assertEqual(cats, sorted(cats))


class ArticleModelTest(TestCase):
    """Test cases for the Article model."""

    def setUp(self):
        self.user = User.objects.create_user(username='writer', password='pass123')
        self.cat = Category.objects.create(name='General')

    def test_create_article(self):
        """Test creating an article."""
        article = Article.objects.create(
            title='Test Article',
            content='This is test content.',
            author=self.user,
            category=self.cat,
            status='published',
        )
        self.assertEqual(str(article), 'Test Article')
        self.assertEqual(article.author.username, 'writer')
        self.assertEqual(article.status, 'published')

    def test_article_default_status(self):
        """Test that the default article status is draft."""
        article = Article.objects.create(
            title='Draft Article',
            content='Draft content.',
            author=self.user,
        )
        self.assertEqual(article.status, 'draft')
