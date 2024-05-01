import cv2
# Initialize video capture
video_capture = cv2.VideoCapture("D:/walk.mp4") # Replace with your video file
# Initialize background subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2()
while video_capture.isOpened():
    ret, frame = video_capture.read()
    if not ret:
        break
# Apply background subtraction
    fg_mask = bg_subtractor.apply(frame)
# Apply thresholding to get a binary mask
    _, thresh = cv2.threshold(fg_mask, 50, 255, cv2.THRESH_BINARY)
# Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
# Filter contours based on area (adjust the threshold as needed)
        if cv2.contourArea(contour) > 100:
# Draw a bounding box around detected objects or events
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
# Display the processed frame
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release video capture and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
