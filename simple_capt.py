import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 2560)
cap.set(4, 1080)
#cvSetCaptureProperty(cap, CV_CAP_PROP_FRAME_WIDTH, 640)
#cvSetCaptureProperty(cap, CV_CAP_PROP_FRAME_HEIGHT, 480)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
