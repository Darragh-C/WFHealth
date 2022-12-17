import firebase_admin
from firebase_admin import credentials, firestore, storage, db
import os

cred=credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'pibell-893ac.appspot.com', # REPLACE WITH YOUR BUCKET ID
    'databaseURL': 'https://pibell-893ac-default-rtdb.europe-west1.firebasedatabase.app/' #
})

bucket = storage.bucket()

# realtime db ref
ref = db.reference('/')

# temperature_and_humidity node
temp_humid_ref = ref.child('temperature_and_humidity')

def push_db_temp_humid(temp, humid, time):
    # Push temp, humid, and timestamp data to Realtime DB
    temp_humid_ref.push({
        'date': time,
        'temperature': temp,
        'humidity': humid
        },
)

