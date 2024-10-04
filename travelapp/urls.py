from django.urls import path
from . import views

urlpatterns = [
    path("create-destination/", views.GetData.as_view(), name="create-destination"),
]
