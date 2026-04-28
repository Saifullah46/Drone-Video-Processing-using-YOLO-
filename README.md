<img width="1366" height="693" alt="Screenshot 2026-04-28 121525" src="https://github.com/user-attachments/assets/c1dcee89-3e76-49f2-960d-6856e5915172" /># Drone Video Processing using YOLO (FREE AI Version )

## 📌 Overview

This project processes drone footage using **YOLOv8** to detect objects such as animals, vehicles, and humans, and generates real-time insights **without using any paid APIs**.

The system outputs a processed video with bounding boxes, labels, and AI-generated summaries — making it suitable for real-world applications like agriculture monitoring, surveillance, and traffic analysis.

---

## 🎯 Features

* 🎯 Object Detection using YOLOv8
* 📊 Real-time object counting
* 🧠 AI-like summary generation (Rule-based, no API cost)
* 🎥 Video processing with bounding boxes & labels
* 💾 Saves processed output video
* ⚡ Beginner-friendly & fully offline

---

## 🧠 Tech Stack

* Python
* OpenCV
* YOLOv8 (Ultralytics)
* NumPy

---

## 🏗️ Project Structure

```bash
Drone-Video-Processing-YOLO-Free/
│
├── app/
│   ├── detector.py
│   ├── summarizer.py
│
├── input/
│   └── sample_video.mp4
│
├── outputs/
│   └── output.avi
│
├── detect.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/drone-video-yolo.git
cd drone-video-yolo

python -m venv .venv
.venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

---

## ▶️ Usage

1. Add your video inside the `input/` folder
2. Rename it to:

```bash
sample_video.mp4
```

3. Run the project:

```bash
python detect.py
```

---

## 📁 Output

Processed video will be saved in:

```bash
outputs/output.avi
```

### Output includes:

* 🟩 Bounding boxes
* 🏷 Object labels with confidence
* 🔴 AI-generated summary text

---

## 🧠 How It Works

```
Input Video
   ↓
YOLOv8 Detection
   ↓
Object Counting
   ↓
Rule-Based AI Summary
   ↓
OpenCV Video Rendering
   ↓
Output Video
```

---

## 💡 Key Highlight

👉 This project **eliminates dependency on paid APIs** by implementing a rule-based AI summarization system.

---

## ⚠️ Limitations

* Detection accuracy depends on YOLO model
* Processing may be slow on low-end systems
* Rule-based AI is simpler than advanced LLMs

---

## 🚀 Future Improvements

* 🌐 Web App (Flask / Streamlit)
* 🎥 Real-time webcam detection
* 📊 Dashboard for analytics
* 🔥 Instagram Reel-style output
* 🧠 Integration with local LLMs

---

## 📸 Demo ( output )

<img width="1366" height="693" alt="Screenshot 2026-04-28 121525" src="https://github.com/user-attachments/assets/3a2d9b79-f0f9-4b27-a3be-098725afec26" />



---

## 👤 Author

**Saifullah S**
B.Tech – Artificial Intelligence & Data Science



