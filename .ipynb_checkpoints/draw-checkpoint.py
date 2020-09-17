import cv2
import numpy as np


###########################
######## Function #########
###########################

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 5, (255,255,255),-1)

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_circle)

###########################
##Show image with opencv ##
###########################

img = np.zeros((800,800,3),np.int8)

while True:
    cv2.imshow('my_drawing',img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()