#-----------------------------------------Juego----------------------------------------------
import random 
options = ['1', '2', '3']
play=True
#----------------------------------- Interfaz Grafica --------------------------
from tkinter import *
from tkinter import messagebox

raiz=Tk()
raiz.config(bg="lightblue")
raiz.geometry("250x150")
#-------------------------------------------------------- Ventanas emergentes -------------------------------
varOption=IntVar()
while play == True:

    def jugar():
        pc = random.choice(options)
        if varOption.get()==1:
            if pc == '1':
                raiz.withdraw()
                messagebox.showinfo('Resultado',"Ambos sacamos papel. EMPATE")
                
            elif pc == '3':
                raiz.withdraw()
                messagebox.showinfo('Resultado',"Yo saque tijeras. PIERDES")
                
            elif pc == '2':
                raiz.withdraw()
                messagebox.showinfo("Eleccion", "Yo saque piedra. Papel le gana a piedra. GANASTE")
        
        elif varOption.get()==2:
            if pc == '1':
                raiz.withdraw()
                messagebox.showinfo('Resultado',"Saque papel. PIERDES")
                
            elif pc == '3':
                raiz.withdraw()
                messagebox.showinfo('Resultado',"Ambos sacamos piedra. EMPATE")
                
            elif pc == '2':
                raiz.withdraw()
                messagebox.showinfo("Resultado", "Yo saque tijeras. GANASTE")

        elif varOption.get()==3:
            if pc == '1':
                raiz.withdraw()
                messagebox.showinfo('Resultado',"Saque papel. GANASTE")
                           
            elif pc == '3':
                raiz.withdraw()
                messagebox.showinfo('Resultado',"Ambos sacamos tijera. EMPATE")
                
                
            elif pc == '2':
                raiz.withdraw()
                messagebox.showinfo("Resultado", "Yo saque piedra. PIERDES")
                
          
        valor=messagebox.askquestion("Otra vez", "¿Quieres volver a jugar?")
        if valor == "yes": 
            play = True
            raiz.deiconify()
        else:
            raiz.destroy()
            
#------------------------------- Interfaz ---------------------------------------------------
    

    instruccion=Label(raiz, text="Elige piedra, papel o tijera", padx=10, pady=10)
    instruccion.config(bg="lightblue")
    instruccion.pack()

    papel=Radiobutton(raiz, text="Papel", variable=varOption, value=1,  command=jugar, pady=5)
    papel.config(bg="lightblue")
    papel.pack()

    piedra=Radiobutton(raiz, text="Piedra", variable=varOption, value=2, command=jugar,pady=5)
    piedra.config(bg="lightblue")
    piedra.pack()

    tijera=Radiobutton(raiz, text="Tijera", variable=varOption, value=3, command=jugar,pady=5)
    tijera.config(bg="lightblue")
    tijera.pack()
    
    raiz.mainloop()

