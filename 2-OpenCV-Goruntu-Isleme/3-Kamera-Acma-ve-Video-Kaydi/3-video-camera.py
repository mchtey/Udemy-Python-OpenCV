import cv2

#capture
cap = cv2.VideoCapture(0)
#harici kamera takilirsa 0 iki kamera varsa 0 ya da 1 hangisi kullanilacaksa o yazilir.
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width,height)

#Video kaydet:
writer = cv2.VideoWriter('video_kayit.mp4',cv2.VideoWriter_fourcc(*'DIVX'),20,(width,height))
# 20 video akisinin hizi. Frame per second
# fourcc cerceveleri sikistirma icin kullanilir.
# DIVX microsoft icin kullanilir.

while True:
    ret, frame = cap.read()
    cv2.imshow('Video',frame)
    
    #save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF ==ord('q'): break

cap.release()
writer.release()
cv2.destroyAllWindows()