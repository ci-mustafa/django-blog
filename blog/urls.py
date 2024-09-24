from django.urls import path
from .views import PostList, post_detail, comment_edit, comment_delete

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         comment_delete, name='comment_delete'),
]