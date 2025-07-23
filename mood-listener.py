import firebase_admin
from firebase_admin import credentials, db
import time
import json
import os

# Initialize Firebase
cred = credentials.Certificate("/Users/aliendelon/carpet-mood-ui/carpet-mood-firebase-adminsdk-fbsvc-337b3a6da3.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://carpet-mood-default-rtdb.europe-west1.firebasedatabase.app'
})

def get_mood():
    ref = db.reference('mood')
    return ref.get()

OUTPUT_FILE = "mood.json"

if __name__ == "__main__":
    last_mood = None

    while True:
        mood = get_mood()

        if mood != last_mood:
            print("New mood:", mood)
            with open(OUTPUT_FILE, 'w') as f:
                json.dump(mood, f)
            last_mood = mood

        time.sleep(5)