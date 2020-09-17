import cv2
import numpy as np

#################################
########## VARIABLES ###########
##############################

drawing = False

ix, iy = -1, -1




###########################
######## Function #########
###########################

# def draw_circle(event,x,y,flags,params):
#     global drawing
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         drawing = True
#         cv2.circle(img, (x,y), 50, (255,255,255),-1)
    # elif event == cv2.EVENT_RBUTTONDOWN:
    #     cv2.circle(img, (x,y), 10, (220,0,0),-1)

def draw_rectangle(event,x,y,flags,params):
    global ix,iy,drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        
        drawing = True
        ix, iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:

        if drawing == True:
            cv2.rectangle(img, (ix,iy),(x,y),(0,255,255),-1,)

    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 50, (255,255,255),-1)


    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix,iy),(x,y),(0,0,255),-1,)

    



cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_rectangle)

###########################
##Show image with opencv ##
###########################

img = np.zeros((800,800,3),np.int8)

while True:
    cv2.imshow('my_drawing',img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()