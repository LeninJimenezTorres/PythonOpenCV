#Aplicación para visualizar varias cámaras en Python 3 + OpenCV + Tkinter

import numpy as np
import cv2,time

import tkinter as tk
from tkinter import *
from tkinter import messagebox, PhotoImage, Label, image_types, Image, ttk, Canvas,Frame,BOTH
import PIL.Image
import PIL.ImageTk

from tkinter.test.support import destroy_default_root

from threading import Thread, Lock


puertos=[]
camaras=[]
video=[]
SimpleCap=[]
cam=[]
capturas=[]

carpetaFrames='C:\\Users\\Lenin\\Documents\\PythonProyects\\Clases\\AppSomeCamerasViewer\\'

#Tipos de letras*******************************************************************************************
font_s = 'Times 16 bold'#italic
font_titulo='Times 14 bold'
font_texto='Times 12'

#***********************************************************************************************************************************************************************************    
        
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
                #self.im=cv2.cvtColor(self.im, cv2.COLOR_BGR2RGB)
            
                global capturas
                capturas.append(self.im);
                cv2.imwrite(carpetaFrames+'Frame_'+str(a)+'.jpg',capturas[a])     

            else:
                return (self.rev, None)
            self.videoTurno.release()
            
        if a>=len(puertos):
            #capturas.clear()
            a=0

def limpiar():
    global capturas
    capturas.clear()
    capturas=[]


class Interface:
    def __init__(self, titulo,puertos):
        self.ventana= Tk()
        self.titulo=titulo
        self.ventana.title(titulo)
        self.ventana.configure(background='black')
        self.puertos=puertos
        self.alturaMin=480
        self.anchoMin=640
        self.anchoMax=1500
        self.ventana.minsize(self.anchoMax,self.alturaMin+100)
        self.ventana.maxsize(width=self.anchoMax, height=900)
        #self.ventana.resizable(width=False, height=False)
        
        self.nuevoAncho=round(int(self.anchoMax/len(puertos)))
        
        print('Numero de camaras = '+str(len(self.puertos)))
        
        self.achoTotal=self.anchoMin*len(puertos)
        self.Cerrar=tk.Button(self.ventana,text="Cerrar",bg="SlateGray4",fg="black",font=font_titulo,command=self.Close).place(x=(self.anchoMax/2)-15,y=490)
               
        self.imagenes=[]
        self.Espacios=[]
        self.frames=[]
        
        self.WebCams=CamaraSetting(puertos)
        self.WebCams.Captura()
            
        print('Numero de capturas= '+str(len(capturas)))
    
        self.delay=60
        self.Imagenes()
        
        self.ventana.mainloop()
        
    def Imagenes(self):   
        for i in range (len(capturas)):
            self.ima=capturas[i]
            #self.ima=cv2.resize(self.ima,(self.nuevoAncho,self.alturaMin))
            
            self.imagenes.append(self.ima)
            self.frames.append(i)
            self.frames[i]=PIL.ImageTk.PhotoImage(file=carpetaFrames+'Frame_'+str(i)+'.jpg')
            
            
            self.Espacios.append(i)
            self.Espacios[i]=Label(self.ventana, image=self.frames[i]).place(x=self.nuevoAncho*i,y=0)
  
        limpiar()
        self.WebCams.Captura()  

        
        self.ventana.after(self.delay, self.Imagenes)
    
    def Close(self):
        self.ventana.destroy()


if __name__=='__main__':
        
    puertos=[1, 4, 2]
    print('Cantidad de camaras:   '+str(len(puertos)))
    
    Interface('Monitor Central',puertos)