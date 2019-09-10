#Lectura de varias cámaras en ciclo infinito sin control
#OpenCV + Python 3
#Presionar q o Esc para realizar nuevas capturas

import cv2, numpy

puertos=[]
camaras=[]
video=[]
class CamaraSetting:
    def __init__(self, camara, puerto):
        self.puerto=puerto
        self.camara=camara
        puertos.append(puerto)
        camaras.append(camara)
    
    def InformacionGlobal(self):
        print('Camaras')
        for j in range (len (camaras)):
            print(camaras[j])
        print('Puertos')
        for i in range(len(puertos)):
            print(puertos[i])
    
    def InformacionParticular(self):
        print('Camara #:  '+str(self.camara))
        print('Puerto :   '+str(self.puerto))
       
    def SimpleViewer(self):
        video.append(self.camara)
        indice=video.index(self.camara)
        video[indice]= cv2.VideoCapture(self.puerto)
        print('Video '+ str(indice))
        _,im = video[indice].read()
        cv2.imshow('Capure camera '+str(indice), im)
        cv2.waitKey()
        return im
    
 
#Configuración de puertos de las cámaras (Id cámara, puerto cámara)       
camaraFrontal=CamaraSetting(15,0)
camaraLateralDerecha=CamaraSetting(17,1)
camaraLateralIzquierda=CamaraSetting(23,3)

#Esta función muestra la información del Id y del puerto de todas las cámaras
camaraFrontal.InformacionGlobal()

#Al presionar 'q' se realiza una nueva captura. Las capturas son en serie por lo que se realizan consecutivamente
while(True):
    camaraFrontal.InformacionParticular()
    camaraFrontal.SimpleViewer()
    
    camaraLateralDerecha.InformacionParticular()
    camaraLateralDerecha.SimpleViewer()
    
    camaraLateralIzquierda.InformacionParticular()
    ult_im=camaraLateralIzquierda.SimpleViewer()
    
    cv2.imshow('Ultima imagen',ult_im)
    cv2.waitKey(0)
    
    puertos=[]
    camaras=[]
    video=[]
    cv2.destroyAllWindows()
    