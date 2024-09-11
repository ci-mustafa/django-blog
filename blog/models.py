from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    DRAFT = 0
    PUBLISHED = 1
    STATUS_CHOICES = (
        (DRAFT, "Draft"),
        (PUBLISHED, "Published")
    )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)
    excerpt = models.TextField(null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")

