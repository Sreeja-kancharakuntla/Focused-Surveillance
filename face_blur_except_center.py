import cv2
import numpy as np
import math
import threading
import tkinter as tk

# Calculate Euclidean distance between two points
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Blur all faces except the one closest to the center of the frame
def blur_all_except_closest(frame, faces, center_x, center_y, blur_radius):
    if len(faces) == 0:
        return frame

    height, width = frame.shape[:2]
    distances = []

    # Calculate distances of all faces from the frame center
    for (x, y, w, h) in faces:
        face_center_x = x + w // 2
        face_center_y = y + h // 2
        distance = calculate_distance(face_center_x, face_center_y, center_x, center_y)
        distances.append(distance)

    min_index = distances.index(min(distances))  # Index of the closest face

    for i, (x, y, w, h) in enumerate(faces):
        x1 = max(0, x)
        y1 = max(0, y)
        x2 = min(width, x + w)
        y2 = min(height, y + h)

        if i != min_index:
            face = frame[y1:y2, x1:x2]
            # Ensure kernel size is odd
            kernel = blur_radius if blur_radius % 2 == 1 else blur_radius + 1
            blurred_face = cv2.GaussianBlur(face, (kernel, kernel), 30)
            frame[y1:y2, x1:x2] = blurred_face
        else:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return frame


def main():
    # Initialize video capture
    cap = cv2.VideoCapture(0)
    blur_radius = 21
    if not cap.isOpened():
        print("❌ Error: Could not open webcam.")
        return

    # Load pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Can't receive frame (stream end?). Exiting ...")
            break

        # Detect faces in the frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
       
        # Get center coordinates of the frame
        center_x = frame.shape[1] // 2
        center_y = frame.shape[0] // 2

        frame = blur_all_except_closest(frame, faces, center_x, center_y, blur_radius)
        # Display the resulting frame
        cv2.imshow('Face Blur Within Radius', frame)

        # Break the loop if 'q' is pressed
        key=cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break


        if cv2.getWindowProperty('Face Blur Within Radius', cv2.WND_PROP_VISIBLE) < 1:
            break

    # Release the video capture object
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()