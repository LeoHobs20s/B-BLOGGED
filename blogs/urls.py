""" Defining URL patterns for Blogs """

from django.urls import path
from . import views
from .views import NewPostView, UpdatePostView

urlpatterns = [
    path('', views.index, name='index'),
    path('add_post/', NewPostView.as_view(template_name='blogs/add_post.html'), name='add_post'),
    path('edit_post/<int:post_id>/', UpdatePostView.as_view(template_name='blogs/edit_post.html'), name='edit_post')
]