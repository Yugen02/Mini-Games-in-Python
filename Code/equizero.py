from tkinter import *

xo = Tk()
xo.title("Minijuego Para Mancos")
xo.geometry("600x300")
xo.resizable(False,False)
xo.configure(background="black")

# definiciones
count_impar = 1
count_par = 2
turno_o = [1,3,5,7,9]
texto_pan1= StringVar()
texto_pan2= StringVar()
texto_pan3= StringVar()
texto_pan4= StringVar()
texto_pan5= StringVar()
texto_pan6= StringVar()
texto_pan7= StringVar()
texto_pan8= StringVar()
texto_pan9= StringVar()
texto_pan10= StringVar()

texto_pan= StringVar()
b = 1
a = 1
IX = 'X'
IO = 'O'

def funcion1():
    global turno1
    global a
    global b
    global count_impar
    global count_par
    if a == count_impar:
        turno1 = str(IX)
        texto_pan1.set(turno1)
        count_impar = count_impar + 2
    elif a == count_par:
        turno1 = str(IO)
        texto_pan1.set(turno1)
        count_par = count_par + 2
    a = a + 1
    b = b + 1

def funcion2():
    global turno2
    global a
    global b
    global count_impar
    global count_par
    if a == count_impar:
        turno2 = str(IX)
        texto_pan2.set(turno2)
        count_impar = count_impar + 2
    elif a == count_par:
        turno2 = str(IO)
        texto_pan2.set(turno2)
        count_par = count_par + 2
    a = a + 1
    b = b + 1

def funcion3():
    global turno3
    global a
    global b
    global count_impar
    global count_par
    if a == count_impar:
        turno3 = str(IX)
        texto_pan3.set(turno3)
        count_impar = count_impar + 2
    elif a == count_par:
        turno3 = str(IO)
        texto_pan3.set(turno3)
        count_par = count_par + 2
    a = a + 1
    b = b + 1

def funcion4():
    global turno4
    global a
    global b
    global count_impar
    global count_par
    if a == count_impar:
        turno4 = str(IX)
        texto_pan4.set(turno4)
        count_impar = count_impar + 2
    elif a == count_par:
        turno4 = str(IO)
        texto_pan4.set(turno4)
        count_par = count_par + 2
    a = a + 1
    b = b + 1

def funcion5():
    global turno5
    global a
    global b
    global count_impar
    global count_par
    if a == count_impar:
        turno5 = str(IX)
        texto_pan5.set(turno5)
        count_impar = count_impar + 2
    elif a == count_par:
        turno5 = str(IO)
        texto_pan5.set(turno5)
        count_par = count_par + 2
    a = a + 1
    b = b + 1

def funcion6():
    global turno6
    global a
    global b
    global count_impar
    global count_par
    if a == count_impar:
        turno6 = str(IX)
        texto_pan6.set(turno6)
        count_impar = count_impar + 2
    elif a == count_par:
        turno6 = str(IO)
        texto_pan6.set(turno6)
        count_par = count_par + 2
    a = a + 1
    b = b + 1

def funcion7():
    global turno7
    global a
    global b
    global count_impar
    global count_par
    if a == count_impar:
        turno7 = str(IX)
        texto_pan7.set(turno7)
        count_impar = count_impar + 2
    elif a == count_par:
        turno7 = str(IO)
        texto_pan7.set(turno7)
        count_par = count_par + 2
    a = a + 1
    b = b + 1

def funcion8():
    global turno8
    global a
    global b
    global count_impar
    global count_par
    if a == count_impar:
        turno8 = str(IX)
        texto_pan8.set(turno8)
        count_impar = count_impar + 2
    elif a == count_par:
        turno8 = str(IO)
        texto_pan8.set(turno8)
        count_par = count_par + 2
    a = a + 1

def funcion9():
    global turno9
    global a
    global b
    global count_impar
    global count_par
    if a == count_impar:
        turno9 = str(IX)
        texto_pan9.set(turno9)
        count_impar = count_impar + 2
    elif a == count_par:
        turno9 = str(IO)
        texto_pan9.set(turno9)
        count_par = count_par + 2
    a = a + 1

def funcion10():
    global turno10
    turno10 = str('¡Pasa Pack!')
    texto_pan10.set(turno10)


#Pantallas
Pantalla0 = Label(xo,width=2,font=("arial",33,"bold"),background="CadetBlue1",textvariable=texto_pan1).place(x=350,y=10)
Pantalla1 = Label(xo,width=2,font=("arial",33,"bold"),background="CadetBlue1",textvariable=texto_pan2).place(x=423,y=10)
Pantalla2 = Label(xo,width=2,font=("arial",33,"bold"),background="CadetBlue1",textvariable=texto_pan3).place(x=496,y=10)
Pantalla3 = Label(xo,width=2,font=("arial",33,"bold"),background="CadetBlue1",textvariable=texto_pan4).place(x=350,y=85)
Pantalla4 = Label(xo,width=2,font=("arial",33,"bold"),background="CadetBlue1",textvariable=texto_pan5).place(x=423,y=85)
Pantalla5 = Label(xo,width=2,font=("arial",33,"bold"),background="CadetBlue1",textvariable=texto_pan6).place(x=496,y=85)
Pantalla6 = Label(xo,width=2,font=("arial",33,"bold"),background="CadetBlue1",textvariable=texto_pan7).place(x=350,y=160)
Pantalla7 = Label(xo,width=2,font=("arial",33,"bold"),background="CadetBlue1",textvariable=texto_pan8).place(x=423,y=160)
Pantalla8 = Label(xo,width=2,font=("arial",33,"bold"),background="CadetBlue1",textvariable=texto_pan9).place(x=496,y=160)
Pantalla9 = Label(xo,width=10,font=("arial",33,"bold"),background="CadetBlue1",textvariable=texto_pan10).place(x=190,y=230)

# Botones
An_Boton = 6
Al_Boton = 3
Boton0 = Button(xo,text =' ',command=funcion1,width=An_Boton,heigh=Al_Boton).grid(row=1,column=0,padx=10,pady=10)
Boton1 = Button(xo,text =' ',command=funcion2,width=An_Boton,heigh=Al_Boton).grid(row=1,column=1,padx=10,pady=10)
Boton2 = Button(xo,text =' ',command=funcion3,width=An_Boton,heigh=Al_Boton).grid(row=1,column=2,padx=10,pady=10)
Boton3 = Button(xo,text =' ',command=funcion4,width=An_Boton,heigh=Al_Boton).grid(row=2,column=0,padx=10,pady=10)
Boton4 = Button(xo,text =' ',command=funcion5,width=An_Boton,heigh=Al_Boton).grid(row=2,column=1,padx=10,pady=10)
Boton5 = Button(xo,text =' ',command=funcion6,width=An_Boton,heigh=Al_Boton).grid(row=2,column=2,padx=10,pady=10)
Boton6 = Button(xo,text =' ',command=funcion7,width=An_Boton,heigh=Al_Boton).grid(row=3,column=0,padx=10,pady=10)
Boton7 = Button(xo,text =' ',command=funcion8,width=An_Boton,heigh=Al_Boton).grid(row=3,column=1,padx=10,pady=10)
Boton8 = Button(xo,text =' ',command=funcion9,width=An_Boton,heigh=Al_Boton).grid(row=3,column=2,padx=10,pady=10)
Boton9 = Button(xo,text =' ',command=funcion10,width=An_Boton,heigh=Al_Boton).place(x=496,y=230)

#  Programacion
xo.mainloop()
