from django.shortcuts import render
from django.http import JsonResponse
from firebase_admin import credentials, db, storage
import firebase_admin
from django.core.files.storage import default_storage
from .serializers import GetForm
from .models import DestinationData
from rest_framework import generics
from rest_framework.permissions import AllowAny
# Create your views here.



class GetData(generics.ListCreateAPIView):
    serializer_class = GetForm
    queryset = DestinationData.objects.all()
    permission_classes = [AllowAny]


# def index(request):
#     if request.method == "POST":
#         place_name = request.POST.get("place_name")
#         image = request.FILES.get("image")
#         country = request.POST.get("country")
#         state = request.POST.get("state")
#         weather = request.POST.get("weather")
#         activity = request.POST.get("activity")
#         location = request.POST.get("location")

#     return render(request,"index.html")

def my_view(request):
    # Reading data from Firebase Realtime Database
    ref = db.reference('user')
    data = ref.set({
        'name': "sadiiq",
        "email": "sadiq@gmail.com"
    })
    return JsonResponse(data)