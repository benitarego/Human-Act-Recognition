#Based on Zed code - Person Fall detection using raspberry pi camera and opencv lib. Link: https://www.youtube.com/watch?v=eXMYZedp0Uo

import cv2
import time

cap = cv2.VideoCapture('queda.mp4') #'queda.mp4'

#To set the resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

time.sleep(2)

fgbg = cv2.createBackgroundSubtractorMOG2()
j = 0
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC9ff3f227c0a9de0606351f3656ee2274'
auth_token = '6eaec067e0c697309716afdc6e1c8a2a'
client = Client(account_sid, auth_token)

# message = client.messages.create(
#                               body='ALERT!!! FALL DETECTED!!!',
#                               from_='whatsapp:+14155238886',
#                               to='whatsapp:+917977032378'
#                           )

fall=0
while(1):
    count=0
    ret, frame = cap.read()
    
    #Conver each frame to gray scale and subtract the background
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fgmask = fgbg.apply(gray)
    
    #Find contours
    #_ , contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        areas = []

        for contour in contours:
            ar = cv2.contourArea(contour)
            areas.append(ar)
        
        max_area = max(areas or [0])

        max_area_index = areas.index(max_area)

        cnt = contours[max_area_index]

        M = cv2.moments(cnt)
        
        x, y, w, h = cv2.boundingRect(cnt)

        cv2.drawContours(fgmask, [cnt], 0, (255,255,255), 3, maxLevel = 0)
        
        if h < w:
            j += 1
            
        if j > 10:

            cv2.putText(fgmask, 'FALL', (x, y), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 2)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            print("Fall detected")
            count=1
            # print(message.sid)

        if h > w:
            j = 0 
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            fall=0


        cv2.imshow('video', frame)
    
        if cv2.waitKey(33) == 27:
            break

        if count==1 and fall==0:
            message = client.messages.create(
                              body='ALERT!!! FALL DETECTED! Please call 102 immediately',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+919892938847'
                          )
            fall=1

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

cap.release()

cv2.destroyAllWindows()