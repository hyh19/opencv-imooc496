import cv2
import numpy as np

img = cv2.imread('./math.png')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, dst = cv2.threshold(img1, 180, 255, cv2.THRESH_BINARY_INV)
print(dst.shape)

cv2.imshow('img', img)
cv2.imshow('gray', img1)
cv2.imshow('bin', dst)

cv2.waitKey(0)