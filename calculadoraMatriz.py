
from git import Repo
import tkinter as tk
from tkinter import messagebox

def crear_matriz_entrada(frame, fila, columna):
    matriz_entrada = []
    for i in range(fila):
        fila_entrada = []
        for j in range(columna):
            entrada = tk.Entry(frame, width=5)
            entrada.grid(row=i + 1, column=j + 1, padx=5, pady=5)
            fila_entrada.append(entrada)
        matriz_entrada.append(fila_entrada)
    return matriz_entrada

def obtener_valores_matriz(matriz_entrada):
    matriz = []
    for fila_entrada in matriz_entrada:
        fila = []
        for entrada in fila_entrada:
            valor = entrada.get()
            if not valor.strip():
                messagebox.showerror("Error", "Por favor, complete todas las casillas.")
                return None
            fila.append(float(valor))
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz, label):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            label[i][j].config(text=str(matriz[i][j]))

def operar_matrices():
    matriz1 = obtener_valores_matriz(matriz_entrada1)
    matriz2 = obtener_valores_matriz(matriz_entrada2)

    if matriz1 is None or matriz2 is None:
        return

    if len(matriz1[0]) != len(matriz2):
        messagebox.showerror("Error", "El número de columnas de la Matriz A debe ser igual al número de filas de la Matriz B.")
        return

    if operacion.get() == "Suma":
        resultado = suma_matrices(matriz1, matriz2)
    elif operacion.get() == "Resta":
        resultado = resta_matrices(matriz1, matriz2)
    elif operacion.get() == "Producto":
        resultado = producto_matrices(matriz1, matriz2)
    else:
        messagebox.showerror("Error", "Operación no válida.")
        return

    mostrar_matriz(resultado, resultado_label)
    guardar_historial(f"Operación {operacion.get()}", resultado)

def suma_matrices(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz1[0])):
            suma = matriz1[i][j] + matriz2[i][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)
    return resultado

def resta_matrices(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz1[0])):
            resta = matriz1[i][j] - matriz2[i][j]
            fila_resultado.append(resta)
        resultado.append(fila_resultado)
    return resultado

def producto_matrices(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz2[0])):
            producto = 0
            for k in range(len(matriz2)):
                producto += matriz1[i][k] * matriz2[k][j]
            fila_resultado.append(producto)
        resultado.append(fila_resultado)
    return resultado
        
ventana = tk.Tk()
ventana.title("Operaciones de Matrices MAX 5X5")

frame_matriz1 = tk.Frame(ventana)
frame_matriz1.grid(row=0, column=0, padx=10)
frame_matriz2 = tk.Frame(ventana)
frame_matriz2.grid(row=0, column=2, padx=10)

label_matriz1 = tk.Label(frame_matriz1, text="Tamano matriz A:")
label_matriz1.grid(row=0, column=0)

fila1 = tk.IntVar()
columna1 = tk.IntVar()
entrada_fila1 = tk.Entry(frame_matriz1, textvariable=fila1, width=3)
entrada_fila1.grid(row=0, column=1)
entrada_columna1 = tk.Entry(frame_matriz1, textvariable=columna1, width=3)
entrada_columna1.grid(row=0, column=2)

boton_crear_matriz1 = tk.Button(frame_matriz1, text="Crear Matriz", command=lambda: crear_matriz1())
boton_crear_matriz1.grid(row=0, column=3)

label_matriz2 = tk.Label(frame_matriz2, text="Tamano matriz B")
label_matriz2.grid(row=0, column=0)

fila2 = tk.IntVar()
columna2 = tk.IntVar()
entrada_fila2 = tk.Entry(frame_matriz2, textvariable=fila2, width=3)
entrada_fila2.grid(row=0, column=1)
entrada_columna2 = tk.Entry(frame_matriz2, textvariable=columna2, width=3)
entrada_columna2.grid(row=0, column=2)

boton_crear_matriz2 = tk.Button(frame_matriz2, text="Crear Matriz", command=lambda: crear_matriz2())
boton_crear_matriz2.grid(row=0, column=3)

def crear_matriz1():
    global matriz_entrada1
    fila = fila1.get()
    columna = columna1.get()
    if fila > 0 and columna > 0 and fila <= 5 and columna <= 5:
        if 'matriz_entrada1' in globals():
            for fila in matriz_entrada1:
                for entrada in fila:
                    entrada.destroy()
        matriz_entrada1 = crear_matriz_entrada(frame_matriz1, fila, columna)

def crear_matriz2():
    global matriz_entrada2
    fila = fila2.get()
    columna = columna2.get()
    if fila > 0 and columna > 0 and fila <= 5 and columna <= 5:
        if 'matriz_entrada2' in globals():
            for fila in matriz_entrada2:
                for entrada in fila:
                    entrada.destroy()
        matriz_entrada2 = crear_matriz_entrada(frame_matriz2, fila, columna)

frame_operacion = tk.Frame(ventana)
frame_operacion.grid(row=1, column=0, columnspan=2, pady=10)

label_operacion = tk.Label(frame_operacion, text="Operación:")
label_operacion.grid(row=0, column=0)

operacion = tk.StringVar()
operacion.set(" Selecione operacion")

def seleccionar_operacion(event):
    operacion.set(event)

def guardar_historial(expresion, resultado):
    with open("historial_matriz.txt", "a") as archivo:
        archivo.write(f"{expresion} = {resultado}\n")
    try:
        repo = Repo(r"C:\Users\Lucho\final-algoritmos")
        repo.git.add("historial_matriz.txt")
        repo.git.commit("-m", "se actualizo historial de la calculadora de matriz")
        repo.git.push("origin")
        print("Historial actualizado y enviado a Git.")
    except Exception as e:
        print(f"Error al enviar a Git: {e}")        

menu_operacion = tk.OptionMenu(frame_operacion, operacion, "Suma", "Resta", "Producto")
menu_operacion.grid(row=0, column=1)

# Configura la función de selección para actualizar la variable operacion
menu_operacion.bind("<Configure>", lambda event: seleccionar_operacion(operacion.get()))

menu_operacion.grid(row=0, column=1)

boton_operar = tk.Button(frame_operacion, text="Operar", command=operar_matrices)
boton_operar.grid(row=0, column=2)

frame_resultado = tk.Frame(ventana)
frame_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

label_resultado = tk.Label(frame_resultado, text="Resultado:")
label_resultado.grid(row=0, column=0)

resultado_label = []
for i in range(5):
    fila_label = []
    for j in range(5):
        label = tk.Label(frame_resultado, text="", width=8)
        label.grid(row=i + 1, column=j)
        fila_label.append(label)
    resultado_label.append(fila_label)

ventana.mainloop()



