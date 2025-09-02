import cv2


img = cv2.imread('practice_img_lecture1_3.jpg')
cv2.imshow('Origin image', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray image', gray)

edge = cv2.Canny(gray, 50, 150)
cv2.imshow('edge image', edge)

cv2.waitKey(0)
cv2.destroyAllWindows()


# pip install opencv-python
# pip install matplotlib