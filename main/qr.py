import cv2
import numpy as np
from pyzbar.pyzbar import decode
import webbrowser
import os

#img = cv2.imread('1.png')
d = os.path.dirname(__file__)
#to setup the camera
cam_fol=d+"\\..\\temp\\cam.ttg"
cam_set=open(cam_fol,"r")
inste=str(cam_set.readline())
insta=int(inste)
print(insta)
#to get the pid of the program
PID = str(os.getppid())
fol_pid=d+"\\..\\temp\\qr.pid"# To get teh process id for the qrcode app
rite=open(fol_pid,"w")
rite.write(PID)
rite.close()
#changing the camera
cap = cv2.VideoCapture(insta)
cap.set(3,640)
cap.set(4,480)

while True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        if "http" in myData:
            webbrowser.open(myData)
            exit()
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255,0,255),2)

    cv2.imshow('Result',img)
    cv2.waitKey(1)
