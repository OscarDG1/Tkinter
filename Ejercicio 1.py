import tkinter as tk

#Variables
operacion = None
num1 = None

#Metodos

def clear():
    quadre_text.delete(0, tk.END)

def operar(tipo):
    global operacion
    global num1
    num1 = float(quadre_text.get())
    operacion = tipo
    clear()

def igual():
    global operacion
    num2 = float(quadre_text.get())
    clear()
    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        resultado = num1 / num2
    else:
        resultado = num2  # En caso de ninguna operación seleccionada
    quadre_text.insert(0, str(resultado))

finestra = tk.Tk()
finestra.title('Calculadora Simple')

quadre_text = tk.Entry(finestra, borderwidth=2)
quadre_text.pack()

for i in range(10):
    boton_numero = tk.Button(finestra, text=str(i), command=lambda i=i: quadre_text.insert(tk.END, str(i)))
    boton_numero.pack(side=tk.LEFT)

boton_suma = tk.Button(finestra, text='+', command=lambda: operar("+"))
boton_suma.pack(side=tk.LEFT)

boton_resta = tk.Button(finestra, text='-', command=lambda: operar("-"))
boton_resta.pack(side=tk.LEFT)

boton_multiplicacion = tk.Button(finestra, text='*', command=lambda: operar("*"))
boton_multiplicacion.pack(side=tk.LEFT)

boton_division = tk.Button(finestra, text='/', command=lambda: operar("/"))
boton_division.pack(side=tk.LEFT)

boton_igual = tk.Button(finestra, text='=', command=igual)
boton_igual.pack(side=tk.LEFT)

boton_clear = tk.Button(finestra, text='C', command=clear)
boton_clear.pack(side=tk.LEFT)

finestra.mainloop()
