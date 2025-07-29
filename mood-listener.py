<<<<<<< HEAD
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
=======
import os
import time
import json
import firebase_admin
from firebase_admin import credentials, db

# === Configuration ===
CRED_PATH = "/carpet-mood-firebase-adminsdk-fbsvc-29ecddb4f0.json"
DB_URL = "https://carpet-mood-default-rtdb.europe-west1.firebasedatabase.app"
OUTPUT_FILE = "mood.json"
POLL_INTERVAL = 5  # seconds

# === Firebase Initialization ===
try:
    cred = credentials.Certificate(CRED_PATH)
    firebase_admin.initialize_app(cred, {
        'databaseURL': DB_URL
    })
    print(f"✅ Firebase initialized with {CRED_PATH}")
except Exception as e:
    print(f"❌ Firebase initialization failed: {e}")
    exit(1)

# === Firebase Data Retrieval ===
def get_combined_data():
    try:
        root = db.reference('/')
        data = root.get()
        if data is None:
            return {}

        mood = data.get('mood', {})
        mood['night_override'] = data.get('night_override', False)
        return mood
    except Exception as e:
        print(f"⚠️ Error fetching data from Firebase: {e}")
        return {}

# === Main Loop ===
def main():
    last_data = None
    output_path = os.path.abspath(OUTPUT_FILE)
    print(f"💾 Writing to: {output_path}")

    while True:
        data = get_combined_data()

        if data != last_data:
            try:
                with open(output_path, 'w') as f:
                    json.dump(data, f)
                print(f"🔁 Updated mood.json: {data}")
                last_data = data
            except Exception as e:
                print(f"❌ Failed to write to file: {e}")

        time.sleep(POLL_INTERVAL)

# === Run ===
if __name__ == "__main__":
    main()
>>>>>>> eefdd59 (LAYOUT)
