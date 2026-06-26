import cv2
import torch
from ultralytics import YOLO

# Use CUDA only if an NVIDIA GPU is available, otherwise fall back to CPU
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Using device: {device}")

model = YOLO('yolov8s.pt')
model.to(device)

camera = cv2.VideoCapture(0)

while camera.isOpened():
    ret, frame = camera.read()
    if not ret:
        break

    # Run inference
    results = model(frame, stream=True)

    for r in results:
        annotated_frame = r.plot()
        
        # Display the annotated frame instead of the raw one
        cv2.imshow("Video", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # Changed to 1ms delay for smoother live video
        break

# Release resources
camera.release()
cv2.destroyAllWindows()