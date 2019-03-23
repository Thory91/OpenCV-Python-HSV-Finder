import cv2
import numpy as np

cv2.namedWindow("Trackbars")

cv2.createTrackbar("L - H", "Trackbars", 0 , 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0 , 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0 , 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 0 , 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 0 , 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 0 , 255, nothing)

img = cv2.imread("color_sample.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([178,179,0])
upper_red = np.array([255,255,255])
mask = cv2.inRange(hsv, lower_red, upper_red)

while(1):

    
    cv2.imshow('image',img)
    cv2.imshow('hsv',hsv)
    cv2.imshow('mask',mask)
    k = cv2.waitKey(5) & 0xFF
    if(k==27):
        break

cv2.destroyAllWindows()
