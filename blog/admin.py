from django.contrib import admin
from .models import Post, Comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ["title", "slug", "content", "excerpt", "status", "author"]



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ["post", "author", "body", "approved"]
