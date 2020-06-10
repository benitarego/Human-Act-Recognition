import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("./scripts/benita.json")

default_app firebase_admin.initialize_app(cred)

dv = firestore.client()