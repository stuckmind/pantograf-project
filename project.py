import cv2
import time

# Path to your video file
video_path = 'video.mp4'

# Open the video capture
cap = cv2.VideoCapture(video_path)

# Initialize variables
start_time = time.time()
frame_count = 0
blue_roi = (100, 400, 600, 200)  # Define blue ROI (x, y, width, height)
red_roi = (400, 100, 100, 200)   # Define red ROI (x, y, width, height)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_count += 1
    elapsed_time = time.time() - start_time
    
    # Extract ROIs
    blue_frame = frame[blue_roi[1]:blue_roi[1] + blue_roi[3], blue_roi[0]:blue_roi[0] + blue_roi[2]]
    red_frame = frame[red_roi[1]:red_roi[1] + red_roi[3], red_roi[0]:red_roi[0] + red_roi[2]]
    
    # Draw rectangles around ROIs
    cv2.rectangle(frame, (blue_roi[0], blue_roi[1]), (blue_roi[0] + blue_roi[2], blue_roi[1] + blue_roi[3]), (255, 0, 0), 2)  # Blue
    cv2.rectangle(frame, (red_roi[0], red_roi[1]), (red_roi[0] + red_roi[2], red_roi[1] + red_roi[3]), (0, 0, 255), 2)  # Red
    
    # Display speed information
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (255, 255, 255)
    font_thickness = 2
    speed_text = f"Speed: {frame_count / elapsed_time:.2f} FPS"
    cv2.putText(frame, speed_text, (10, 30), font, font_scale, font_color, font_thickness)
    
    # Display labels above ROIs
    label_font_scale = 0.8
    label_font_color = (0, 255, 0)  # Green color
    cv2.putText(frame, "Pantograf", (blue_roi[0], blue_roi[1] - 10), font, label_font_scale, label_font_color, font_thickness)
    cv2.putText(frame, "Kabel Kereta", (red_roi[0], red_roi[1] - 10), font, label_font_scale, label_font_color, font_thickness)
    
    # Display frame
    cv2.imshow('Video Player', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    if elapsed_time > 1:  # Print speed every 1 second
        frame_count = 0
        start_time = time.time()

cap.release()
cv2.destroyAllWindows()
