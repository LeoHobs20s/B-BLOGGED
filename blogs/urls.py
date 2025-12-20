""" Defining URL patterns for Blogs """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]