import cv2
import numpy as np

img = cv2.imread('kart.png')
cv2.imshow('Orjinal',img)

width = 400
heigth = 500

#Cevirmek istedigimiz resmin koseleri
pts1 = np.float32([[203,1],[1,472],[540,150],[338,617]])

#Duzlestirmek istedigimiz resmin koseleri
pts2 = np.float32([[0,0],[0,heigth],[width,0],[width,heigth]])

#iki noktasi bilinen transform matrisi olusturma
matrix = cv2.getPerspectiveTransform(pts1,pts2)
print(matrix)

#Cevirme islemi
imgOutput=cv2.warpPerspective(img,matrix,(width,heigth))
cv2.imshow('Nihai Resim',imgOutput)