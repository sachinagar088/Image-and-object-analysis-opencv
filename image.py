import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('C:\Users\DELL\Desktop\messi.jpg',1)
cv2.imshow('football',img)
k=cv2.waitKey(0)
if(k==ord('s')):
	cv2.imwrite('mess1.jpg',img)
	cv2.destroyAllWindows()
else:
	cv2.destroyAllWindows()
"""
using matplotlib printing coloured image 

"""
b,g,r = cv2.split(img)
img2=cv2.merge([r,g,b])
plt.imshow(img2)
plt.show()
