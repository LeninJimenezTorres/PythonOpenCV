#Aplicación para visualizar varias cámaras empleando hilos o multiprocesamiento
#OpenCV + Python3
#Las capturas se realizan de manera simultánea, guarda los frames y los abre

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
def Destroy(nombre,numero):
    ima=cv2.imread(carpetaFrames+'F'+str(numero)+'.jpg')
    cv2.imshow(nombre,ima)
    cv2.waitKey()
    cont=0
    while cont<=50:#Delay
        cont=cont+1
    print('Cerrando ventana : '+str(nombre)) 
    cv2.destroyWindow(nombre)
    
def Camaras(puertoC, fotograma):
    Videos=cv2.VideoCapture(puertoC)
    while True:
        rev,im=Videos.read()
        if rev:                    
            im=cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            cv2.imwrite(carpetaFrames+'F'+str(fotograma)+'.jpg',im)     
            Videos.release()
            break
    nombre='Imagen '+str(fotograma)
    hiloAux=threading.Thread(target=Destroy,args=(nombre,fotograma,))
    hiloAux.start()
    
if __name__=='__main__':
    puertos=[4, 2, 0]
    print('Cantidad de camaras:   '+str(len(puertos)))
    print('Arranca')
    Hilos=[None]*len(puertos)
    while True:
        a=False
        while a!=True:
            for i in range(len(puertos)):
                Hilos[i]=threading.Thread(target=Camaras(puertos[i], i))
                Hilos[i].start()

            a=True            
            break