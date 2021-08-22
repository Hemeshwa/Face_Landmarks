import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)
pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=1)


while True:
    success,img = cap.read()




    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = faceMesh.process(imgRGB)

    if result.multi_face_landmarks:
        for faceLms in result.multi_face_landmarks:
            for id, lm in enumerate(faceLms.landmark):
                print(id,lm)
            mpDraw.draw_landmarks(img,faceLms,mpFaceMesh.FACE_CONNECTIONS)



    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img,f'FPS:{int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,255),3)
    cv2.imshow("IMAGE",img)

    cv2.waitKey(1)


