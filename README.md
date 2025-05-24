# Focused-Surveillance
This project uses real-time video processing to enhance privacy by blurring all detected faces in a webcam feed except the one closest to the center of the frame. Leveraging OpenCV and Haar cascade classifiers, it dynamically detects multiple faces, computes their distance from the frame's center, and applies a Gaussian blur to all except the most central face. This approach is useful for surveillance, video conferencing focus, and privacy-preserving applications, ensuring attention remains on the main subject while anonymizing others.

# Face Blur Except Center

This project uses OpenCV and Python to blur all detected faces in a webcam video stream **except** the one **closest to the center** of the frame. It’s a real-time computer vision application demonstrating facial detection, distance computation, and selective blurring.

## 🎯 Features

- Real-time face detection using Haar cascades
- Calculates the center of the video frame
- Blurs all faces **except** the one nearest to the center
- Optionally draws bounding boxes around faces
  - Green for the unblurred (central) face
  - Red for blurred faces

## 📦 Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy

## 🔧 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/face-blur-except-center.git
   cd face-blur-except-center
2. Install dependencies
    pip install opencv-python numpy
3. Run the script
    python face_blur_except_center.py

# How It Works
- Captures video stream from the default webcam
- Detects faces in each frame
- Calculates the Euclidean distance from each face to the center of the frame
- Blurs all faces **except** the one with the minimum distance
- Displays output in a real-time window

# Real-Time Use Cases
1. Targeted Surveillance in Public Places
    - Use: Automatically highlight and monitor a specific individual (e.g., nearest to the camera) while anonymizing others.
    - Where: Airports, train stations, shopping malls, etc.
    - Benefit: Protects the privacy of bystanders while enabling focused tracking.

2. Interview Recording or Video Calls
    - Use: Emphasize the main speaker and blur everyone else.
    - Where: Panel interviews, online meetings, group discussions.
    - Benefit: Keeps the focus on the presenter or respondent for better clarity and privacy.

3. News and Journalism
    - Use: Capture video from crowded events while ensuring the anonymity of non-consenting individuals.
    - Where: Protests, rallies, political events. 
    - Benefit: Ethical reporting with respect for public privacy laws.

4. Smart Classrooms and Lecture Recording
    - Use: Focus on the lecturer or a student presenting, while blurring others.
    - Where: Schools, online education platforms.
    - Benefit: Enhances the viewer’s focus and protects student identities.

5. Retail Stores and Customer Analysis
    - Use: Study customer behavior or expressions without revealing other shoppers.
    - Where: Showrooms, supermarkets.
    - Benefit: Helps in consumer research without violating privacy.

6. Security Footage Sharing
    - Use: Share security footage with authorities or public while blurring unrelated people.
    - Where: Apartment buildings, ATMs, private properties.
    - Benefit: Prevents unnecessary exposure of individuals not involved in incidents.

7. Automated Test Proctoring
    - Use: Focus on the test-taker and blur surroundings.
    - Where: Online exam portals.
    - Benefit: Prevents cheating while ensuring privacy of the environment.

# Notes
Press q to quit the program (or) simply press the window close button 
You can adjust the blur radius and detection sensitivity by modifying the code.

# Future Improvements
- Add GUI to configure radius or toggle modes

- Support image and video file input

- Integration with deep learning face detectors for better accuracy


Developed by Sreeja Kancharakuntla


Let me know if you want me to customize the GitHub repo link, add a license section, or include a video demo badge.

