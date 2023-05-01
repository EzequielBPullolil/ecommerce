from django.urls import path, include
from users.views import (
    UserRegisterView
)
urlpatterns = [
    path('register', UserRegisterView.as_view(), name='user_register')
]
