#Visor de varias cámaras OpenCV + Python3
# Presionar Esc para terminar programa 

import numpy as np
import cv2

puertos=[]
camaras=[]
video=[]
SimpleCap=[]
cam=[]
capturas=[]

class CamaraSetting:
    def __init__(self, puertos):
        self.puertos=puertos
        self.prelectura=[]
        for i in range (len(puertos)):                   
            self.im=cv2.VideoCapture(puertos[i])
            self.prelectura.append(self.im)
            self.width = self.im.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.height = self.im.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print('Ancho = '+str(self.width))
        print('Alto = '+str(self.height))
        
    def InformacionParticular(self):
        for j in range (len(puertos)):
            print('Puerto '+str(j)+'  :   '+str(self.puertos[j]))
            
    def Captura(self):
        
        for a in range(len(puertos)):     
            self.videoTurno=cv2.VideoCapture(self.puertos[a])
            #print('Puerto '+str(puertos[a])+'  ______abierto')
            
            self.rev,self.im=self.videoTurno.read()
            
            if self.rev:
                #print('Captura realizada')
                global capturas
                capturas.append(self.im);
                #cv2.imshow('Captura Actual',capturas[a])
                #cv2.waitKey()
            else:
                return (self.rev, None)
            
            #self.videoTurno.release()
            
        if a>=len(puertos):
            a=0


#Introducir los puertos______________________________________________________________________________
puertos=[1, 4, 2]
WebCams=CamaraSetting(puertos)
print('Cantidad de camaras:   '+str(len(puertos)))
WebCams.InformacionParticular()

WebCams.Captura()

while True:     
    for i in range (len(capturas)):
        cv2.imshow('Captura '+str(i)+' ',capturas[i])
    
    tecla = cv2.waitKey(10)
    if tecla == 27:
        break
    
    if len(capturas)>=len(puertos):#IMPORTANTE_____LIMPIAR ARRAY Y DEJARLO EN CERO_________
        capturas.clear()
        capturas=[]
        
    WebCams.Captura()
    #print('Cantidad de capturas:   '+str(len(capturas)))

