import pyrebase

config = {
    "apiKey": "AIzaSyC-O7rEAWRj17u1IHaidphx-yDUaQijjv0",
    "authDomain": "citi-1df6c.firebaseapp.com",
    "databaseURL": "https://citi-1df6c.firebaseio.com",
    "projectId": "citi-1df6c",
    "storageBucket": "citi-1df6c.appspot.com",
    "messagingSenderId": "478029708540",
    "appId": "1:478029708540:web:f4f0dc3585309a8b96eb79"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

email = input("Enter email\n")
password = input("Enter password\n")

user = auth.create_user_with_email_and_password(email, password)

auth.get_account_info(user['idToken'])