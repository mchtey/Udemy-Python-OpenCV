import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('red_blue.jpg')
img_vis = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img_vis)

#Kac piksel var?
print(img.shape)

#Histogram cizimi
img_hist = cv2.calcHist([img],channels=[0],mask=None,histSize=[256],ranges=[0,256])
print(img_hist.shape)
plt.figure(),plt.plot(img_hist)

#Yukaridaki komutta renk ayrimi olmadigi gozlemleniyor
#renk ayrimi uygulama

color = ('b','g','r')
plt.figure()
for i, c in enumerate(color):
    hist=cv2.calcHist([img],channels=[i],mask=None,histSize=[256],ranges=[0,256])
    plt.plot(hist,color=c)
    
    
# Diger bir resime histogram uygulama:
golden_gate = cv2.imread('goldenGate.jpg')
golden_gate_vis = cv2.cvtColor(golden_gate,cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(golden_gate_vis)    
print(golden_gate.shape)

#maske uygulama 
mask = np.zeros(golden_gate.shape[:2],np.uint8)
plt.figure(),plt.imshow(mask,cmap='gray')
#maske icine bir delik uygulanir
mask[1500:2000,1000:2000]=255
plt.figure(),plt.imshow(mask,cmap='gray')

masked_img = cv2.bitwise_and(golden_gate_vis,golden_gate_vis,mask=mask)
plt.figure(),plt.imshow(masked_img,cmap='gray')


#Histogram uygulama:
#channel=[0] kirmiziya denk gelir.
masked_img = cv2.bitwise_and(golden_gate,golden_gate,mask=mask)
masked_img_hist = cv2.calcHist([golden_gate],channels=[0],mask=mask,histSize=[256],ranges=[0,256])
plt.figure(), plt.plot(masked_img_hist)

#mavi renk 
masked_img = cv2.bitwise_and(golden_gate,golden_gate,mask=mask)
masked_img_hist = cv2.calcHist([golden_gate],channels=[2],mask=mask,histSize=[256],ranges=[0,256])
plt.figure(), plt.plot(masked_img_hist)

#yesil renk 
masked_img = cv2.bitwise_and(golden_gate,golden_gate,mask=mask)
masked_img_hist = cv2.calcHist([golden_gate],channels=[1],mask=mask,histSize=[256],ranges=[0,256])
plt.figure(), plt.plot(masked_img_hist)

# Histogram Esitleme
# Karsitlik artirma (kontrasti artirma ile detaylilik artirilir.)

img = cv2.imread('hist_equ.jpg',0)
plt.figure(), plt.imshow(img,cmap='gray')
#resmi siyah beyaz olarak acmak gorselligi icin iyi gelse de islem yapilmali

img_hist = cv2.calcHist([img],channels=[0],mask=None,histSize=[256],ranges=[0,256])
plt.figure(), plt.plot(img_hist)


eq_hist = cv2.equalizeHist(img)
plt.figure(), plt.imshow(eq_hist,cmap='gray')
#renkler arasindaki farklar artmis oldu.

eq_img_hist = cv2.calcHist([eq_hist],channels=[0],mask=None,histSize=[256],ranges=[0,256])
plt.figure(), plt.plot(eq_img_hist)