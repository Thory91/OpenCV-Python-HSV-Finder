import numpy as np
import cv2

def nothing(x):
    pass

cv2.namedWindow("Trackbars")
cv2.createTrackbar("L - H", "Trackbars", 0 , 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0 , 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0 , 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179 , 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255 , 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255 , 255, nothing)


cap = cv2.VideoCapture(0)


while(True):
    ret,img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")

    lower_color = np.array([l_h,l_s,l_v])
    upper_color = np.array([u_h,u_s,u_v])
    mask = cv2.inRange(hsv,lower_color,upper_color)
    
    #cv2.imshow('video output', img)
    cv2.imshow('video output', mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

