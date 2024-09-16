from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models

# Create class based generic view to list all posts from database
class PostList(generic.ListView):
    # queryset to fetch all posts
    queryset = models.Post.objects.all()
    # template name 
    template_name = "blog/index.html"
    # declare a custom context object name
    context_object_name = "posts"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    post = get_object_or_404(models.Post, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "coder": "mustafa"},
    )
    


