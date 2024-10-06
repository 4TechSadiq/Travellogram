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
from .mail import send_mail
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
        description = request.POST.get("description")
        image = request.FILES.get("image")
        country = request.POST.get("country")
        state = request.POST.get("state")
        weather = request.POST.get("weather")
        activity = request.POST.get("activity")
        location = request.POST.get("location")
        create_api = "http://127.0.0.1:8000/create-destination/"
        create_data = {
            "place_name": place_name,
            "description": description,
            "country": country,
            "state": state,
            "weather": weather,
            "activity": activity,
            "location": location
        }
        response1 = requests.post(create_api, data=create_data, files={"picture": image})
        print(response1.status_code)

    list_api = "http://127.0.0.1:8000/view-destination/"
    response = requests.get(list_api)
    response_data = response.json()
    print(response_data)


    return render(request,"index.html",context={"data":response_data})

def moreinfo(request,dest_id):
    data = DestinationData.objects.get(dest_id)
    return render(request,"moreinfo.html", context={"data":data})

def destinations(request):
    list_api = "http://127.0.0.1:8000/view-destination/"
    response = requests.get(list_api)
    response_data = response.json()
    print(response_data)

    return render(request,"places.html",context={"data":response_data})

def my_view(request):
    # Reading data from Firebase Realtime Database
    ref = db.reference('user')
    data = ref.set({
        'name': "sadiiq",
        "email": "sadiq@gmail.com"
    })
    return JsonResponse(data)


def Aboutus(request):
    return render(request,"aboutUs.html")

def Contactus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        send_mail(mail=email,name=name,msg=message)
    return render(request,"contactUs.html")