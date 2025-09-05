import cv2
from fer.fer import FER  # direct import to avoid moviepy dependency

# Initialize detector
detector = FER(mtcnn=False)  # mtcnn=True = more accurate but slower

# Open webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("❌ Cannot access webcam")

while True:
    ok, frame = cap.read()
    if not ok:
        break

    # Flip horizontally (mirror effect)
    frame = cv2.flip(frame, 1)

    # Detect emotions
    results = detector.detect_emotions(frame)

    for r in results:
        (x, y, w, h) = r["box"]
        emotions = r["emotions"]

        # Get dominant emotion
        dominant = max(emotions, key=emotions.get)
        confidence = emotions[dominant]

        # Draw face box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Put label
        cv2.putText(frame, f"{dominant} ({confidence*100:.1f}%)",
                    (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (0, 255, 0), 2, cv2.LINE_AA)

    # Show window
    cv2.imshow("Real-Time Emotion Detector", frame)

    # Press ESC to quit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
