#Aplicación para una cámara Tkinter
#OpenCV + Python3
import numpy as np
import cv2

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


#***********************************************************************************************************************************************************************************    
class AppCamara:
    def __init__(self, ventanaVideo, titulo, puerto): #, serial_source=PuertoArduino):
        self.window = ventanaVideo
        self.window.title(titulo)
        self.puerto = puerto
        
        self.window.minsize(640,480)
        self.window.configure(background='gray10')
    
         
        self.imagenRecivida = CamaraSetting(self.puerto)  
        self.canvas = tk.Canvas(ventanaVideo, width = self.imagenRecivida.width, height = self.imagenRecivida.height)
        self.canvas.place(x=0, y=0)
        
        self.delay = 10
        self.update()
        
        self.window.mainloop()
    
           
    def update(self):
        # Get a frame from the video source
        ok, captura = self.imagenRecivida.Captura()

        if ok:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(captura))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)
            self.window.after(self.delay, self.update)

class CamaraSetting:
    def __init__(self, puerto):
        self.puerto=puerto
        puertos.append(puerto)
        
        self.prelectura = cv2.VideoCapture(puerto)
        self.width = self.prelectura.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.prelectura.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
    def InformacionParticular(self):
        print('Puerto :   '+str(self.puerto))
           
    def Captura(self):
        if self.prelectura.isOpened(): 
            video.append(len(cam))
            video[len(cam)]= cv2.VideoCapture(self.puerto)
            rev,im = video[len(cam)].read()
        
            cam.append(1)
        
            #rev,im=self.prelectura.read()
            if rev:
                return (rev,cv2.cvtColor(im, cv2.COLOR_BGR2RGB))#IMPORTANTE _______________
            else:
                return (rev, None)
            self.prelectura.release()
        else:
            return (rev, None)
        
        
    def __del__(self):
        if self.prelectura.isOpened():
            self.prelectura.release()
        
    

AppCamara(tk.Tk(), "Interface Usuario",1)
