from os import close
import os
import cv2
import numpy as np
from PIL import Image

molecula = "Butanol"

# Conversion de PNG a JPG

im = Image.open(molecula + ".png")
bg = Image.new("RGB", im.size, (255,255,255))
bg.paste(im,im)
bg.save(molecula + ".jpg")

# Meter la imagen y convertirla a escala de grises

imagen = cv2.imread(molecula + ".jpg")
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY_INV)

# Empezamos con el contorno

contornos,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Contornos : " + str(len(contornos)))

lista_contorno = []
x = 0
while x != len(contornos):
    lista_contorno.append(x)
    x = x + 1
print(lista_contorno)

for valor in lista_contorno:
    color_aleatorio = (list(np.random.choice(range(256), size = 3)))
    color = [int(color_aleatorio[0]), int(color_aleatorio[1]), int(color_aleatorio[2])]
    cv2.drawContours(imagen, contornos, (valor), (color),3)
    valor = valor - 1

print(hierarchy)
file = open("C:/Users/kemen/Desktop/Programacion/Quimica 2.0/Datos de moleculas/" + molecula + ".txt", "w")
file.write("Jerarquia de la molecula " + molecula + " : \n" + str(hierarchy))
file.close()


cv2.imshow("Gray", gray)
cv2.imshow("Thresh", thresh)
cv2.imshow("Imagen", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
