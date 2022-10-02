import cv2
# img = cv2.imread('images/1.png', 1)
# img = cv2.imread('images/1.png', -1)
img = cv2.imread('images/1.PNG', 1)
cv2.imshow('hamzoooz', img)
k  = cv2.waitKey(0)

if k == 27:
    # cv2.destroyAllWindows()
    cv2.imwrite('images/hamzoooz.jpg' , img)
    img = cv2.imread('images/hamzoooz.png', 0)
    cv2.imshow('hamzoooz', img)
    cv2.waitKey(0)
