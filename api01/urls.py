from django.urls import path

from .import views

urlpatterns=[
    path('api/', views.api01, name='api01'),
]