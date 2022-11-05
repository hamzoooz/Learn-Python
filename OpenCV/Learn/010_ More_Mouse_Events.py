import numpy as np 
import cv2 
# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('images/1.PNG')

print(img.shape) # returens a tuple of number 



cv2.imshow('hamzoooz', img)

cv2.waitKey(0)
# # Close All Windows
cv2.destroyAllWindows()

