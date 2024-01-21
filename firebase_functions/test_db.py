from datetime import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def get_key(val, response):
   for key, value in response.items():
        print(key, value)



# Fetch the service account key JSON file contents
cred = credentials.Certificate('firebasecreds.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://skilled-nation-396901-default-rtdb.europe-west1.firebasedatabase.app/'
})

# As an admin, the app has access to read and write all data, regardless of Security Rules
ref = db.reference('/')

#get 

nodes_ref = ref.child('third')
nodes_ref = nodes_ref.child('first of third')

response = nodes_ref.get()

print(type(response))
#print(type(ref.get()))
print(response)

print(get_key("{'00:00:00': 'hello world^2'}", response))

