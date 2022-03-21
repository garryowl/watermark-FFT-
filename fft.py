import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('origin.jpg',0) #直接读为灰度图像
wm = cv2.imread("watermark.jpg", 0)
wm = 255-wm

f = np.fft.fft2(img) #快速傅里叶变换算法得到频率分布
fshift = np.fft.fftshift(f) #默认结果中心点位置在左上角，转移到中间
#取绝对值：将复数变化成实数
#取对数的目的为了将数据变化到0-255
#fshift是复数，求绝对值结果才是振幅
s1 = np.log(np.abs(fshift))
#求相位，相位和振幅是频域两个很重要的结果
#振幅只是记录图片的明暗，而相位才是记录图像的形状
s1_angle = np.angle(fshift)

#将水印放入频域
fshift2 = fshift.copy()
fshift2[0:78, 0:443] += wm *50.0
fshift2[-78:, -443:] += cv2.flip(wm, -1) *50.0
s2 = np.log(np.abs(fshift2))

# 逆变换
f1shift2 = np.fft.ifftshift(fshift2)
img_back2 = np.fft.ifft2(f1shift2)
#出来的复数，无法显示，转成实数
img_back2 = np.abs(img_back2)

cv2.imwrite('output.jpg',s2)