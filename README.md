# Emotion Detector Project

![Emotion Detector](https://img.shields.io/badge/status-completed-brightgreen)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Requests](https://img.shields.io/badge/library-requests-yellow)

---

## Overview

The **Emotion Detector Project** is a Python-based application that uses IBM Watson's Natural Language Processing API to detect emotions from input text. It analyzes the text and predicts emotions such as **joy, anger, sadness, fear,** and **disgust**, providing confidence scores and highlighting the dominant emotion.

This tool can be useful in sentiment analysis, customer feedback interpretation, chatbots, and social media monitoring.

---

## Features

- **Emotion detection** for multiple sentiments in text
- Returns detailed scores for emotions: anger, disgust, fear, joy, sadness
- Identifies and outputs the dominant emotion with the highest confidence score
- Easy to use Python function interface
- Packaged with unit tests for reliable performance

---

## Getting Started

### Prerequisites

- Python 3.11+
- `requests` library (for HTTP requests to IBM Watson API)

Install the `requests` library if you don’t have it:

```bash
pip install requests
How to Run
Clone the repository

bash
Copy
Edit
git clone https://github.com/kishoreb023/emotion_detector_project.git
cd emotion_detector_project
Run emotion detection in Python

Open Python shell or your script and use:

python
Copy
Edit
from emotion_detection import emotion_detector

result = emotion_detector("I love this new technology!")
print(result)
The output will be a dictionary showing scores for all emotions and the dominant emotion.

Project Structure
cpp
Copy
Edit
emotion_detector_project/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── tests/
│   └── test_emotion_detector.py
│
├── static/
│   └── mywebscript.js
│
├── templates/
│   └── index.html
│
├── README.md
├── LICENSE
└── .gitignore
Author
👤 Kishore B
📧 kishoread023@gmail.com
🌐 GitHub Profile

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
IBM Watson Natural Language Understanding API

Coursera Skills Network for project inspiration and rubric
