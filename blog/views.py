from django.shortcuts import render
from django.views import generic
from . import models

# Create class based generic view to list all posts from database
class PostList(generic.ListView):
    # queryset to fetch all posts
    queryset = models.Post.objects.all()
    # template name 
    template_name = "post_list.html"
    # declare a custom context object name
    context_object_name = "posts"
    


