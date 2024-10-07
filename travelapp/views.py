from django.shortcuts import render,redirect
from django.http import JsonResponse
from firebase_admin import credentials, db, storage
import firebase_admin
from django.core.files.storage import default_storage
from .serializers import GetForm
from .models import DestinationData
from rest_framework import generics
from rest_framework.permissions import AllowAny
import requests
from django.contrib import messages
from .mail import send_mail
from .imageUrl import get_url
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

class RetriveDestination(generics.RetrieveAPIView):
    queryset = DestinationData.objects.all()
    serializer_class = GetForm

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

        image_url = get_url(image)
        print("image_url:------------------",image_url)
        create_data = {
            "place_name": place_name,
            "picture": image_url,
            "description": description,
            "country": country,
            "state": state,
            "weather": weather,
            "activity": activity,
            "location": location
        }
        print(create_data)
        response1 = requests.post(create_api, data=create_data)
        print(response1.status_code)

    list_api = "http://127.0.0.1:8000/view-destination/"
    response = requests.get(list_api)
    response_data = response.json()
    #print(response_data)


    return render(request,"index.html",context={"data":response_data})

def moreinfo(request,dest_id):
    if request.method == "POST":
        place_name = request.POST.get("place_name")
        description = request.POST.get("description")
        country = request.POST.get("country")
        state = request.POST.get("state")
        weather = request.POST.get("weather")
        activity = request.POST.get("activity")
        location = request.POST.get("location")
        picture = request.FILES.get("picture")

        image_url = get_url(picture)

        new_data = {
            "place_name": place_name,
            "picture": image_url,
            "description": description,
            "country": country,
            "state": state,
            "weather": weather,
            "activity": activity,
            "location": location
        }

        #print(new_data)
        
        update_url = f"http://127.0.0.1:8000/update-destination/{dest_id}/"
        response = requests.put(update_url, data=new_data)
        print("status_code:---------------:",response.status_code)
        if response.status_code == 200:
            print("updated successfully")
            return redirect(f"http://127.0.0.1:8000/moreinfo/{dest_id}")
        else:
            print("cannot update")
            messages.error(request, f"error submitting data to rest_api, {response.status_code}")
    
    list_api = f"http://127.0.0.1:8000/retrive/{dest_id}/"
    response = requests.get(list_api)
    response_data = response.json()
    data = response_data
    #print(data)
    return render(request,"moreinfo.html", context={"data":data})

def destinations(request):
    list_api = "http://127.0.0.1:8000/view-destination/"
    response = requests.get(list_api)
    response_data = response.json()
    #print(response_data)

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

def DeleteDest(request,id):
    print("print id________________________", id)
    dest_id = request.POST.get("dest_id")
    delete_url = f"http://127.0.0.1:8000/delete-destination/{id}/"
    response = requests.delete(delete_url)
    print(response.status_code)
    return redirect("destinations")