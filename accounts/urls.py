""" Define URL patterns for accounts """

from django.urls import path
from . import views
from .views import LoginView, RegistrationView

urlpatterns=[
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', RegistrationView.as_view(template_name='accounts/register.html'), name='register'),
]