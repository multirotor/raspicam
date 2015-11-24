# import the necessary packages
import cv2
import time
from picamera.array import PiRGBArray
from picamera import PiCamera

# initialize the camera and grab a reference to the raw camera capture
w = 640
h = 480
camera = PiCamera()
camera.resolution = (w, h) 
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(w, h))

end = 0
# keep looping
for image in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    start = end
    end = time.time()
    if start > 0:
        fps = 1.0 / (end - start)
    else:
        fps = 0
    
    frame = image.array

    status = "FPS = " + str(fps)

    # draw the status text on the frame
    cv2.putText(frame, status, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
        (0, 0, 255), 2)

    # show the frame and record if a key is pressed
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

# close camera and any open windows
camera.close()
cv2.destroyAllWindows()

