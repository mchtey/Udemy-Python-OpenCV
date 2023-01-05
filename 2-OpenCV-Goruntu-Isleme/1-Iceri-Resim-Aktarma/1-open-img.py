'''
- Goruntu okuma
- Goruntuleme
- kaydetme
'''
# Iceri Resim Aktarma:
    
import cv2
img = cv2.imread('messi5.jpg',0)
cv2.imshow('Ilk Resim',img)


k = cv2.waitKey(0) &0xFF

if k ==27: #wsc
  cv2.destroyAllWindows()
elif k == ord('s'):
  cv2.imwrite('messi_gray.png',img)
  cv2.destroyAllWindows() 

'''
ESC ye basildiginda cikma ve s ye basildiginda kayıt icin kullanilir.
'''