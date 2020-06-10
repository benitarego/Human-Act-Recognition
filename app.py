#import flask libraries
from flask import Flask, render_template, url_for, flash, redirect, Response
from forms import signupform, signinform

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



@app.route('/video_camera')
def video_camera():
    # cap = cv2.VideoCapture('queda.mp4')

    # time.sleep(2)
    
    # fgbg = cv2.createBackgroundSubtractorMOG2()
    # j = 0
    
    # account_sid = 'AC9ff3f227c0a9de0606351f3656ee2274'
    # auth_token = '6eaec067e0c697309716afdc6e1c8a2a'
    # client = Client(account_sid, auth_token)

    # fall=0
    # while(1):
    #     count=0
    #     ret, frame = cap.read()

    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     fgmask = fgbg.apply(gray)

    #     _ , contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #     if contours:
    #         areas = []

    #         for contour in contours:
    #             ar = cv2.contourArea(contour)
    #             areas.append(ar)
        
    #             max_area = max(areas or [0])

    #             max_area_index = areas.index(max_area)

    #             cnt = contours[max_area_index]

    #             M = cv2.moments(cnt)
        
    #             x, y, w, h = cv2.boundingRect(cnt)

    #             cv2.drawContours(fgmask, [cnt], 0, (255,255,255), 3, maxLevel = 0)

    #             if h < w:
    #                 j += 1
            
    #             if j > 10:

    #                 cv2.putText(fgmask, 'FALL', (x, y), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 2)
    #                 cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    #                 print("Fall detected")
    #                 count=1
                
    #             if h > w:
    #                 j = 0 
    #                 cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    #                 fall=0

    #             cv2.imshow('video', frame)
    
    #             if cv2.waitKey(33) == 27:
    #                 break

    #             if count==1 and fall==0:
    #                 message = client.messages.create(
    #                           body='ALERT!!! FALL DETECTED!!!',
    #                           from_='whatsapp:+14155238886',
    #                           to='whatsapp:+919892938847'
    #                       )
    #                 fall=1

    # cap.release()

    # cv2.destroyAllWindows()
    return render_template('viewcamera.html', title='Camera')

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
            u'email': form.email.data,
            u'password': form.password.data
        }
        auth.create_user_with_email_and_password(form.email.data, form.password.data)
        flash(f'You have been logged in', 'success')
        return redirect(url_for('dashboard'))
    else:
        print("Login Unsuccessful. Please check username and password")
    return render_template('login.html', title='Login', form=form)



if __name__=="__main__":
    app.run(debug=True)