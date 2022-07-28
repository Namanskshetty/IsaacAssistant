import cv2
import mediapipe as mp
import time


class FaceDetector():#creating claSS
    def __init__(self, mindet=0.75):# here default confidence is 0.75 which can be changed
        self.mindet=mindet
        self.mpFaceDetection = mp.solutions.face_detection # envoking mediapipe facial detection
        self.mpDraw = mp.solutions.drawing_utils # asking model to draw a axial lines
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.mindet) # seting the confidence score for the facial structure

    def findFaces(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #convering the background color to rgb
        self.results = self.faceDetection.process(imgRGB)# saves the rgb image for the show
        #print(self.results)
        bboxs=[]#list to add the poimnts to get back the bounding box for the faces
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape # Makes the points based on the picture source provided
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih),\
                       int(bboxC.width * iw), int(bboxC.height * ih)
                bboxs.append([id,bbox,detection.score])#appending the score for the box of the face
                if draw:
                    self.fancyDraw(img,bbox)
                    cv2.putText(img, f'Score: {int(detection.score[0]*100)}%', (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN,1, (0, 255, 255), 2)#to check score of the face
        return img, bboxs# it is important to return the image as well asa the bounding box
    def fancyDraw(self,img,bbox,l=30,t=5,rt=1):
        x,y,w,h=bbox
        x1,y1=x+w,y+h

        cv2.rectangle(img, bbox, (255, 0, 255),rt)# ploting rectangle for face
        #top left x,y
        cv2.line(img,(x,y),(x+l,y),(0,255,255),t)#drawing the new line(above)
        cv2.line(img,(x,y),(x,y+l),(0,255,255),t)#drawing the new line(left-above)
        #top right x1,y
        cv2.line(img,(x1,y),(x1-l,y),(0,255,255),t)#drawing the new line(above)
        cv2.line(img,(x1,y),(x1,y+l),(0,255,255),t)#drawing the new line(right-above)
        #bottom left x,y1
        cv2.line(img,(x,y1),(x+l,y1),(0,255,255),t)#drawing the new line(above)
        cv2.line(img,(x,y1),(x,y1-l),(0,255,255),t)#drawing the new line(left-above)
        #bottom right x1,y1
        cv2.line(img,(x1,y1),(x1-l,y1),(0,255,255),t)#drawing the new line(above)
        cv2.line(img,(x1,y1),(x1,y1-l),(0,255,255),t)#drawing the new line(right-above)
        return img

def main(): #if tghere is no code tthis activates
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector=FaceDetector()
    while True:
        success, img = cap.read() # sending the captured file to the class
        img,bbox=detector.findFaces(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,3, (0, 255, 0), 2)
        cv2.imshow("Image", img)
        cv2.waitKey(1)



if __name__=="__main__":#run the dummy code
    main()
