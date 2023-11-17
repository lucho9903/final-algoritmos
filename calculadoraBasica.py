from tkinter import *
from math import *
import os
from git import Repo

ventana = Tk()
ventana.title("Calculadora UCO")
ventana.geometry("480x400")
ventana.resizable(False, False)
ventana.configure(background="gray1")

color_boton = "gray15"
ancho_boton = 10
alto_boton = 3

operador = " "
texto_pantalla = StringVar()

def clear_basica():
    global operador
    operador = ""
    texto_pantalla.set("0")

def click_basica(b):
    global operador
    operador += str(b)
    texto_pantalla.set(operador)

def resultado_basica():
    global operador
    try:
        r = str(eval(operador))
        guardar_historial(operador, r)
    except:
        r = "Math ERROR"
    texto_pantalla.set(r)

def guardar_historial(expresion, resultado):
    with open("historial_calculadora.txt", "a") as archivo:
        archivo.write(f"{expresion} = {resultado}\n")
    try:
        repo = Repo(r"C:\Users\Lucho\final-algoritmos")
        repo.git.add("historial_calculadora.txt")
        repo.git.commit("-m", "se actualizo el historial de la calculadora basica")
        repo.git.push("origin")
        print("Historial actualizado y enviado a Git.")
    except Exception as e:
        print(f"Error al enviar a Git: {e}")    

Boton7 = Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_basica(7)).grid(row=1,column=0,pady=10)
Boton8 = Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click_basica(8)).grid(row=1,column=1,pady=10)
Boton9 = Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_basica(9)).grid(row=1,column=2,pady=10)
BotonClear = Button(ventana,text="C",bg="red",width=ancho_boton,height=alto_boton,fg="white", command=clear_basica).grid(row=1,column=3,pady=10)
BotonIgual = Button(ventana,text="=",bg="blue" ,width=ancho_boton,height=alto_boton, fg="white",command=resultado_basica).grid(row=1,column=4,pady=10)

Boton4 = Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white", command=lambda:click_basica(4)).grid(row=2,column=0,pady=10)
Boton5 = Button(ventana,text="5",bg=color_boton,width=ancho_boton ,height=alto_boton,fg="white", command=lambda:click_basica(5)).grid(row=2,column=1,pady=10)
Boton6 = Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click_basica(6)).grid(row=2,column=2,pady=10)
BotonMultiplicar = Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_basica("*")).grid(row=2,column=3,pady=10)
BotonDivision = Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_basica("/")).grid(row=2,column=4,pady=10)

Boton1 = Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_basica(1)).grid(row=3,column=0,pady=10)
Boton2 = Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_basica(2)).grid(row=3,column=1,pady=10)
Boton3 = Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click_basica(3)).grid(row=3,column=2,pady=10)
BotonSuma = Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click_basica("+")).grid(row=3,column=3,pady=10)
BotonResta = Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_basica("-")).grid(row=3,column=4,pady=10)

Boton_0 = Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_basica(0)).grid(row=4,column=0,pady=10)
BotonPunto = Button(ventana,text=".",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_basica(".")).grid(row=4,column=1,pady=10)
BotonParenIzq = Button(ventana,text="(",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click_basica("(")).grid(row=4,column=2,pady=10)
BotonParenDer = Button(ventana,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_basica(")")).grid(row=4,column=3,pady=10)
BotonMod = Button(ventana,text="%",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click_basica("%")).grid(row=4,column=4,pady=10)
    
Pantalla = Entry(ventana, font=("arial", 20, "bold"), width=22, borderwidth=10, background="grey50", textvariable=texto_pantalla)
Pantalla.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

ventana.mainloop()
    