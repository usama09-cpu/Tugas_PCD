import cv2
import numpy as np

img = cv2.imread("usama1.jpeg")
img_1 = cv2.resize(img, (560, 340))
gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar Usama Original", img_1)
cv2.imshow("Gambar Usama GraScale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()