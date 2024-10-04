from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create-destination/", views.CreateDestination.as_view(), name="create-destination"),
    path("view-destination/", views.ViewDestination.as_view(), name="view-destination"),
    path("update-destination/<str:pk>/", views.UpdateDestination.as_view(), name="update-destination"),
    path("delete-destination/<str:pk>/", views.DeleteDestination.as_view(), name="delete-destination"),
]
