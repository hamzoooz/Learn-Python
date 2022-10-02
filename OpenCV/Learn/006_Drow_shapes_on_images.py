import cv2 
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(1)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH ))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGT ))

cap.set( 3, 120 )

cv2.imshow('006_Drow_shapes_on_images.py', img)
# To Keep Window Opened
cv2.waitKey(0)
# Close All Windows
cv2.destroyAllWindows()