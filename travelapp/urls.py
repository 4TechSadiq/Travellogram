from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("name/", views.my_view)
]
