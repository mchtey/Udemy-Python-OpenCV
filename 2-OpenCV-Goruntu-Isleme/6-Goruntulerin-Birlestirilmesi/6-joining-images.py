import cv2
import numpy as np
# resmi ice aktarma

img = cv2.imread('Lenna.png')
cv2.imshow('Orjinal',img)

# yatay birlestirme
hor = np.hstack((img,img))
cv2.imshow('Horizontal',hor)

# dikey birlestirme
ver = np.vstack((img,img))
cv2.imshow('Vertival',ver)