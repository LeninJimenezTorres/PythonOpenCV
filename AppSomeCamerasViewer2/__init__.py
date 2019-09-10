#Aplicación 2 para visualizar varias cámaras en Python 3 + OpenCV + Tkinter


import numpy as np
import cv2,time
import ctypes #Para ver tamaño de pantalla

import tkinter as tk
from tkinter import *
from tkinter import messagebox, PhotoImage, Label, image_types, Image, ttk, Canvas,Frame,BOTH
import PIL.Image
import PIL.ImageTk
from PIL import Image, ImageTk

from tkinter.test.support import destroy_default_root
from threading import Thread, Lock


puertos=[]
camaras=[]
video=[]
SimpleCap=[]
cam=[]
capturas=[]

carpetaFrames='C:\\Users\\Lenin\\Documents\\PythonProyects\\Clases\\AppCamerasViewer\\'

anchoPantalla=1920
altoPantalla=1080

#Tipos de letras*******************************************************************************************
font_s = 'Times 16 bold'#italic
font_titulo='Times 14 bold'
font_texto='Times 12'

#***********************************************************************************************************************************************************************************    

def InfoPantalla():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    global anchoPantalla, altoPantalla
    anchoPantalla, altoPantalla = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    print(anchoPantalla, altoPantalla)
      
class Interface:
    def __init__(self, titulo,puertos):
        self.ventana= Tk()
        self.titulo=titulo
        self.ventana.title(titulo)
        self.ventana.configure(background='black')
        self.puertos=puertos
        self.alturaMin=480
        self.anchoMin=640
        self.altoMax=altoPantalla
        self.anchoMax=anchoPantalla
        self.ventana.minsize(self.anchoMax,self.alturaMin+100)
        self.ventana.maxsize(width=self.anchoMax, height=900)
        
        self.nuevoAncho=round(int(self.anchoMax/len(puertos)))
        
        print('Numero de camaras = '+str(len(self.puertos)))
        
        self.achoTotal=self.anchoMin*len(puertos)
        self.Cerrar=tk.Button(self.ventana,text="Cerrar",bg="SlateGray4",fg="black",font=font_titulo,command=self.Close).place(x=(self.anchoMax/2)-15,y=490)
             
        self.imagenes=[]
        self.Espacios=[]
        self.frames=[]
        self.Videos=[]
        self.Img=[]
          
        self.delay=20
        self.Imagenes()
                
        self.ventana.mainloop()
    
    def Limpiar(self):
        self.Espacios.clear()
        self.frames.clear() 
        self.Espacios=[]
        
    def Imagenes(self):       
        self.frames=[]
        self.Espacios=[]
        #Videos=[]
        for i in range(len(puertos)):
            #Videos.append(cv2.VideoCapture(puertos[i]))
            #Videos[i]=cv2.VideoCapture(puertos[i])
            Video=cv2.VideoCapture(puertos[i])
            while True:
                self.rev,self.im=Video.read()
                if self.rev:                    
                    self.im=cv2.cvtColor(self.im, cv2.COLOR_BGR2RGB)
                    #cv2.imwrite(carpetaFrames+'F'+str(i)+'.png',self.im)     
                    Video.release()
                    #Videos[i].release()
                    break
            #self.frames.append(i)
            #self.frames[i]=PIL.ImageTk.PhotoImage(file=carpetaFrames+'F'+str(i)+'.png')
            self.frames.append(i)
            self.frames[i]=ImageTk.PhotoImage(PIL.Image.fromarray(self.im))
            self.Espacios.append(i)
            self.Espacios[i]=Label(self.ventana, image=self.frames[i]).place(x=self.nuevoAncho*i,y=0)     
        self.ventana.after(self.delay, self.Imagenes)
    def Close(self):
        self.ventana.destroy()

if __name__=='__main__':
    InfoPantalla()
    puertos=[4, 2, 1]
    print('Cantidad de camaras:   '+str(len(puertos)))
    
    Interface('Monitor Central',puertos)