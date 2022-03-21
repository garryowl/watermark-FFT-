import cv2
import numpy as np

img = cv2.imread("origin.jpg")
wm = cv2.imread("watermark.jpg")
wm2 = cv2.resize(wm,(img.shape[1],img.shape[0]))

s_black = wm2[:,:]<128
wm2[s_black] = 1
s_white = wm2[:]>=128
wm2[s_white] = 0
r = img.shape[0]
c = img.shape[1]
t255 = np.ones((r, c, 3), dtype=np.uint8)*254 #获取前7位数据
demo_h7 = np.bitwise_and(img, t255)
demo_s_in = np.bitwise_or(demo_h7, wm2)

t1 = np.ones((r, c, 3), dtype=np.uint8)
s_out = np.bitwise_and(demo_s_in, t1)
s_out_white = s_out[:]<1
s_out[s_out_white] = 255
s_out = cv2.resize(s_out, (wm.shape[1],wm.shape[0]))
cv2.imwrite('output.jpg', s_out)