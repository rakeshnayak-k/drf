from django.contrib import admin
from django.urls import path
from .views import StudentsAPI

urlpatterns = [
    path('students/', StudentsAPI.as_view()),
]