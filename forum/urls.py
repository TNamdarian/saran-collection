"""
URLs for Forum App includng Forum, Add, View and Delete Threads,
and Add, View and Delete Comments
"""
from django.urls import path
from . import views
from .views import (
    ThreadView,
    AddThreadView,
    EditThreadView,
    DeleteThreadView,
    AddCommentView,
    EditCommentView,
    DeleteCommentView,
)

# Class based views & urls https://bit.ly/3DyP7wf
urlpatterns = [
    path('', views.forum_view, name='forum'),
    path('thread/<int:pk>', ThreadView.as_view(), name="thread"),
    path('add_thread/', AddThreadView.as_view(), name="add_thread"),
    path('thread/edit/<int:pk>', EditThreadView.as_view(), name="edit_thread"),
    path('thread/delete/<int:pk>', DeleteThreadView.as_view(),
         name="delete_thread"),
    path('thread/<int:pk>/add_comment/', AddCommentView.as_view(),
         name="add_comment"),
    path('edit_comment/<int:pk>', EditCommentView.as_view(),
         name="edit_comment"),
    path('comment/delete/<int:pk>', DeleteCommentView.as_view(),
         name="delete_comment")
]