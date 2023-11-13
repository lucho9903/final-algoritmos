import tkinter as tk
import subprocess

def abrir_programa1():
    subprocess.Popen(["python", "calculadoraBasica.py"])

def abrir_programa2():
    subprocess.Popen(["python", "calculadoraTK.py"])  

def abrir_programa3():
    subprocess.Popen(["python", "calculadoraMatriz.py"])

ventana = tk.Tk()
ventana.title("calculadoras")
ventana.geometry("400x200")
ventana.resizable(False, False)
ventana.configure(background="gray1")

color_boton = "gray15"
ancho_boton = 30
alto_boton = 4

boton_programa1 = tk.Button(ventana, text="calculadora basica", bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=abrir_programa1)
boton_programa2 = tk.Button(ventana, text="calculadora cientifica",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white", command=abrir_programa2)
boton_programa3 = tk.Button(ventana, text="calculadora matrices",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white", command=abrir_programa3)

boton_programa1.pack()
boton_programa2.pack()
boton_programa3.pack()

ventana.mainloop()