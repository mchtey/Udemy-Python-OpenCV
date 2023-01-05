import cv2
import matplotlib.pyplot as plt

#Karistirma
img1 = cv2.imread('img1.jpg')
#Goruntuyu orjinal renkleri ile acma
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = cv2.imread('img2.jpg')
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)


print(img1.shape)
print(img2.shape)

#Yeniden Boyutlandirma

img1 = cv2.resize(img1,(600,600))
print(img1.shape)

img2 = cv2.resize(img2,(600,600))
print(img2.shape)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#Karistirilmis resim = alpha*img1 + beta*img2

blended = cv2.addWeighted(src1=img1, alpha=0.8, src2=img2, beta=0.8, gamma=0)
plt.figure()
plt.imshow(blended)