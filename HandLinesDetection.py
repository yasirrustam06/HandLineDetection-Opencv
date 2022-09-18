import cv2
import numpy as np
img=cv2.imread("thumbs_up_down.jpg")

img_Gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,th=cv2.threshold(img_Gray,200,255,cv2.THRESH_BINARY)

contours,hirechy=cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,255,0),3)

cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows()




