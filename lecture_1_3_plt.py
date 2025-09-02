import cv2
import matplotlib.pyplot as plt


img = cv2.imread('practice_img_lecture1_3.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edge = cv2.Canny(gray, 50 ,150)

plt.subplot(1, 3, 1)
plt.imshow(img_rgb)

plt.subplot(1, 3, 2)
plt.imshow(gray, cmap = 'gray')

plt.subplot(1, 3, 3)
plt.imshow(edge, cmap = 'gray')

plt.tight_layout()
plt.show()