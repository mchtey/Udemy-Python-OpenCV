#Kutuphanelerin yuklenmesi
import cv2
import matplotlib.pyplot as plt

#Resmi ice aktarma
img = cv2.imread('odev1.jpg',0)
cv2.imshow('Odev1',img)

#Resmin boyutlarina bakma
print(img.shape)
# (568,860)

# Resmi yeniden boyutlandirma (4/5) oraninda 
imgBoyutlandirma = cv2.resize(img, int(img.shape[1]*4/5), int(img.shape[0]*4/5))
cv2.imshow('Yeni Boyut: ',imgBoyutlandirma)

# Orjinal resme yazi ekleme
cv2.putText(img, 'kedi', (625,150),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0))
cv2.imshow('kedi Yazisi',img)

# thresh = 50 altindakiler siyah, uzerindekiler beyaz olacak sekilde binary threshold uygulama
_, thresh_img = cv2.threshold(img, thresh=50, maxval=255, type=cv2.THRESH_BINARY)
cv2.imshow('Threshold', thresh_img)

#Orjinal resme Gaussian Gradyan uygulama
gb = cv2.GaussianBlur(img,ksize=(3,3), sigmaX=7)
cv2.imshow('Gaussian Blur',gb)

#Orjinal resme Laplacian Gradyan uygulama:
laplacian_img = cv2.Laplacian(img,ddepth=cv2.CV_64F)
cv2.imshow('Laplacian',laplacian_img)

#Orjinal resmin histograminin cizilmesi
hist_img = cv2.calcHist([img], channels=[0],mask=None, histSize=[256], ranges=[0,256])
plt.figure()
plt.plot(hist_img)