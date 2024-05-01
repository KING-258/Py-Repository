import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

prev_x = None
prev_y = None

while cap.isOpened():
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            pinky_mcp = landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP]
            
            x, y = int(index_tip.x * frame.shape[1]), int(index_tip.y * frame.shape[0])

            if prev_x is not None and prev_y is not None:
                dx = x - prev_x
                dy = y - prev_y

                if abs(dx) > abs(dy):
                    if dx > 50:
                        print('Right')
                    elif dx < -50:
                        print('Left')
                else:
                    if dy > 50:
                        print('Down')
                    elif dy < -50:
                        print('Up')

            prev_x = x
            prev_y = y

    cv2.imshow("Gesture Recognition", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
