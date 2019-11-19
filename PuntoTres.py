import firebase_admin
import tkinter as punto_tres
from firebase_admin import credentials
from firebase_admin import db

from pyfirmata import Arduino, util
from tkinter import *
from PIL import Image
from PIL import ImageTk
import time

placa = Arduino ('COM3')
it = util.Iterator(placa)
it.start()
a_0 = placa.get_pin('a:0:i')
a_1 = placa.get_pin('a:1:i')
a_2 = placa.get_pin('a:2:i')
led1 = placa.get_pin('d:8:o')
led2 = placa.get_pin('d:9:p')
led3 = placa.get_pin('d:10:p')
led4 = placa.get_pin('d:11:p')
led5 = placa.get_pin('d:12:o')
led6 = placa.get_pin('d:13:o')
time.sleep(0.5)
ventana = Tk()
ventana.geometry('250x250')
ventana.title("Punto Tres")

# Fetch the service account key JSON file contents
cred = credentials.Certificate('key/key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://parcial-d03bc.firebaseio.com/'
})
def validacion():
    print("Número pin: %s" % int(e1.get()))
    if int(e1.get())<8 & int(e1.get())>13:
        print("Ingrese un número dentro del rango")

def enc_apg():
    print("Número: %s" % int(e2.get()))
    if int(e2.get())<0 & int(e2.get())>1:
        print("Ingrese 0 para apagar y 1 para encender")

master = punto_tres.Tk()
punto_tres.Label(master, 
         text="Número Pin").grid(row=0)

e1 = punto_tres.Entry(master)

e1.grid(row=0, column=1)

punto_tres.Button(master, 
          text='Imprimir', command=validacion).grid(row=3, 
                                                       column=1, 
                                                       sticky=punto_tres.W, 
                                                       pady=4)
punto_tres.Label(master, 
         text="Número:").grid(row=1)

e2 = punto_tres.Entry(master)

e2.grid(row=1, column=1)

punto_tres.Button(master, 
          text='Aceptar', command=enc_apg).grid(row=3, 
                                                       column=5, 
                                                       sticky=punto_tres.W, 
                                                       pady=4)

punto_tres.mainloop()

ventana.mainloop()
