from django.urls import path
from .views import hello_world

urlpatterns = [
    path('query-system/', hello_world),
]
