import cv2
import torch
from ultralytics import YOLO
import sys

# Use CUDA only if an NVIDIA GPU is available, otherwise fall back to CPU
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Using device: {device}")

model = YOLO('yolov8s.pt')
model.to(device)

if 'darwin' in sys.platform: #For my own quick testing, macbook vs PC
    camera = cv2.VideoCapture(0)
elif 'win32' in sys.platform:
    camera = cv2.VideoCapture(1)

while camera.isOpened():
    ret, frame = camera.read()
    if not ret:
        break

    # Run inference
    results = model.track(frame, stream=True)

    for r in results:
        annotated_frame = r.plot()
        
        # Display the annotated frame instead of the raw one
        cv2.imshow("Video", annotated_frame)

    if cv2.waitKey(25) & 0xFF == ord('q'): # Changed to 1ms delay for smoother live video
        break

# Release resources
camera.release()
cv2.destroyAllWindows()