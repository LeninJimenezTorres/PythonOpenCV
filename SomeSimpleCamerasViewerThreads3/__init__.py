#Aplicación para visualizar varias cámaras empleando hilos o multiprocesamiento
#OpenCV + Python3
#Las capturas se realizan de manera simultánea, optimizado pero se satura la memoria

import numpy as np
import cv2,time
from tkinter.test.support import destroy_default_root
from threading import Thread, Lock
import threading
import multiprocessing 

import sys
from platform import release

puertos=[]
camaras=[]
video=[]
SimpleCap=[]
cam=[]
capturas=[]

all_processes = [] 
numeros=0
#***********************************************************************************************************************************************************************************    
def DestroyComplete(puertos,imagenes):
    for i in range(len(puertos)):
        cv2.imshow('Puerto '+str(i),imagenes[i])
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Kill(nombre):
    time.sleep(0.5)
    cv2.destroyWindow(nombre)
    print('Cerrando ventana : '+str(nombre)) 
    
def Destroy(nombre,imagen):
    cv2.namedWindow(nombre,cv2.WINDOW_NORMAL)
    cv2.imshow(nombre,imagen)
    hiloKill=threading.Thread(target=Kill,args=(nombre,),)
    cv2.waitKey()
    hiloKill.start()            
    hiloKill.join()
    #cv2.destroyWindow(nombre)
    
def Camaras(CamAbierta, fotograma):
    while True:
        ok,im=CamAbierta.read()
        if ok:
            Imagenes[fotograma]=im
            Videos[fotograma].release()
            hiloAux=threading.Thread(target=Destroy,args=(str(fotograma),im,),)
            hiloAux.start()
            break
        hiloAux.join()
        
def Captura(puertos):
    
    for i in range(len(puertos)):
        Videos[i]=cv2.VideoCapture(puertos[i])
        HilosB[i]=threading.Thread(target=Camaras,args=(Videos[i],i,),)
        HilosB[i].start()
        #HilosB.join()    
        
        #HilosB[i]=multiprocessing.Process(target=Camaras,args=(Videos[i],i,))
        
        #HilosB[i].start()
        
        #all_processes.append(HilosB[i])
            
    for j in range (len(puertos)):
    #HilosB.join()    
    #HilosB._stop()
        HilosB[j].join()
    c=threading.active_count()
    d=threading.enumerate()
    print('Hilos Corriendo: '+str(c))
    print('D=: '+str(d))

    
if __name__=='__main__':
    puertos=[1, 2]
    Imagenes=[None]*len(puertos)
    Hilos=[None]*len(puertos)
    HilosB=[None]*len(puertos)
    Videos=[None]*len(puertos)

    print('Cantidad de camaras:   '+str(len(puertos)))
    print('Arranca')
    Hilos=[None]*len(puertos)
    while True:
        Captura(puertos)

        #threading._shutdown() 
        #Thread._stop(self)
        #getting.start()
            