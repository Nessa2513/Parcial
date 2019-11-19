import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from pyfirmata import Arduino, util
from tkinter import *
from PIL import Image
from PIL import ImageTk
import time
cont=0
cont2=0
cont3=0
cont4=0
cont5=0
cont6=0
cont7=0
cont8=0
cont9=0
cont10=0

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
ventana.geometry('1200x1200')
ventana.title("Punto Cuatro")

# Fetch the service account key JSON file contents
cred = credentials.Certificate('key/key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://parcial-d03bc.firebaseio.com/'
})

Frame1 = Frame(ventana, bg="gray", highlightthickness=1, width=1280, height=800, bd= 5)
Frame1.place(x = 0,y = 0)

valor= Label(Frame1, bg='light blue', font=("Arial Bold", 15), fg="black", width=5)
variable=StringVar()

valor2= Label(Frame1, bg='light green', font=("Arial Bold", 15), fg="black", width=5)
variable2=StringVar()

valor3= Label(Frame1, bg='light blue', font=("Arial Bold", 15), fg="black", width=5)
variable3=StringVar()

valor4= Label(Frame1, bg='light green', font=("Arial Bold", 15), fg="black", width=5)
variable4=StringVar()

valor5= Label(Frame1, bg='light blue', font=("Arial Bold", 15), fg="black", width=5)
variable5=StringVar()

valor6= Label(Frame1, bg='light green', font=("Arial Bold", 15), fg="black", width=5)
variable6=StringVar()

valor7= Label(Frame1, bg='light blue', font=("Arial Bold", 15), fg="black", width=5)
variable7=StringVar()

valor8= Label(Frame1, bg='light green', font=("Arial Bold", 15), fg="black", width=5)
variable8=StringVar()

valor9= Label(Frame1, bg='light blue', font=("Arial Bold", 15), fg="black", width=5)
variable9=StringVar()

valor10= Label(Frame1, bg='light green', font=("Arial Bold", 15), fg="black", width=5)
variable10=StringVar()

      
def SOS():
    global cont
    cont=cont+1
    ref = db.reference("contador")
    ref.set({'Boton 1': cont,
        })
    variable.set(cont)
    print("S: °°°")
    print("O: ---")
    print("S: °°°")
    led1.write(1)
    time.sleep(0.1)
    led1.write(0)
    time.sleep(0.1)
    led1.write(1)
    time.sleep(0.1)
    led1.write(0)
    time.sleep(0.1)
    led1.write(1)
    time.sleep(0.1)
    led1.write(0)
    time.sleep(0.2)
    
    led2.write(1)
    time.sleep(0.3)
    led2.write(0)
    time.sleep(0.3)
    led2.write(1)
    time.sleep(0.3)
    led2.write(0)
    time.sleep(0.3)
    led2.write(1)
    time.sleep(0.3)
    led2.write(0)
    time.sleep(0.3)

def estoy_herido():
    #x=a_1.read()
    #print(x)
    #adc_data2.set(x)
    #time.sleep(0.1)
    global cont2
    cont2=cont2+1
    ref = db.reference("contador")
    ref.set({
              'Boton 2': cont2,
        })
    variable2.set(cont2)

def llama_policia():
    global cont3
    cont3=cont3+1
    ref = db.reference("contador")
    ref.set({
              'Boton 3': cont3,
        })
    variable3.set(cont3)

def tiene_arma():
    global cont4
    cont4=cont4+1
    ref = db.reference("contador")
    ref.set({
              'Boton 4': cont4,
        })
    variable4.set(cont4)
    
def incendio():
    global cont5
    cont5=cont5+1
    ref = db.reference("contador")
    ref.set({
              'Boton 5': cont5,
        })
    variable5.set(cont5)
    
def no_puedo_hablar():
    global cont6
    cont6=cont6+1
    ref = db.reference("contador")
    ref.set({
              'Boton 6': cont6,
        })
    variable6.set(cont6)
    
def llama_ambulancia():
    global cont7
    cont7=cont7+1
    ref = db.reference("contador")
    ref.set({
              'Boton 7': cont7,
        })
    variable7.set(cont7)
    
def estoy_perdido():
    global cont8
    cont8=cont8+1
    ref = db.reference("contador")
    ref.set({
        'Boton 8': cont8,
        })
    variabl8e.set(cont8)
    
def nos_hundimos():
    global cont9
    cont9=cont9+1
    ref = db.reference("contador")
    ref.set({
              'Boton 9': cont9,
        })
    variable9.set(cont9)
    
def te_amo():
    global cont10
    cont10=cont10+1
    ref = db.reference("contador")
    ref.set({
              'Boton 10': cont10,
        })
    variable10.set(cont10)
    
valor.configure(textvariable=variable)
valor.place(x=20, y=30)
btn=Button(Frame1,text="SOS",command=SOS)
btn.place(x=95, y=32)

valor2.configure(textvariable=variable2)
valor2.place(x=20, y=80)
btn2=Button(Frame1,text="Estoy Herido",command=estoy_herido)
btn2.place(x=95, y=82)

valor3.configure(textvariable=variable3)
valor3.place(x=20, y=130)
btn3=Button(Frame1,text="Llama a la policía",command=llama_policia)
btn3.place(x=95, y=132)

valor4.configure(textvariable=variable4)
valor4.place(x=20, y=130)
btn4=Button(Frame1,text="Tiene un arma",command=tiene_arma)
btn4.place(x=95, y=132)

valor5.configure(textvariable=variable5)
valor5.place(x=20, y=130)
btn5=Button(Frame1,text="Incendio",command=incendio)
btn5.place(x=95, y=132)

valor6.configure(textvariable=variable6)
valor6.place(x=20, y=130)
btn6=Button(Frame1,text="No puedo hablar",command=no_puedo_hablar)
btn6.place(x=95, y=132)

valor7.configure(textvariable=variable7)
valor7.place(x=20, y=130)
btn7=Button(Frame1,text="Llama a la ambulancia",command=llama_ambulancia)
btn7.place(x=95, y=132)

valor8.configure(textvariable=variable8)
valor8.place(x=20, y=130)
btn8=Button(Frame1,text="Estoy perdido",command=estoy_perdido)
btn8.place(x=95, y=132)

valor9.configure(textvariable=variable9)
valor9.place(x=20, y=130)
btn9=Button(Frame1,text="Nos hundimos",command=nos_hundimos)
btn9.place(x=95, y=132)

valor10.configure(textvariable=variable10)
valor10.place(x=20, y=130)
btn10=Button(Frame1,text="Te amo",command=te_amo)
btn10.place(x=95, y=132)

ventana.mainloop()
