from django.urls import path
from .views import *



urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('profile/', UserAccountView.as_view()),
]