from firebase_admin import credentials, db
import firebase_admin


import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("TRAVELPROJECT/firebase_config.py")
firebase_admin.initialize_app(cred,{
    "databaseURL": "https://travellogram-2a80c-default-rtdb.firebaseio.com/"
})
