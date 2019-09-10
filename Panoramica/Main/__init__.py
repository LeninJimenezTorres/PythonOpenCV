#Composición simple de imagen panorámica Python 3 + OpenCV 

import cv2


directorio="C:\\Users\\Lenin\\My Documents\\LiClipse Workspace\\Panoramica\\images\\"
stitcher = cv2.createStitcher(True)

#Abro las imagenes
f1 = cv2.imread(directorio+"1.jpg")
f2 = cv2.imread(directorio+"2.jpg")
f3 = cv2.imread(directorio+"3.jpg")
f4 = cv2.imread(directorio+"4.jpg")

#ejecuto el cosido de imágenes por pixeles afines
result = stitcher.stitch((f1,f2,f3,f4))

#Guardo el resultado 
cv2.imwrite(directorio+"Result.jpg", result[1])

#Abro la imagen guardada 
resultados=cv2.imread(directorio+"Result.jpg")

#Muestro 
cv2.namedWindow('Result', cv2.WINDOW_NORMAL)
cv2.imshow('Result',resultados)
cv2.waitKey(0)
