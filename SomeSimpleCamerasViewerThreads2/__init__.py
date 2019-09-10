#Aplicación para visualizar varias cámaras empleando hilos o multiprocesamiento
#OpenCV + Python3
#Las capturas se realizan de manera simultánea, No guarda los frames


import numpy as np
import cv2,time
from tkinter.test.support import destroy_default_root
from threading import Thread, Lock
import threading

puertos=[]
camaras=[]
video=[]
SimpleCap=[]
cam=[]
capturas=[]

carpetaFrames='C:\\Users\\Lenin\\Documents\\PythonProyects\\Clases\\SomeSimpleCamerasViewer\\'

#***********************************************************************************************************************************************************************************    
def Destroy(nombre,imagen):
    cv2.imshow(nombre,imagen)
    cv2.waitKey(0)
    print('Cerrando ventana : '+str(nombre)) 
    cv2.destroyWindow(nombre)
    
def Camaras(puertoC, fotograma):
    Videos=cv2.VideoCapture(puertoC)
    #cont=0
    while True:
        rev,im=Videos.read()
        if rev:                    
            Videos.release()
            break
        #cont=cont+1
    nombre='Imagen '+str(fotograma)
    hiloAux=threading.Thread(target=Destroy,args=(nombre,im,))
    hiloAux.start()
    
if __name__=='__main__':
    puertos=[1, 2]
    print('Cantidad de camaras:   '+str(len(puertos)))
    print('Arranca')
    Hilos=[None]*len(puertos)
    while True:
        for i in range(len(puertos)):
            Hilos[i]=threading.Thread(target=Camaras(puertos[i], i))
            Hilos[i].start()
   