import numpy as np
import cv2
img = cv2.imread('C:\Users\DELL\Desktop\messi.jpg',1)
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img,'Messi',(410,330), font, 2,(0,0,0),2,cv2.CV_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
