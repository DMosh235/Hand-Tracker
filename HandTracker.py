# Importing neccesary libraries
import cv2
import mediapipe as mp
import time

# Setting up camera feed
videoCap = cv2.VideoCapture(0)

# Declaring neccesary functions from mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Initializing time values
pTime = 0
cTime = 0

# Loop to execute code
while True:

    # Capturing each frame
    success, frame = videoCap.read()

    # Geting RGB image
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processing RGB image
    results = hands.process(rgb)

    # Checking for multiple hands
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # Placing landmarks and drawing connections
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)

    # Flipping image before dislpay to create mirror effect for webcam use
    img = cv2.flip(frame, 1)

    # Updates time values and calculate framerate
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    # Display framerate as an overlay on screen
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 124), 2)

    cv2.waitKey(1)
    cv2.imshow("Hand Track", img)

    
