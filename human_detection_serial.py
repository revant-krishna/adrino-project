import cv2
import time
import winsound  # For playing beep sound on Windows

# No serial communication needed for inbuilt sound

# Load pre-trained Haar Cascade for human detection
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("[ERROR] Could not open webcam.")
else:
    print("[INFO] Webcam opened successfully.")

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Failed to grab frame from webcam.")
        break
    # Resize for faster detection
    frame = cv2.resize(frame, (640, 480))
    # Detect people in the frame
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8))
    # Draw bounding boxes
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    if len(boxes) > 0:
        print(f"[INFO] Detected {len(boxes)} human(s) in frame.")
    # If any humans detected, play a beep sound
    if len(boxes) > 0:
        print("[ACTION] Human detected! Playing beep sound on laptop.")
        winsound.Beep(2000, 1000)  # Beep at 2000 Hz for 1 sec
        time.sleep(1)  # Avoid spamming sound
    cv2.imshow('Human Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
