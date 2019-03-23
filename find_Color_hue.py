"""IMPORTING THE LIBRARIES for finding color HUES"""
import cv2 
import numpy as np

def nothing(x): #userdata for trackbar purposes.
    pass

#add trackbars to adjust colors of the image(HSV)
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L - H", "Trackbars", 0 , 179, nothing)#adjust H for lower color
cv2.createTrackbar("L - S", "Trackbars", 0 , 255, nothing)#adjust S for lower color
cv2.createTrackbar("L - V", "Trackbars", 0 , 255, nothing)#adjust V for lower color
cv2.createTrackbar("U - H", "Trackbars", 179 , 179, nothing)#adjust H for upper color
cv2.createTrackbar("U - S", "Trackbars", 255 , 255, nothing)#adjust S for upper color
cv2.createTrackbar("U - V", "Trackbars", 255 , 255, nothing)#adjust V for upper color

img = cv2.imread("150_resistor_sample.jpg") #150 ohm resistor image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #change the background color to HSV

while(1):
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")#Get reading of trackbar for lower H
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")#Get reading of trackbar for lower S
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")#Get reading of trackbar for lower V
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")#Get reading of trackbar for upper H
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")#Get reading of trackbar for upper S
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")#Get reading of trackbar for upper V
    
    lower_brown = np.array([l_h,l_s,l_v])#adjust according to HSV settings
    upper_brown = np.array([u_h,u_s,u_v])#adjustable according to HSV settings
    mask = cv2.inRange(hsv, lower_brown, upper_brown)#masking the color that we want to find

    cv2.imshow('image',img)#show the image
    cv2.imshow('mask', mask)#show adjusting HSV color window
    
    k = cv2.waitKey(5) & 0xFF #press ESC to quit the program
    if(k==27):
        break#end the loop of the program.

cv2.destroyAllWindows()#kill all process that is being run by the program
