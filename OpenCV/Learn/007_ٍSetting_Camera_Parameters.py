import cv2 
img = cv2.imread('images/hamzoooz.png' , 1)

# Draw Line 
img = cv2.line(img, (0, 0), (255, 255, ), (147, 96, 44), 10 )

# Draw Arrow 
img = cv2.arrowedLine(img, (10, 300), (255, 255), (255, 0, 0 ), 10 )

# Deow rectangle
img  = cv2.rectangle(img , (384 ,0 ), (510, 120 ), (0, 0 , 255, 0), 10 )

# Drow circle 
img  = cv2.circle(img , (447,0 ), 63, (0, 255, 0),  -1 )

# Put Text in Image
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'hamzoooz', (10,500), font, 4, (0, 255, 255), 10, cv2.LINE_AA )

# To Show Image
cv2.imshow('006_Drow_shapes_on_images.py', img)
# To Keep Window Opened
cv2.waitKey(0)
# Close All Windows
cv2.destroyAllWindows()