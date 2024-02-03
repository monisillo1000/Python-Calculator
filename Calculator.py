import tkinter as tk

# Función para evaluar la expresión matemática
def calcular():
    try:
        expresion = entry.get()
        resultado = eval(expresion)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(resultado))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Función para agregar caracteres al campo de entrada
def agregar_caracter(caracter):
    entry.insert(tk.END, caracter)

# Función para borrar la entrada
def borrar():
    entry.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculator")
ventana.geometry("400x500")

# Campo de entrada
entry = tk.Entry(ventana, width=20, font=('Arial', 20), justify="right")
entry.grid(row=0, column=0, columnspan=5)

# Botones de la calculadora
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Agregar botones a la interfaz
for (texto, fila, columna) in botones:
    boton = tk.Button(ventana, text=texto, width=6, height=3, font=('Arial', 14), command=lambda t=texto: agregar_caracter(t))
    boton.grid(row=fila, column=columna)

# Botón "C" para borrar la entrada
borrar_button = tk.Button(ventana, text="C", width=6, height=3, font=('Arial', 14), command=borrar)
borrar_button.grid(row=0, column=5)

# Botón de igual para realizar el cálculo
igual_button = tk.Button(ventana, text="=", width=6, height=3, font=('Arial', 14), command=calcular)
igual_button.grid(row=4, column=3)

# Iniciar la aplicación
ventana.mainloop()
