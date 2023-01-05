# Video Ice Aktarma:
    
import cv2
import time

video_name = 'MOT17-04-DPM.mp4'

cap = cv2.VideoCapture(video_name)

print('Genislik: ',cap.get(3))
print('Yukseklik: ',cap.get(4))

if cap.isOpened() == False:
  print('Hata')

#Eger iceri aktarma olmadiysa bize uyari vermesini sagliyoruz.,

while True: #read islemi resim acma old. icin surekli hale getirmek gerekiyor.
  ret, frame = cap.read()
  '''
  cap.read islemi basarisiz olursa ret yani return false olarak donecek
  sonraki islemler icin tedbir.
  Eger True ise sorun yok isleme devam edilebilir
  '''
  if ret == True:
    '''
    frame'ler resimelr old. icin art arda hizli gecmesini engellemek icin
    time.sleep kullanilir.
    '''
    time.sleep(0.01) #kullanmaz isek cok hizli akar.
    #video hizi ayarlama
    cv2.imshow('Video',frame)

  else: break  
  
  #Tum videoyu izlemek istemezsek:
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


cap.release() #stop capture
cv2.destroyAllWindows() # tum acik pencereleri kapat