import firebase_admin
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

Frame1 = Frame(ventana, bg="gray", highlightthickness=1, width=1280, height=800, bd= 5)
Frame1.place(x = 0,y = 0)

valor= Label(Frame1, bg='cadet blue1', font=("Arial Bold", 15), fg="black", width=5)
adc_data=StringVar()
valor2= Label(Frame1, bg='cadet blue1', font=("Arial Bold", 15), fg="black", width=5)
adc_data2=StringVar()
valor3= Label(Frame1, bg='cadet blue1', font=("Arial Bold", 15), fg="black", width=5)
adc_data3=StringVar()
variable=StringVar()



def entrada():
    x=input("Numero de pin")
    print("Número pin: %s\n" % (x.get())
    if x>=8 & x<=13:
              print("x")
          else:
              print("Debe ingresar un número dentro del rango")
          


    #def clicked():
 #   valor.configure(text="Se presionó el boton!")
    
#valor=Label(ventana,textvariable=variable)
#valor.place(x=20, y=90)
#btn=Button(ventana,text="start",command=clicked, font=("Times new roman", 10))
#btn.place(x=20, y=120)

    
valor.configure(textvariable=variable)
valor.place(x=20, y=30)
start_button=Button(Frame1,text="lector 1",command=entrada)
start_button.place(x=95, y=32)
ventana.mainloop()
