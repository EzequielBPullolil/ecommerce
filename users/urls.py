from django.urls import path, include
from users.views import (
    UserRegisterView,
    UserLoginView
)
urlpatterns = [
    path('register', UserRegisterView.as_view(), name='user_register'),
    path('login', UserLoginView.as_view(), name='user_login')
]
