import cv2 
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(1)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH ))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT ))

cap.set( 3, 120 )
cap.set( 4, 720 )
while ( cap.isOpened()):
    ret, frame = cap.read()
    if ret == True: 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
        cv2.imshow('006_Drow_shapes_on_images.py', cap )
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    else:
        break
cap.release()
# Close All Windows
cv2.destroyAllWindows()