import cv2
import numpy as np

#resim olustur:
img = np.zeros((512,512,3),np.uint8) # siyah bir resim
print(img.shape)
cv2.imshow('Siyah',img)

#Cizgi Olustur:
#(resim,baslangic_noktasi,bitis_noktasi,renk,kalinlik)
cv2.line(img, (290,300),(100,300),(0,255,0),3) #BGR = (0,255,0) -yesil
cv2.imshow('Cizgi',img)

#Dikdortgen Cizme:
#(resim,baslangic,bitis)
cv2.rectangle(img,(0,0),(256,256),(150,60,50),cv2.FILLED)
cv2.imshow('dikdortgen',img)

#Cember Cizme:
# (resim,merkez,yaricap,renk)
cv2.circle(img,(300,300),45,(0,0,255),cv2.FILLED)
cv2.imshow('Cember',img)

#Metin
# (resim,baslangic,font,kalinlik,renk)
cv2.putText(img,'Yazilar',(350,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.imshow('Metin',img)