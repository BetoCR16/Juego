#-----------------------------------------Juego----------------------------------------------
import random 
options = ['1', '2', '3']
play=True
#----------------------------------- Interfaz Grafica --------------------------
from tkinter import *
from tkinter import messagebox

raiz=Tk()
varOption=IntVar()

while play == True:

    def imprimir():
        pc = random.choice(options)
        if varOption.get()==1:
            if pc == '1':
                messagebox.showinfo('Resultado',"Ambos sacamos papel. EMPATE")
                
            elif pc == '3':
                messagebox.showinfo('Resultado',"Yo saque tijeras. PIERDES")
                
            elif pc == '2':
                messagebox.showinfo("Eleccion", "Yo saque piedra. Papel le gana a piedra. GANASTE")
                
            
        elif varOption.get()==2:
            if pc == '1':
                messagebox.showinfo('Resultado',"Saque papel. PIERDES")
                
            elif pc == '3':
                messagebox.showinfo('Resultado',"Ambos sacamos piedra. EMPATE")
                
            elif pc == '2':
                messagebox.showinfo("Resultado", "Yo saque tijeras. GANASTE")
        elif varOption.get()==3:
            if pc == '1':
                messagebox.showinfo('Resultado',"Saque papel. GANASTE")
                
            elif pc == '3':
                messagebox.showinfo('Resultado',"Ambos sacamos tijera. EMPATE")
                
            elif pc == '2':
                messagebox.showinfo("Resultado", "Yo saque piedra. PIERDES")

    instruccion=Label(raiz, text="Elige piedra, papel o tijera")
    instruccion.pack()

    papel=Radiobutton(raiz, text="Papel", variable=varOption, value=1,  command=imprimir)
    papel.pack()

    piedra=Radiobutton(raiz, text="Piedra", variable=varOption, value=2, command=imprimir)
    piedra.pack()

    tijera=Radiobutton(raiz, text="Tijera", variable=varOption, value=3, command=imprimir)
    tijera.pack()

    raiz.mainloop()