import cv2

img = cv2.imread('lenna.png')
print('Resim Boyutu:',img.shape)
cv2.imshow('Orjinal',img)

#Yeniden Boyutlandirma:
imgResized = cv2.resize(img,(100,100))
print('Resized Img Shape: ',imgResized)
cv2.imshow('Img Resized',imgResized)


# Kirpma:
imgCropped = img[:200,:300] # --> once height sonra width gelir
cv2.imshow('Kirpilmiş Resim: ',imgCropped)