import numpy as np
import cv2
import time

cap0 = cv2.VideoCapture(0)
cap0.set(3, 2560)
cap0.set(4, 720)

#cap1 = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame0 = cap0.read()
    #time.sleep(1)
    ret, frame1 = cap0.read()


    # Our operations on the frame come here
    gray0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    #Make difference image
    dif = cv2.absdiff(frame1,frame0)


    # Display the resulting frame
    #cv2.imshow('frame0',gray0)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break
    #cv2.imshow('frame1',gray1)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break
    cv2.imshow('dif',dif)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    


# When everything done, release the capture
#cap0.release()
#cap1.release()
dif.release()
cv2.destroyAllWindows()
