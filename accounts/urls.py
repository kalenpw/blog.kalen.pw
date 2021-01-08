from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from . import views

app_name = "account"

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', LoginView.as_view(
        template_name='accounts/login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('password', views.change_password, name='change_password')
]
