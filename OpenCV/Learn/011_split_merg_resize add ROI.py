import numpy as np 
import cv2 

def click_event( event, x ,y ,flags, param ): 
  if event == cv2.EVENT_LBUTTONDOWN :
      cv2.circle(img, (x,y), 3,(0,0,255), -1)
      points.append((x, y))
      if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255,255,0),5)
      # font = cv2.FONT_HERSHEY_SIMPLEX
      # strXY = str(x) + ' , ' + str(y)
      # cv2.putText(img, strXY , (x, y), font, .5, (0, 255, 0 ), 2 )
      cv2.imshow('hamzoooz', img )
  
img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('hamzoooz', img)
points = []
cv2.setMouseCallback('hamzoooz', click_event )

cv2.waitKey(0)
# # Close All Windows
cv2.destroyAllWindows()

