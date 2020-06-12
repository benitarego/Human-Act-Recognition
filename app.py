#import flask libraries
from flask import Flask, render_template, url_for, flash, redirect, Response
from forms import signupform, signinform
from camera import VideoCamera

#import firebase
from google.cloud import storage
from firebase import firebase
from firebase_admin import credentials, firestore
import firebase_admin
from firebase_admin import db
import firebase
import os
import pyrebase

#import python libraries
import cv2
import time
import camera
from twilio.rest import Client

config = {
    "apiKey": "AIzaSyC-O7rEAWRj17u1IHaidphx-yDUaQijjv0",
    "authDomain": "citi-1df6c.firebaseapp.com",
    "databaseURL": "https://citi-1df6c.firebaseio.com",
    "projectId": "citi-1df6c",
    "storageBucket": "citi-1df6c.appspot.com",
    "messagingSenderId": "478029708540",
    "appId": "1:478029708540:web:f4f0dc3585309a8b96eb79"
}

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./scripts/benita.json"
cred = credentials.Certificate("./scripts/benita.json")

firebase_admin.initialize_app(
    cred, {"databaseURL": "https://citi-1df6c.firebaseio.com/"}
)

app = Flask(__name__)
app.config['SECRET_KEY']= '374189861e417d9b5a953831473505f6'

db = firestore.client()

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/dashboard')
def dashboard():
    # form = signupform()
    # form1 = signinform()
    return render_template('dashboard.html', title='Dashboard')



@app.route('/viewcamera/', methods=['POST'])
def viewcamera():
    view_message = "Updating profile..."
    return render_template('viewcamera.html', forward_message=view_message)


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')




@app.route("/update/", methods=['POST'])
def update_profile():
    update_message = "Updating profile..."
    return render_template('dashboard.html', forward_message=update_message)



@app.route("/register", methods=['GET','POST'])
def register():
    form = signupform()
    if form.validate_on_submit():
        register = {
            u'iname': form.iname.data,
            u'dob': str(form.dob.data),
            u'address': form.address.data,
            u'uname': form.uname.data,
            u'relation': form.relation.data,
            u'contact': form.contact.data,
            u'email': form.email.data,
            u'password': form.password.data
        }
        db.collection(u'signup').document(register['iname']).set(register)
        auth.create_user_with_email_and_password(form.email.data, form.password.data)
        flash(f'Account created for {form.uname.data}!','success')
        return redirect(url_for('dashboard'))
    else:
        print("Not registered")
        # return redirect(url_for('register'))
    return render_template('register.html', title='Register', form=form)



@app.route('/login', methods=['GET','POST'])
def login():
    form = signinform()
    if form.validate_on_submit():
        login = {
            u'uname': form.uname.data,
            u'email': form.email.data,
            u'password': form.password.data
        }
        auth.sign_in_with_email_and_password(form.email.data, form.password.data)
        flash(f'You have been logged in {form.uname.data}!', 'success')
        return redirect(url_for('dashboard'))
    else:
        print("Login Unsuccessful. Please check username and password")
        # flash(f'Invalid login. Register!', 'danger')
        # return redirect(url_for('login'))
    return render_template('login.html', title='Login', form=form)



if __name__=="__main__":
    app.run(debug=True)