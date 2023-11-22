from django.contrib import admin
from django.urls import path
from .views import students

urlpatterns = [
    path('students/', students),
]