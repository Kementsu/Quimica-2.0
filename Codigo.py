# Importacion de modulos
import cv2
import matplotlib.pyplot as plt
import pytesseract
from pytesseract.pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
# Lectura de imagen mediante OpenCV
img = cv2.imread("Butanol.jpg")
# Conversion a escala de grises
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# En este paso hay que convertirla a una imagen binaria, este paso es obligatorio si la imagen es a color, en nuestro caso no lo sera.
# El comando seria el siguiente : 
threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) [1]
# Mostrar la imagen
cv2.imshow('threshold image', threshold_image)
# Manteneer la ventana abierta hasta que se toque una tecla
cv2.waitKey()
# Destruir las ventanas actuales en la pantalla
cv2.destroyAllWindows()

# En este momento los pixeles blancos estan bien separados, por lo cual seria mas facil de detectar