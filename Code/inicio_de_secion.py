from tkinter import *
import os
from tkinter import messagebox

def inicio():
    global regi
    regi = Toplevel(sesi)
    regi.title("Registro")
    regi.geometry("550x370")
    regi.resizable(False,False)
    regi.configure(background="black")
    
    global NAME
    NAME = StringVar()
    global PASSWORD
    PASSWORD = StringVar()

    Label(regi,font=("arial",22,"bold"),fg=("white"),text=("Introduzca su Nombre y Contraseña"),background="black").pack()
    Label(regi,font=("arial",22,"bold"),fg=("white"),text=(""),background="black").pack()

    N_User = Label(regi,font=("arial",22,"bold"),fg=("white"),text=("Usuario:"),background="black").pack()
    P_Usuario_Regi = Entry(regi,font=("arial",22),background="CadetBlue1",textvariable=NAME).pack()

    Contra_User = Label(regi,font=("arial",22,"bold"),fg=("white"),text=("Contraseña:"),background="black").pack()
    P_Contrasena_Regi = Entry(regi,font=("arial",22),background="CadetBlue1",textvariable=PASSWORD,show="*").pack()

    Label(regi,font=("arial",22,"bold"),fg=("white"),text=(""),background="black").pack()
    button_Regi = Button(regi, text='Registrarme',font=("arial",22), fg='White', background= 'dark green',command=archivo).pack()

def archivo():
    user_info = NAME.get()
    clave_info = PASSWORD.get()

    file = open(user_info, "w")
    file.write(user_info + "\n")
    file.write(clave_info)

    file.close()
    Label(regi,font=("arial",22,"bold"),fg=("white"),text=("Registro Completo"),background="black").pack()



def login():
    global sesi
    sesi = Tk()
    sesi.title("Inicio De Sesion")
    sesi.geometry("600x300")
    sesi.resizable(False,False)
    sesi.configure(background="black")
    global Users
    Users = StringVar()
    global Clave
    Clave = StringVar()


    Pantalla1 = Entry(sesi,font=("arial",22),background="CadetBlue1",textvariable=Users).place(x=200,y=50,width=250,height=30)
    Usuario = Label(sesi,font=("arial",22,"bold"),fg=("white"),text=("Usuario:"),background="black").place(x=0,y=45)

    Pantalla2 = Entry(sesi,font=("arial",22),background="CadetBlue1",textvariable=Clave,show="*").place(x=200,y=100,width=250,height=30)
    Contrasena = Label(sesi,font=("arial",22,"bold"),fg=("white"),text=("Contraseña:"),background="black").place(x=0,y=95)

    button1 = Button(sesi, text='Acceder',font=("arial",22), fg='White', background= 'dark green',command=getvalue).place(x=300,y=200)
    button2 = Button(sesi, text='Registrate',font=("arial",22), fg='White', background= 'dark green',command=inicio).place(x=100,y=200)

    sesi.mainloop()

def getvalue():
    Users1 = Users.get()
    Clave1 = Clave.get()
    #Pantalla2.delete(0, END)

    lista_archivos = os.listdir() #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.
    #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS..
    if "Raelee" == Users1:
        archivo1 = open(Users1, "r") 
        verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.
        if Clave1 in verifica:
            # Raelee()
            juego2()
            Label(sesi,font=("arial",22,"bold"),fg=("red"),text=("                                                          "),background="black").place(x=50,y=150)
        else:
            messagebox.showinfo(message="Contraseña incorrecta, por favor verifique su contraseña", title="Advertencia")

    elif Users1 in lista_archivos:

        archivo1 = open(Users1, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
        verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.
        #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
        if Clave1 in verifica:
            print("Entrastes")
            Label(sesi,font=("arial",22,"bold"),fg=("red"),text=("                                                          "),background="black").place(x=50,y=150)
            juego1()

        else:
            messagebox.showinfo(message="Contraseña incorrecta, por favor verifique su contraseña", title="Advertencia")

    else:
        messagebox.showinfo(message="Usuario incorrecto, por favor verifique su nombre de usuario", title="Advertencia")


def Raelee():
    global rae
    rae = Toplevel(sesi)
    rae.title("We")
    rae.geometry("550x150")
    rae.resizable(False,False)
    rae.configure(background="black")

    Label(rae,font=("arial",40,"bold"),fg=("red"),text=("Bien Hecho"),background="black").pack()

def juego1():
    os.system('equizero.py')

def juego2():
    os.system('ahorcado.py')
login()
