from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='index'),
    path("dogs/", list_dogs, name='dogs'),
    path("delete/<int:pk>/", delete, name='delete'),
]
