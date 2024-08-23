import cv2
import mediapipe as mp
mp_face_mesh = mp.solutions.face_mesh
cap = cv2.VideoCapture(0)
with mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            continue
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                landmarks = face_landmarks.landmark
                height, width, _ = frame.shape
                left_eye = (int(landmarks[362].x * width), int(landmarks[362].y * height))
                right_eye = (int(landmarks[133].x * width), int(landmarks[133].y * height))
                left_cheek = (int(landmarks[234].x * width), int(landmarks[234].y * height))
                right_cheek = (int(landmarks[454].x * width), int(landmarks[454].y * height))
                chin = (int(landmarks[152].x * width), int(landmarks[152].y * height))
                cv2.line(frame, left_eye, chin, (255, 255, 255), 2)
                cv2.line(frame, right_eye, chin, (255, 255, 255), 2)
                cv2.line(frame, left_cheek, chin, (255, 255, 255), 2)
                cv2.line(frame, right_cheek, chin, (255, 255, 255), 2)
                cv2.line(frame, left_cheek, left_eye, (255, 255, 255), 2)
                cv2.line(frame, right_cheek, right_eye, (255, 255, 255), 2)
                cv2.circle(frame, left_eye, 5, (0, 0, 255), -1)
                cv2.circle(frame, right_eye, 5, (0, 0, 255), -1)
                cv2.circle(frame, left_cheek, 5, (0, 0, 255), -1)
                cv2.circle(frame, right_cheek, 5, (0, 0, 255), -1)
                cv2.circle(frame, chin, 5, (0, 0, 255), -1)
        cv2.imshow('Face Mesh', frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()