# =================================
# =================================
# import cv2 
# cammera = cv2.VideoCapture(1);
# 
# while (True):
#     ret, frame = cammera.read()
#     cv2.imshow('name of window', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cammera.release()
# cv2.destroyAllWindows()
# 
# =================================
# =================================

import cv2
cammera = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output1.mp4', fourcc, 20.0, (640, 480 ) )
# print((cammera.isOpened()))
while (cammera.isOpened()):
    ret, frame = cammera.read()
    if ret == True:
        # print(cammera.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print(cammera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        
        # # to Convert Images To Gray 
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    
        cv2.imshow('hamzoooz', frame )
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cammera.release()
cammera.release()
cv2.destroyAllWindows()

# =================================
# =================================