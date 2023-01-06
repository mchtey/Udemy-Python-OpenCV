import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')

#Blurring: detayi azaltir, gurultuyu engeller

img = cv2.imread('NYC.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img), plt.axis('off'), plt.title('Orjinal'), plt.show()


'''
Ortalama Bulaniklastirma Yontemi
'''

dst2 = cv2.blur(img, ksize = (3,3))
plt.figure(), plt.imshow(dst2), plt.axis('off'), plt.title('Ortalama Blur')

'''
Gaussian Blur
'''

gb = cv2.GaussianBlur(img, ksize = (3,3),sigmaX = 7)
plt.figure(), plt.imshow(gb), plt.axis('off'), plt.title('Gaussian Blur')


'''
Median Blur
'''
mb = cv2.medianBlur(img, ksize = 3)
plt.figure(), plt.imshow(mb), plt.axis('off'), plt.title('Median Blur')

'''
Noise ihtiyac var.
filtrelerin ise yaradigini gormek icin asagidaki def yaziliyor.
'''

def gaussianNoise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    
    return noisy

# Gurultuyu eklemek icin normalizasyon yapmamiz gerekli
# Orjinal goruntu degerlerini 0-1 arasinatasiyacagiz
img = cv2.imread('NYC.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255
plt.figure(), plt.imshow(img), plt.axis('off'), plt.title('Orjinal'), plt.show()

gaussianNoisyImage = gaussianNoise(img)
plt.figure(), plt.imshow(gaussianNoisyImage), plt.axis('off'), plt.title('Gaussian Noisy'), plt.show()


# Gaussian Noise elde ettik simdi bunu azaltacagiz
# Gaus Blur

gb2 = cv2.GaussianBlur(gaussianNoisyImage, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gb2), plt.axis('off'), plt.title('With Gauss Blur')

#Tuz karabiber gürültü uygulama

def saltPapperNoise(image):
    row,col,ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy = np.copy(image) #orjinalin yedegi
    
    #salt beyaz
    num_salt = np.ceil(amount * image.size * s_vs_p) #ceil ondalikli sayiyi yukari ya da asagi yuvarlar
    #beyaz gurultunun koordinatlarini belirleme
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy[coords] = 1 #beyazin karsiligi 1
    
    #papper siyah
    num_pepper = np.ceil(amount * image.size * (1 - s_vs_p)) #ceil ondalikli sayiyi yukari ya da asagi yuvarlar
    #beyaz gurultunun koordinatlarini belirleme
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy[coords] = 0 #siyahin karsiligi 0
    
    return noisy


spImage = saltPapperNoise(img)
plt.figure(),plt.imshow(spImage), plt.axis('off'), plt.title('SP Image')

#Simdi bu tuz biberlerden kurtulalim:
mb2 = cv2.medianBlur(spImage.astype(np.float32), ksize = 3)
plt.figure(), plt.imshow(mb2), plt.axis('off'), plt.title('with Median Blur')

#Sonuc olarak Noise azaltiyor ama detay da azalmis oluyor.