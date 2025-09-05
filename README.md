# Real-Time-Facial-Emotion-Detection
Real-Time Facial Emotion Detection detects facial expressions
# 🎭 Real-Time Facial Emotion Detection

A Python project that detects **emotions (happy, sad, angry, neutral, surprised, etc.)** from your face in **real-time** using your webcam.  

This project uses **OpenCV** for live video streaming and **FER (Facial Emotion Recognition)** library for emotion classification.  

---

## ✨ Features
- 🎥 **Live webcam feed**  
- 😀 Detects multiple emotions: `happy`, `sad`, `angry`, `surprise`, `fear`, `disgust`, `neutral`  
- 👨‍👩‍👧 Works for multiple faces at once  
- ⚡ Lightweight and runs on CPU (no GPU required)  
- 🖼️ Displays bounding box + emotion label with confidence %  

---

## 🛠️ Tech Stack
- [Python 3.11](https://www.python.org/)  
- [OpenCV](https://opencv.org/) – for real-time video capture  
- [FER](https://github.com/justinshenk/fer) – Facial Emotion Recognition model (Keras-based)  
- [MoviePy](https://zulko.github.io/moviepy/) – required by FER  
---

## 📦 Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/facial-emotion-detection.git
   cd facial-emotion-detection
   Create a virtual environment (recommended):

Create a virtual environment (recommended):

python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/Mac

PROJECT STRUCTURE

facial-emotion-detection/
│── realtime_emotion.py   # Main script
│── requirements.txt      # Dependencies
│── README.md             # Documentation

