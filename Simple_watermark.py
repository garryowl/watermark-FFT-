import cv2
import numpy as np

img = cv2.imread("origin.jpg")
wm = cv2.imread("watermark.jpg")
img1 = cv2.resize(img,(1435,882))
imgROI = img1[882-wm.shape[0]:882,1435-wm.shape[1]:1435] #注意行列顺序
cv2.addWeighted(imgROI,0.5,wm,0.5,0,imgROI)
cv2.imwrite('output.jpg',img1)
#img:1435*882, wm:443*78