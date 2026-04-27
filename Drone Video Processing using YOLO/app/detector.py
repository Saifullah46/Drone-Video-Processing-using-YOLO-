from ultralytics import YOLO

model = YOLO("yolov8x.pt")

def detect_objects(frame):
    results = model(frame, verbose=False)
    counts = {}

    for box in results[0].boxes:
        label = results[0].names[int(box.cls[0])].lower()
        conf = float(box.conf[0])

        if conf < 0.3:
            continue

        counts[label] = counts.get(label, 0) + 1

    return results, counts
