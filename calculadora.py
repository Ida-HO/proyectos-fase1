import tkinter as tk

def click(boton):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + str(boton))

def borrar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.configure(bg="#666565")  

entrada = tk.Entry(
    ventana, width=25, borderwidth=5,
    font=('Arial', 16), justify='right',
    bg="#776D41", fg="white", insertbackground="white"
)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

color_boton = "#4F4F4F"
color_texto = "white"

botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

for (texto, fila, columna) in botones:
    if texto == '=':
        tk.Button(
            ventana, text=texto, width=10, height=2,
            command=calcular, bg=color_boton, fg=color_texto, font=('Arial', 12, 'bold')
        ).grid(row=fila, column=columna, padx=2, pady=2)
    elif texto == 'C':
        tk.Button(
            ventana, text=texto, width=45, height=2,
            command=borrar, bg=color_boton, fg=color_texto, font=('Arial', 12, 'bold')
        ).grid(row=fila, column=columna, columnspan=4, padx=2, pady=2)
    else:
        tk.Button(
            ventana, text=texto, width=10, height=2,
            command=lambda t=texto: click(t), bg=color_boton, fg=color_texto, font=('Arial', 12, 'bold')
        ).grid(row=fila, column=columna, padx=2, pady=2)

ventana.mainloop()