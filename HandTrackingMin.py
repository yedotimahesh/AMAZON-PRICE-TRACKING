import mediapipe as mp
import cv2

cap=cv2.VideoCapture(0) #Zero Means Webcam
mpHands = mp.solutions.hands
hands= mpHands.Hands()
mpDraw= mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)


            mpDraw.draw_landmarks(img, handLms,mpHands.HAND_CONNECTIONS)



    cv2.imshow("Image" ,img)
    cv2.waitKey(1) 