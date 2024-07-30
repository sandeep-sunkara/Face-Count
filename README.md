# Face Detection with OpenCV and Dlib

This project captures video from a webcam, detects faces using the Dlib library, and displays the number of faces detected with rectangles drawn around them in real-time.

## Requirements

- Python 3.x
- OpenCV
- Dlib
- NumPy

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/face-detection-opencv-dlib.git
    cd face-detection-opencv-dlib
    ```

2. Install the required packages:
    ```sh
    pip install opencv-python dlib numpy
    ```

## Usage

1. Run the `face_detection.py` script:
    ```sh
    python face_detection.py
    ```

2. The webcam will open, and the script will start detecting faces. To exit, press the `q` key.

## Code Explanation

- **Video Capture**: Initializes the video capture object to capture video from the webcam.
- **Face Detection**: Uses Dlib's `get_frontal_face_detector` to detect faces in the video frames.
- **Drawing Rectangles**: Draws rectangles around detected faces and displays the face count.
- **Exiting**: Press `q` to exit the video capture and close the OpenCV windows.

## Example

When the script is running, it will display the webcam feed with rectangles drawn around detected faces and labels indicating the face count.

![Face Detection Example](example.png
