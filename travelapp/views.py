from django.shortcuts import render
from django.http import JsonResponse
from firebase_admin import credentials, db, storage
import firebase_admin

# Create your views here.

config = {
    "type": "service_account",
    "project_id": "travellogram-2a80c",
    "private_key_id": "b54632e765918a6dee5bfe35a912436994afb604",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDTRloAih1NSEv7\ncmuDfK1PxByOKsB8gzIHtCoelmbEJ5DJBNh2Svdgc4J4kkHF/f+P5DR6ZbSN+VEL\no1TXov5V7mWevgj+AjUcyjPU8ZqZ/I/PfnKZKFLoIyFpttvXKqGTgCZrNBKbckZU\nK19Ic0cwX6OzZiPuRppqwKqpq6DAgQEpzGfmszWnGntBj7Aiv2xaczN92aflYM6b\nI4xuVtZhYs+p8VV1xDlLePaDBThglZBgbk9vGZ9XW0FJF8fhFBxP2P95T39F5V4n\nmUC8MUIgzCF3U+8u7Q0QynSuJD8lEzo6/uILnPERAPJLqKK7lk2pnR/Vei3nVD7X\nGPbrkEl/AgMBAAECggEABPkNg45O9kFJqtd4CzrTLOwKNb1McNiv+scDHskwoFTD\nys5WrWtCTaMqYrlHtwx2mpy5VTTDoumQ0MmY0n32OXAj654JeLf1J4JS5W0W+Hzm\ny14RIsAGzK9pSREkfmaZn5NzwcLJcMM6Y/qAOaSfRTI2hjGeIJqAQa3bRDcch4bS\nSY2RUD732YdtPiLGIRdL6bb98rOqX6nLOjLpJsrfqFtiiCw9ssPhOR/KgNkwFnDK\nA8eOCrOFlCWu0NvTP59E4iNN3vCy/igPzZdA+JpIHni0gxmZyH3kn1MtnIzSNHyZ\nEEmnrfBjlwHivjQJd1Pt6KMT2/dIyPL416zRfVYJ4QKBgQDv42h2rgMLbr7cWfPr\n8djB0NgCfvQGoJcsxkdOODwBNcViHmEqV8hmBAHXC+YyeTNe9+VqkCTvj1pB0MBq\nZsdNQN9vHXJ47iPwj6QS39Z6vJbx5jGKMUJKWHiVOaiPK28IGwr6xwpqvfdLC35J\nYwosU+JTZC03jOmtyqwknvMnZwKBgQDhdvf5XExiqGFTKKkkIunp3CZdzrECWKCQ\nblLYCAMY6d2Hgf/Clk0ZPbgM0cjm9I/fwhScnRKDK47lohp3CC2espO2ZLr9tppE\n35IIkWs1FRNbaW2jwSuYXWiellyBJePCvU16X3Irkzs+osGpWPrItwGae364MwGf\nKn7uS+72KQKBgFC4wD03XvTo5ja12juqHRtTEGz+lVTpkxVQ/0uV5rMtiebzfBTI\nhzm03X2klmijmiK53iwWpycpoOCGw0jKnwQi8UytpwiEcfmQDFEBm2Wfsldh84eh\n/cGQtbrZNRxALFOY7f/nHF1A4UcSbgN53UF/VKhlDEYmF7gQfA6yofW/AoGAP/qH\ncW48ir5nJ7bhEE0L/X2oMXRmjFjj7zgvL/hOELLEVyCPmAMYi7IU2SZqkQcTEJa9\nTJfR2gDxQr5WLjLW5zKbceVxnm9DpYmfoejJ+D0rygPHxfEZ0tmmx2G5jDhZQjh/\nlNsixbS42hRLSifiujQcM18Z3WEz85uWez5258kCgYEAi4zSi91XwRNZN4Xs+of+\n8vuSumHEFxIGSibvpUhWEoi7KyuC+9Xab33TftAVjNDWANmtgNXdwVCEk8H1Bqg7\noOjhtVpbGqxgKGV4ZV0A6UgUYMqXQ5DZRQHgcf7UT2BJb8yBLvjwTOg63iDLKqMf\nstpHNex8A+m+dMxoQUgnAYU=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-8w1jg@travellogram-2a80c.iam.gserviceaccount.com",
    "client_id": "108402424620820674904",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-8w1jg%40travellogram-2a80c.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
  }


cred = credentials.Certificate(config)
firebase_admin.initialize_app(cred,{
    "databaseURL": "https://travellogram-2a80c-default-rtdb.firebaseio.com/",
    'storageBucket': 'gs://travellogram-2a80c.appspot.com'
})




def index(request):
    if request.method == "POST":
        place_name = request.POST.get("place_name")
        image = request.FILES.get("image")
        country = request.POST.get("country")
        state = request.POST.get("state")
        weather = request.POST.get("weather")
        activity = request.POST.get("activity")
        location = request.POST.get("location")

        print(place_name, image, country, state, weather, activity, location)

        # ref = db.reference("users")
        ref = db.reference("places")
        ref.push({
            "place_name": place_name,
            "country": country,
            "state": state,
            "weather": weather,
            "activity": activity,
            "location": location
        })

    return render(request,"index.html")

def my_view(request):
    # Reading data from Firebase Realtime Database
    ref = db.reference('user')
    data = ref.set({
        'name': "sadiiq",
        "email": "sadiq@gmail.com"
    })
    return JsonResponse(data)