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
    ah.geometry("600x600")
    ah.resizable(False,False)
    #ah.configure(background="black")
    global canvas
    canvas = Canvas(ah,width=600,height=600,background="black")
    canvas.pack(expand=True, fill="both")

    global tu_palabra
    tu_palabra = StringVar()
    global Pal_adivinar
    Pal_adivinar = StringVar()
    global P_Palabra 

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
    # for i in Pal:
    #     print(i,count)
    #     count = count + 1
    # while a < count:
    #     guiones = [Label(ah,font=("arial",22,"bold"),fg=("white"),text=("_"),background="black").place(x=50+esp,y=125)]
    #     a = a + 1
    #     esp = esp + 30

    guiones = [Label(ah,font=("arial",22,"bold"),fg=("white"),text=("_"),background="black") for _ in Pal]
    for i in range(len(Pal)):
        guiones[i].place(x=50+esp,y=125)
        esp = esp + 30

def Prob():
    # global Pal
    # global P_Palabra
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
            canvas.create_line(325,200,325,475,fill='LightYellow4',width=10) 
            canvas.create_line(180,200,330,200,fill='LightYellow4',width=10)
        
        elif vidas == 3:
                canvas.create_line(190,200,190,230,fill='LightYellow4',width=7)
                canvas.create_oval(160,230,220,290,fill='bisque2',width=3,outline='bisque2')

        elif vidas == 2:
                canvas.create_rectangle(150,290,230,375,fill='bisque2',width=3,outline="black")
        
        elif vidas == 1:
                canvas.create_line(150,290,130,360,fill='bisque2',width=9)
                canvas.create_line(230,290,250,360,fill='bisque2',width=9)
        

        elif vidas <=0:
                Lose = Label(ah,font=("arial",22,"bold"),fg=("red"),text=("Perdistes"),background="black").place(x=425,y=300)
                button1 = Button(ah,text=("Probar"),font=("arial",22),bg="green",fg="white",state=DISABLED).place(x=425,y=500)
                canvas.create_line(170,350,170,450,fill='bisque2',width=9)
                canvas.create_line(210,350,210,450,fill='bisque2',width=9)
            

    if tamano == a:
            Win = Label(ah,font=("arial",22,"bold"),fg=("red"),text=("Ganastes"),background="black").place(x=425,y=300)
            button1 = Button(ah,text=("Probar"),font=("arial",22),bg="green",fg="white",state=DISABLED).place(x=425,y=500)

    
    
    print(tamano,a)    
    print(usadas)
 
    # P_Palabra.entry.delete(0, END)

    # Label(ah,font=("arial",22,"bold"),fg=("white"),text=(tupa),background="black").place(x=50+esp2,y=200)
    # esp2 = esp2 + 30

def reiniciar():
    ah.destroy()
    os.system('ahorcado.py')
    

Juego2()