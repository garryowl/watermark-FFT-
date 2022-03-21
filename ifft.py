import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('fft+wm(back,edited).jpg',0)
img1 = cv2.imread('origin.jpg',0)
f = np.fft.fft2(img)
f1 = np.fft.fft2(img1)
fshift = np.fft.fftshift(f)
fshift1 = np.fft.fftshift(f1)
fshift[0:78, 0:443] -= fshift1[0:78, 0:443]
fshift[0:78, 0:443] /= 50.0
fshift[-78:, -443:] -= fshift1[-78:, -443:]
fshift[-78:, -443:] /= 50.0
f2 = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f2)
img_back = np.abs(f2)
cv2.imwrite('output.jpg',img_back)