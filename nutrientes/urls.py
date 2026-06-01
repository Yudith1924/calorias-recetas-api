# nutrientes/urls.py
from django.urls import path
from .views import nutrientes

urlpatterns = [
    path("", nutrientes, name="nutrientes"),
]
