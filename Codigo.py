from PIL import Image
import cv2
from matplotlib.pyplot import close, gray
import numpy as np

# Conversion y escala de grises
image = cv2.imread("Hexane.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gradientes en las direcciones x e y
gradX = cv2.Sobel(gray, cv2.CV_32F, dx = 1, dy = 0, ksize = -1)
gradY = cv2.Sobel(gray, cv2.CV_32F, dx = 0, dy = 1, ksize = -1)

gradiente = cv2.subtract(gradX, gradY)
gradiente = cv2.convertScaleAbs(gradiente)

# Visualizado de imagen 
cv2.imshow("First", gradiente)
cv2.waitKey()

# Eliminacion de ruido (la foto acojona que flipas)
blurred = cv2.blur(gradiente, (9,9))
_, thresh = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresh", thresh)
cv2.waitKey()

# Algun retoque mas

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25,25))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closed1", closed)
cv2.waitKey()

# Creo que queda peor, lo de arriba, lo veremos mas tarde

closed = cv2.erode(closed, None, iterations = 4)
closed = cv2.dilate(closed, None, iterations = 4)
cv2.imshow("Closed2, closed")
cv2.waitKey()

x = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
_a, cnts, _b = x
c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
rect = cv2.minAreaRect(c)
box = np.int0(cv2.boxPoints(rect))
cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
cv2.imshow("Image", image)
cv2.imwrite("Contours Image2.jpg", image)
cv2.waitKey()

Xs = [i[0] for i in box]
Ys = [i[1] for i in box]
x1 = min(Xs)
x2 = max(Xs)
y1 = min(Ys)
y2 = max(Ys)
hight = y2 - y1
width = x2 - x1
cropImg = image[y1:y1+hight, x1:x1+width]

cv2.imshow("CropImg", cropImg)
cv2.imwrite("Final", cropImg)
cv2.waitKey()
