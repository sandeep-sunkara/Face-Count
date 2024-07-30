import cv2
import numpy as np
import dlib

# Initialize the video capture object
video = cv2.VideoCapture(0)

# Create an object for the get_frontal_face_detector() class
detector = dlib.get_frontal_face_detector()

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally

    # Convert the colored image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = detector(gray)

    # Initialize face counter
    num = 0

    for face in faces:
        x, y = face.left(), face.top()
        width, height = face.right() - x, face.bottom() - y
        
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 2)
        
        # Increment the face counter
        num += 1
        
        # Display the face number
        cv2.putText(frame, 'face ' + str(num), (x - 12, y - 12), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # Show the frame with detected faces
    cv2.imshow('faces', frame)
    
    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
video.release()
cv2.destroyAllWindows()
