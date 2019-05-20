#-----------------------------------------Juego----------------------------------------------
import random 
import time
options = ['1', '2', '3']
play=True
#----------------------------------- Interfaz Grafica --------------------------
from tkinter import *
from tkinter import messagebox

raiz=Tk()
raiz.config(bg="lightblue")
raiz.geometry("220x80")

def envio():
    
    instruccioninicio.pack_forget()
    raiz.geometry("200x140")
    nombre.pack_forget()
    enviar.pack_forget()
    

instruccioninicio=Label(raiz, text="Escribe tu nombre",pady=8, padx=8)
instruccioninicio.config(bg="lightblue")
instruccioninicio.pack()

nombre=Entry(raiz)
nombre.pack()

enviar=Button(raiz, text="Enviar",command=envio)
enviar.pack()
#-------------------------------------------------------- Ventanas emergentes -------------------------------
varOption=IntVar()
while play == True:

    def jugar():
        pc = random.choice(options)
        if varOption.get()==1:
            if pc == '1':
                raiz.withdraw()

                messagebox.showinfo('Resultado',"Ambos sacamos papel. EMPATE " +nombre.get())
                
            elif pc == '3':
                raiz.withdraw()
                messagebox.showinfo('Resultado',"Yo saque tijeras. PIERDES " +nombre.get()+". :(")
                
            elif pc == '2':
                raiz.withdraw()
                messagebox.showinfo("Resultado", "Yo saque piedra. Papel le gana a piedra. GANASTE " +nombre.get()+"!")
                
        elif varOption.get()==2:
            if pc == '1':
                raiz.withdraw()

                messagebox.showinfo('Resultado',"Saque papel. PIERDES " +nombre.get()+" :(")
                
            elif pc == '3':
                raiz.withdraw()
                messagebox.showinfo('Resultado',"Ambos sacamos piedra. EMPATE " +nombre.get())
                
            elif pc == '2':
                raiz.withdraw()
                messagebox.showinfo("Resultado", "Yo saque tijeras. GANASTE " +nombre.get()+"!")


        elif varOption.get()==3:
            if pc == '1':
                raiz.withdraw()
                messagebox.showinfo('Resultado',"Saque papel. GANASTE " +nombre.get()+"!")
                           
            elif pc == '3':
                raiz.withdraw()
                messagebox.showinfo('Resultado',"Ambos sacamos tijera. EMPATE " +nombre.get())

            elif pc == '2':
                raiz.withdraw()
                messagebox.showinfo("Resultado", "Yo saque piedra. PIERDES " +nombre.get()+" :(")

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