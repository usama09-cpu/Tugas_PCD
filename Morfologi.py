import cv2 as cv2
import numpy as np
# import matplotlib.pyplot as plt

# Original
img = cv2.imread("usama1.jpeg")
imo = cv2.resize(img, (560, 340))
cv2.imshow("Original", imo)
cv2.waitKey(0)
kernel= np.ones((5,5),np.uint8)

# Erosion
erosion = cv2.erode(imo,kernel,iterations = 1)
# ime = cv2.resize(img, (560, 340))
cv2.imshow("Erosion", erosion)
cv2.waitKey(0)

# Dilation
dilation = cv2.dilate(imo,kernel,iterations = 1)
cv2.imshow("Dilasi", dilation)
cv2.waitKey(0)

# Opening
kernel1 = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(imo, cv2.MORPH_OPEN, kernel1)
cv2.imshow('opening', opening)
cv2.waitKey(0)

# Closing
closing = cv2.morphologyEx(imo, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing", closing)
cv2.waitKey(0)

# Gradient
gradient = cv2.morphologyEx(imo, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Gradient", gradient)
cv2.waitKey(0)