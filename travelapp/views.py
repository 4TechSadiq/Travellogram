from django.shortcuts import render
from django.http import JsonResponse
from firebase_admin import credentials, db, storage
import firebase_admin
from django.core.files.storage import default_storage
from .serializers import GetForm
from .models import DestinationData
from rest_framework import generics
from rest_framework.permissions import AllowAny
import requests
# Create your views here.



class CreateDestination(generics.ListCreateAPIView):
    serializer_class = GetForm
    queryset = DestinationData.objects.all()
    permission_classes = [AllowAny]


class ViewDestination(generics.ListAPIView):
    serializer_class = GetForm
    queryset = DestinationData.objects.all()

class UpdateDestination(generics.RetrieveUpdateAPIView):
    serializer_class = GetForm
    queryset = DestinationData.objects.all()
    permission_classes = [AllowAny]


class DeleteDestination(generics.DestroyAPIView):
    serializer_class = GetForm
    queryset = DestinationData.objects.all()

def index(request):
    if request.method == "POST":
        place_name = request.POST.get("place_name")
        image = request.FILES.get("image")
        country = request.POST.get("country")
        state = request.POST.get("state")
        weather = request.POST.get("weather")
        activity = request.POST.get("activity")
        location = request.POST.get("location")

    api_url = "http://127.0.0.1:8000/view-destination/"
    response = requests.get(api_url)
    data = response.json()
    print(data)


    return render(request,"index.html",context={"data":data})

def my_view(request):
    # Reading data from Firebase Realtime Database
    ref = db.reference('user')
    data = ref.set({
        'name': "sadiiq",
        "email": "sadiq@gmail.com"
    })
    return JsonResponse(data)