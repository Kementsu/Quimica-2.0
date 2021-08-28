from os import close, replace, sep
import os
import cv2
from cv2 import data
from matplotlib.ticker import Formatter
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from numpy import array, core
from numpy.lib.shape_base import split
import pandas as pd
from openpyxl import workbook 

molecula = "Butano"

# Conversion de PNG a JPG

im = Image.open(molecula + ".png")
bg = Image.new("RGB", im.size, (255,255,255))
bg.paste(im,im)
bg.save(molecula + ".jpg")

# Meter la imagen y convertirla a escala de grises

imagen = cv2.imread(molecula + ".jpg")
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY_INV)
canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny,None, iterations=1)


# Empezamos con el contorno

contornos,hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
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
    cv2.drawContours(imagen, contornos, (valor), (color),2)
    area = cv2.contourArea(contornos[valor])
    # print(area)
    np.set_printoptions(threshold=np.inf)
    coords = np.array2string(contornos[valor], separator= ",")
    coordenadas_1 = coords.replace("[", "")
    coordenadas_2 = coordenadas_1.replace("]", "")
    coordenadas_3 = coordenadas_2.replace("\n", "")
    coordenadas_4 = coordenadas_3.replace(" ", "")
    coordenadas_datos = []
    
    coordenadas_5 = coordenadas_4.split(",")

    for coordenada_final in coordenadas_5:
        coordenadas_datos.append(coordenada_final)




    # print(coords)
    file = open("C:/Users/kemen/Desktop/Programacion/Quimica 2.0/Datos de moleculas/" + molecula + "_coords.txt", "w")
    file.write("Coordenadas del contorno " + str(valor) + " de la molecula " + molecula + " : " + coords)
    file.close()

    # for coordenada in coords:
        # print(coordenada)

    x_coord = []
    y_coord = []
    for i_0 in range(0, len(coordenadas_datos), 2):
        x_coord.append(coordenadas_datos[i_0])
    for i_1 in range(1, len(coordenadas_datos), 2):
        y_coord.append(coordenadas_datos[i_1])

    # Exportacion a excel

    data = {"x" : x_coord, "y" : y_coord}
    df = pd.DataFrame(data, columns= ["x", "y"])
    df.to_excel("Datos de moleculas\Excel_datos.xlsx")



# Identificacion de cada contorno


# file = open("C:/Users/kemen/Desktop/Programacion/Quimica 2.0/Datos de moleculas/" + molecula + ".txt", "w")
# file.write("Jerarquia de la molecula " + molecula + " : \n" + str(hierarchy))
# file.close()

# plt.plot(x_coord, y_coord)
# plt.show()
# print(x_coord)
print(str(len(contornos)))
cv2.imshow("Gray", gray)
cv2.imshow("Thresh", thresh)
cv2.imshow("Imagen", imagen)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
