#count_impar = 1
#count_par = 2
#turno_o = [1,3,5,7,9]



#for i in [1,2,3,4,5,6,7,8,9]:
    
    
 #   if i == count_impar:
  #      print("X")
   #     count_impar = count_impar + 2
    #elif i == count_par:
     #   print("O")
      #  count_par = count_par + 2
import tkinter as tk
a = 0

def funcion():
    global a 
    print(a)
    a = a + 1
    
root = tk.Tk()
boton = tk.Button(root, text="¿Que te parece la guia?", command=funcion)
root.geometry('380x300')
root.title("Ventana")
boton.pack()
root.mainloop()