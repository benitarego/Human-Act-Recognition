import cv2
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC9ff3f227c0a9de0606351f3656ee2274'
auth_token = '6eaec067e0c697309716afdc6e1c8a2a'
client = Client(account_sid, auth_token)


face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
ds_factor=0.6

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        fgbg = cv2.createBackgroundSubtractorMOG2()
        j = 0        
        fall=0
        while(1):
            count=0
            ret, frame = self.video.read()
            if ret:
                ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
            #Conver each frame to gray scale and subtract the background
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            fgmask = fgbg.apply(gray)
            #Find contours
            #_ , contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            contours, hierarchy = cv2.findContours(fgmask, 
            cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
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
                cv2.drawContours(fgmask, [cnt], 0, (255,255,255), 3, 
                maxLevel = 0)
                if h < w:
                    j += 1
            
                if j > 10:
                    cv2.putText(fgmask, 'FALL', (x, y), 
                    cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 2)
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
                    body='ALERT!!! FALL DETECTED! Please call 102 immeditately',
                    from_='whatsapp:+14155238886',
                    to='whatsapp:+919892938847'
                    )
                    fall=1
