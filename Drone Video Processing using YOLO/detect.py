import cv2
import os
from app.detector import detect_objects
from app.summarizer import generate_summary

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("❌ Error: Cannot open video file")
        return

    print("✅ Video loaded successfully!")

    # 🎥 Create outputs folder
    os.makedirs("outputs", exist_ok=True)

    # 🎥 Video properties
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = int(cap.get(cv2.CAP_PROP_FPS)) or 30

    # ⚠️ Windows-safe codec (VERY IMPORTANT)
    output_path = "outputs/output.avi"
    fourcc = cv2.VideoWriter_fourcc(*"XVID")

    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    if not out.isOpened():
        print("❌ VideoWriter failed!")
        return

    print("🎬 Saving video...")

    frame_count = 0
    max_frames = 300   # ~10 seconds video

    while frame_count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # 🔍 Detection
        results, counts = detect_objects(frame)
        caption = generate_summary(counts)

        # 🟩 Draw bounding boxes
        for box in results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = results[0].names[int(box.cls[0])]
            conf = float(box.conf[0])

            if conf < 0.3:
                continue

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            text = f"{label} {conf:.2f}"
            cv2.putText(frame, text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (0, 255, 0), 2)

        # 🔴 Add summary text
        cv2.putText(frame, caption, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (0, 0, 255), 2)

        # 💾 Save frame
        out.write(frame)

        # 📊 Progress
        if frame_count % 30 == 0:
            print(f"Processing frame {frame_count}...")

    # 🔚 Release
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print("🎬 Video processing completed!")
    print(f"✅ Output saved at: {output_path}")


if __name__ == "__main__":
    process_video("input/sample_video.mp4")