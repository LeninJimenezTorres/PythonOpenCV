#Imagen panorámica Python 3 + OpenCV + Ajuste de bordes

import cv2
import imutils
import numpy as np

#Dirección de imagenes 
directorio="C:\\Users\\Lenin\\My Documents\\LiClipse Workspace\\Panoramica\\images\\"
extension=".jpg"

#Creo el objeto de reconstrucción pannorámica
stitcher = cv2.createStitcher(True)

#Abro las imágenes
f1 = cv2.imread(directorio+'1.jpg')
f2 = cv2.imread(directorio+'2.jpg')
f3 = cv2.imread(directorio+'3.jpg')
f4 = cv2.imread(directorio+'4.jpg')

#Reconstruyo la imagen panorámica
result = stitcher.stitch((f1,f2,f3,f4))

#Guardo
cv2.imwrite(directorio+"Result.jpg", result[1])

#Abro el resultado
resultados=cv2.imread(directorio+"Result.jpg")
cv2.namedWindow('Result', cv2.WINDOW_NORMAL)
cv2.imshow('Result',resultados)

#Creo una copia para poder modificar la imagen sin alterar la original
stitched=cv2.copyMakeBorder(resultados,10, 10, 10, 10,cv2.BORDER_CONSTANT, (0, 0, 0))
gray = cv2.cvtColor(stitched, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Gray', cv2.WINDOW_NORMAL)
cv2.imshow('Gray',gray)

#Identifico los bordes irregulares de la imagen aplicando un filtro de umbral
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]
cv2.namedWindow('Umbral', cv2.WINDOW_NORMAL)
cv2.imshow('Umbral',thresh)

#Encuentro los contornos de la imagen para borrar los excedentes
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts, key=cv2.contourArea)

#Identifico pixeles negros o en bit 0
mask = np.zeros(thresh.shape, dtype="uint8")
(x, y, w, h) = cv2.boundingRect(c)
cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

minRect = mask.copy()
sub = mask.copy()

pixelesNegros=cv2.countNonZero(sub)
print('Valor ceros= '+str(pixelesNegros))

#Aplico filtro de erosión para borrar los pixeles negros
while pixelesNegros>0:
    #i=0
    #while i<100: 
    minRect = cv2.erode(minRect, None)
    sub= cv2.subtract(minRect, thresh)
    #    i=i+1
        
    pixelesNegros=cv2.countNonZero(sub)
    print('Valor cerosNuevos= '+str(pixelesNegros))

cv2.namedWindow('Sub', cv2.WINDOW_NORMAL)
cv2.imshow('Sub',sub)


#Encuentro los límites internos de la imagen sin bordes con error
cnts = cv2.findContours(minRect.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts, key=cv2.contourArea)
(x, y, w, h) = cv2.boundingRect(c)

#Extraigo esa imagen 
stitched = stitched[y:y + h, x:x + w]

#Guardo
cv2.imwrite("C:\\Users\\Lenin\\My Documents\\LiClipse Workspace\\Panoramica\\images\\Final.jpg", stitched)

#Muestro la imagen con ajuste de borde
cv2.namedWindow('Final', cv2.WINDOW_NORMAL)
cv2.imshow("Final", stitched)

cv2.waitKey(0)
