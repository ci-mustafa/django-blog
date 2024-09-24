from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from . import models
from .forms import CommentForm

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
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment submitted and awaiting approval')
    comment_form = CommentForm()
    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form},
    )
    


