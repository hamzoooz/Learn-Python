import datetime
import cv2 
# cap = cv2.imread('images/hamzoooz.png' , 1)
cap = cv2.VideoCapture(0)

# cap.set(3, 3000)
# cap.set(4, 3000)
while (cap.isOpened() ):
      ret, frame = cap.read()
    #   gray = cv2.cvbtColor(frame, cv2.COLOR_BGR2GRAY )
    #   cv2.imshow('hamzoooz', gray)
      font = cv2.FONT_HERSHEY_SIMPLEX
      text = 'Width : ' + str(cap.get(3)) + ' Height : ' + str(cap.get(4)) 
      datet = str(datetime.datetime.now())
    #   frame = cv2.putText(frame, text , (10, 50), font, 1, (0, 255, 0 ), 2 , cv2.LINE_AA )
      frame = cv2.putText(frame, datet , (10, 50), font, 1, (0, 255, 0 ), 2 , cv2.LINE_AA )
      cv2.imshow('hamzoooz', frame)
      
      if cv2.waitKey(0) & 0xFF == ord('q'):
          break
      else:
          break
cv2.release()
# Close All Windows
cv2.destroyAllWindows()

