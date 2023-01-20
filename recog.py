import cv2
import mediapipe as mp
import time

cam_source = cv2.VideoCapture(0)  # capture_vedio
mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils
pTime=0     #previous time
cTime = 0   #current time

while True:
    success, img = cam_source.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    hand_landmarks = results.multi_hand_landmarks

    if hand_landmarks:
        for handLms in hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
        # print landmark cordinates
                # if id==0:
                #     print('{')
                #     print(f'{id}--> ({cx},{cy})')
                #     continue
                # if id==20:
                #     print(f'{id}--> {cx} , {cy}')
                #     print("}")
                #     continue
                # print(f'{id}--> {cx} , {cy}')

                if id ==4 or id==8 or id==12 or id==16 or id==20:
                    cv2.circle(img, (cx, cy),8, (106,219,247), cv2.FILLED)

                if id ==0 or id==5 or id==9 or id==13 or id==17:
                    cv2.circle(img, (cx, cy), 8, (217, 250, 32), cv2.FILLED)
                    # cv2.circle(Img, center_coordinates, radius, color, thickness)

            mpdraw.draw_landmarks(img, handLms, mphands.HAND_CONNECTIONS,
            landmark_drawing_spec=mpdraw.DrawingSpec(color=(255,255,255), thickness=1, circle_radius=1),
            connection_drawing_spec=mpdraw.DrawingSpec(color=(52, 49, 46), thickness=2, circle_radius=1),)

# finding the FPS     
#    {
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX , 3,(255, 0, 255), 2)
#    }


    cv2.imshow("Image", img)
    cv2.waitKey(1)