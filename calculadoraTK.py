from tkinter import *
from math import *

ventana = Tk()
ventana.title("Calculadora UCO")
ventana.geometry("480x580")
ventana.resizable(False, False)
ventana.configure(background="gray1")

color_boton = "gray15"
ancho_boton = 10
alto_boton = 3

operador = " "
texto_pantalla = StringVar()

def clear_cientifica():
    global operador
    operador = ""
    texto_pantalla.set("0")

def click_cientifica(b):
    global operador
    operador += str(b)
    texto_pantalla.set(operador)

def resultado_cientifica():
    global operador
    try:
        r = str(eval(operador))
        guardar_historial(operador, r)
    except:
        r = "Math ERROR"
    texto_pantalla.set(r)

def guardar_historial(expresion, resultado):
    with open("historial_cientifica.txt", "a") as archivo:
        archivo.write(f"{expresion} = {resultado}\n")


Boton7 = Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_cientifica(7)).grid(row=1,column=0,pady=10)
Boton8 = Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click_cientifica(8)).grid(row=1,column=1,pady=10)
Boton9 = Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_cientifica(9)).grid(row=1,column=2,pady=10)
BotonClear = Button(ventana,text="C",bg="red",width=ancho_boton,height=alto_boton,fg="white", command=clear_cientifica).grid(row=1,column=3,pady=10)
BotonMod = Button(ventana,text="%",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click_cientifica("%")).grid(row=1,column=4,pady=10)

Boton4 = Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white", command=lambda:click_cientifica(4)).grid(row=2,column=0,pady=10)
Boton5 = Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_cientifica(5)).grid(row=2,column=1,pady=10)
Boton6 = Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click_cientifica(6)).grid(row=2,column=2,pady=10)
BotonMultiplicar = Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_cientifica("*")).grid(row=2,column=3,pady=10)
BotonDivision = Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_cientifica("/")).grid(row=2,column=4,pady=10)

Boton1 = Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_cientifica(1)).grid(row=3,column=0,pady=10)
Boton2 = Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_cientifica(2)).grid(row=3,column=1,pady=10)
Boton3 = Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click_cientifica(3)).grid(row=3,column=2,pady=10)
BotonSuma = Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click_cientifica("+")).grid(row=3,column=3,pady=10)
BotonResta = Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_cientifica("-")).grid(row=3,column=4,pady=10)

Boton_0 = Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_cientifica(0)).grid(row=4,column=0,pady=10)
BotonPunto = Button(ventana,text=".",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_cientifica(".")).grid(row=4,column=1,pady=10)
BotonPi = Button(ventana,text="π",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_cientifica("pi")).grid(row=4,column=2,pady=10)
BotonParenIzq = Button(ventana,text="(",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click_cientifica("(")).grid(row=4,column=3,pady=10)
BotonParenDer = Button(ventana,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_cientifica(")")).grid(row=4,column=4,pady=10)

BotonSen = Button(ventana,text="sen",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_cientifica("sin(")).grid(row=5,column=0,pady=10)
BotonCos = Button(ventana,text="cos",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_cientifica("cos(")).grid(row=5,column=1,pady=10)
BotonTan = Button(ventana,text="tan",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click_cientifica("tan(")).grid(row=5,column=2,pady=10)
BotonRaiz = Button(ventana,text="√",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click_cientifica("sqrt(")).grid(row=5,column=3,pady=10)
BotonEXP = Button(ventana,text="e",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click_cientifica("exp")).grid(row=5,column=4,pady=10)

BotonArcCos = Button(ventana, text="cos^-1", bg=color_boton, width=ancho_boton, height=alto_boton,fg="white", command=lambda: click_cientifica("acos(")).grid(row=6, column=0, pady=10)
BotonArcSin = Button(ventana, text="sin^-1", bg=color_boton, width=ancho_boton, height=alto_boton,fg="white", command=lambda: click_cientifica("asin(")).grid(row=6, column=1, pady=10)
BotonArcTan = Button(ventana, text="tan^-1", bg=color_boton, width=ancho_boton, height=alto_boton,fg="white", command=lambda: click_cientifica("atan")).grid(row=6, column=2, pady=10)
BotonLN = Button(ventana,text="LN",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click_cientifica("log")).grid(row=6,column=3,pady=10)
BotonIgual = Button(ventana,text="=",bg="blue",width=ancho_boton,height=alto_boton, fg="white",command=resultado_cientifica).grid(row=6,column=4,pady=10)

Pantalla = Entry(ventana, font=("arial", 20, "bold"), width=22, borderwidth=10, background="grey50", textvariable=texto_pantalla)
Pantalla.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

ventana.mainloop()
