import cv2
import mediapipe as mp
import time
class FaceMeshDetector():
    def __init__(self,staticMode=False,maxFaces=2,minDetection=0.75,minTrackCon=0.75):#the confidence num,ber cannoty be dtermined with avilable version of media pipe
        self.staticMode=staticMode
        self.maxFaces=maxFaces
        self.minDetection=minDetection
        self.minTrackCon=minTrackCon
        self.mpDraw = mp.solutions.drawing_utils#helps draw on faces
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode,self.maxFaces)#""",self.minDetection,self.minTrackCon""" zthe string  verfies the confidence confidence in the face please makle sure to add
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=2)# the drawing part on the face

    def findFaceMesh(self,img, draw=True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        faces=[]
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS,self.drawSpec,self.drawSpec)#Face_connections changed its name to facemesh_contors
                face=[]

                for id,lm in enumerate(faceLms.landmark):
                    #print(lm)
                    ih, iw, ic = img.shape
                    x,y = int(lm.x*iw), int(lm.y*ih)
                    #cv2.putText(img, str(id), (x,y), cv2.FONT_HERSHEY_PLAIN,0.5, (0,254,0), 1) #if you wish to see the points on the face be sure to uncomment ther this line

                    #print(id,x,y)
                    face.append([x,y])
                faces.append(face)
        return img,faces
def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    Detector=FaceMeshDetector()
    while True:
        success, img = cap.read()
        img,faces=Detector.findFaceMesh(img)
        if len(faces)!=0:
            print(faces[0])
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,3, (255, 0, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
if __name__=="__main__":
    main()
