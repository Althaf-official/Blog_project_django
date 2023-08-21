from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Define a Category model to categorize articles
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Define the Article model
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title