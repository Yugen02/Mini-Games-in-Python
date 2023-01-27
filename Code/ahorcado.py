from tkinter import *
import os
from tkinter import messagebox
from tkinter import Canvas

global usadas
usadas = list()
global a
a = 0

def Juego2():
    global esp2
    esp2 = 0
    global ah
    ah = Tk()
    ah.title("Ahorcado")
    ah.geometry("1000x600")
    ah.resizable(False,False)
    global canvas
    canvas = Canvas(ah,width=1000,height=600,background="black",bd=0)
    canvas.pack(expand=True, fill="both")

    global tu_palabra
    tu_palabra = StringVar()
    global Pal_adivinar
    Pal_adivinar = StringVar()
    global P_Palabra 

    blank_1 = Label(canvas,font=("arial",1,"bold"),fg=("white"),text=(""),background="black").pack()
    Label(canvas,font=("arial",22,"bold"),fg=("white"),text=("El Ahorcado"),background="black").pack()
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PRUEBAS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Label(ah,font=("arial",22,"bold"),fg=("white"),text=("                           "),background="black").pack()
    # P_Palabra = Entry(ah,bg="CadetBlue1",font=("arial",22),fg="black",textvariable=Pal_adivinar,show="*").pack(side = TOP)
    # Label(ah,font=("arial",22,"bold"),fg=("white"),text=("                           "),background="black").pack()
    # inicio_button2 = Button(ah,text=("Iniciar"),font=("arial",22),bg="green",fg="white",command=begin).pack(side = TOP)
    # Label(ah,font=("arial",22,"bold"),fg=("white"),text=("                           "),background="black").pack()
    # Label(ah,font=("arial",22,"bold"),fg=("white"),text=("                           "),background="black").pack()
    # button1 = Button(ah,text=("Probar"),font=("arial",22),bg="green",fg="white",command=Prob).pack(side=RIGHT)
    # P_letra = Entry(ah,font=("arial",22),bg="CadetBlue1",fg="black",width=5,textvariable=tu_palabra).pack(side = LEFT)
    # rei_button3 = Button(ah,text=("Reiniciar"),font=("arial",22),bg="green",fg="white",command=reiniciar).pack(side=BOTTOM)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    button1 = Button(canvas,text=("Probar"),font=("arial",22),bg="green",fg="white",command=Prob).place(x=425,y=500)
    P_Palabra = Entry(canvas,bg="CadetBlue1",font=("arial",22),fg="black",textvariable=Pal_adivinar,show="*").place(x=50,y=59)
    inicio_button2 = Button(canvas,text=("Iniciar"),font=("arial",22),bg="green",fg="white",command=begin).place(x=425,y=50)
    rei_button3 = Button(canvas,text=("Reiniciar"),font=("arial",22),bg="green",fg="white",command=reiniciar).place(x=425,y=400)
    P_letra = Entry(canvas,font=("arial",22),bg="CadetBlue1",fg="black",width=5,textvariable=tu_palabra).place(x=100,y=510)

    ah.mainloop()

def begin():
    esp = 0
    count = 0
    global vidas
    global guiones
    vidas = 5
    global Pal
    global Pal1
    Pal1 = Pal_adivinar.get()
    Pal = Pal1.lower()
    tu_palabra=""


    guiones = [Label(ah,font=("arial",22,"bold"),fg=("white"),text=("_"),background="black") for _ in Pal]
    for i in range(len(Pal)):
        guiones[i].place(x=50+esp,y=125)
        esp = esp + 30
    inicio_button2 = Button(canvas,text=("Iniciar"),font=("arial",22),bg="green",fg="white",command=begin,state=DISABLED).place(x=425,y=50)

def Prob():

    global vidas
    global a
    global esp2
    global tamano
    b = 0

    tamano = len(Pal)
    tupa = tu_palabra.get()

    if tupa in Pal:
        if tupa not in usadas:
            usadas.append(tupa)
            if Pal.count(tupa)>1:
                for rn in range(len(Pal)):
                    if Pal[rn]==tupa:
                        guiones[rn].config(text=""+tupa)
                        a = a + 1
                                 
                    
            else:
                guiones[Pal.index(tupa)].config(text=""+tupa)
                a = a + 1

        else:
            messagebox.showinfo(message="Esta letra ya lo uso, intente con otra", title="Advertencia")

    else:
        vidas = vidas - 1
        print(vidas)
    
    if vidas == 4:
        filename4 = PhotoImage(file = "300.4.png")
        canvas.create_image(250, 325, image=filename4).pack()


    elif vidas ==3:
        filename3 = PhotoImage(file = "300.3.png")
        canvas.create_image(250,325,image=filename3).pack()


    elif vidas ==2:
        filename2 = PhotoImage(file = "300.2.png")
        canvas.create_image(250,325,image=filename2).pack()

    elif vidas ==1:
        filename1 = PhotoImage(file = "300.1.png")
        canvas.create_image(250,325,image=filename1).pack


    elif vidas <= 0:
        filename0 = PhotoImage(file = "300.pn")
        canvas.create_image(250,325,image=filename0).pack()
        Lose = Label(ah,font=("arial",22,"bold"),fg=("red"),text=("Perdistes"),background="black").place(x=425,y=300)
        button1 = Button(ah,text=("Probar"),font=("arial",22),bg="green",fg="white",state=DISABLED).place(x=425,y=500)
        Label(ah,font=("arial",22,"bold"),fg=("cyan"),text=(Pal),background="black").place(x=70,y=550)

    
    if tamano == a:
        Win = Label(ah,font=("arial",22,"bold"),fg=("red"),text=("Ganastes"),background="black").place(x=425,y=300)
        button1 = Button(ah,text=("Probar"),font=("arial",22),bg="green",fg="white",state=DISABLED).place(x=425,y=500)

    
    
    print(tamano,a)    
    print(usadas)


def reiniciar():
    ah.destroy()
    os.system('ahorcado.py')
    

Juego2()
