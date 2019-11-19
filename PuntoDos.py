
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
ventana.geometry('450x210')
ventana.title("Punto Dos")

# Fetch the service account key JSON file contents
cred = credentials.Certificate('key/key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://parcial-d03bc.firebaseio.com/'
})

Frame1 = Frame(ventana, bg="gray", highlightthickness=1, width=1280, height=800, bd= 5)
Frame1.place(x = 0,y = 0)

valor= Label(Frame1, bg='cadet blue1', font=("Arial Bold", 15), fg="black", width=25)
adc_data=StringVar()
valor2= Label(Frame1, bg='cadet blue1', font=("Arial Bold", 15), fg="black", width=25)
adc_data2=StringVar()
valor3= Label(Frame1, bg='cadet blue1', font=("Arial Bold", 15), fg="black", width=25)
adc_data3=StringVar()
variable=StringVar()
      
def adc_read1():
    ref=db.reference('sensor')
    x=ref.get()
    print(x.get('sensor1'))
    adc_data.set(x.get('sensor1'))
    
def adc_read2():
    ref=db.reference('sensor')
    x3=ref.get()
    print(x3.get('sensor2'))
    adc_data2.set(x3.get('sensor2'))

def adc_read3():
    ref=db.reference('sensor')
    x2=ref.get()
    print(x2.get('sensor3'))
    adc_data3.set(x2.get('sensor3'))


valor.configure(textvariable=adc_data)
valor.place(x=20, y=30)
adc1_update=Button(Frame1,text="adc1_update",command=adc_read1)
adc1_update.place(x=330, y=32)

valor2.configure(textvariable=adc_data2)
valor2.place(x=20, y=80)
adc2_update=Button(Frame1,text="adc2_update",command=adc_read2)
adc2_update.place(x=330, y=82)

valor3.configure(textvariable=adc_data3)
valor3.place(x=20, y=130)
adc3_update=Button(Frame1,text="adc3_update",command=adc_read3)
adc3_update.place(x=330, y=132)

ventana.mainloop()
