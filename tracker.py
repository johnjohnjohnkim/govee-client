import cv2
from ultralytics import YOLO

model = YOLO('yolov8s.pt')
model.to('cuda')

camera = cv2.VideoCapture(1)

while camera.isOpened():
    ret, frame = camera.read()

    if not ret:
        break   # No more frames -> exit loop

    detections = model(frame)
    print(detections)

    cv2.imshow("Video", frame)

    # Press Q to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release resources
camera.release()
cv2.destroyAllWindows()