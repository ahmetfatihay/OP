
from django.urls import path
from .views import UserRegisterView, PasswordChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password'))
    path('password/', PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password_success', views.password_success, name="password_success")
]
