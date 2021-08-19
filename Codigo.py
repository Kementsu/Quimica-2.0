import cv2
import numpy as np

imagen = cv2.imread("Butanol.jpg")
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_,th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

contornos,hierarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Contornos : " + str(len(contornos)))

cv2.drawContours(imagen, contornos, 0, (0,255,0),3)
cv2.drawContours(imagen, contornos, 1, (255,0,0),3)
cv2.drawContours(imagen, contornos, 2, (0,0,255),3)

print(hierarchy)

cv2.imshow('Th', th)
cv2.imshow("Imagen", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
