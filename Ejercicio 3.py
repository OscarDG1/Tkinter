import tkinter as tk
from tkinter import messagebox

def mostrar_info():
    messagebox.showinfo('Información', 'Este es un mensaje informativo.')

def mostrar_aviso():
    messagebox.showwarning('Aviso', 'Este es un mensaje de advertencia.')

def mostrar_error():
    messagebox.showerror('Error', 'Este es un mensaje de error.')

def preguntar():
    respuesta = messagebox.askquestion('Pregunta', '¿Deseas continuar?')
    resultado.set("Has clicado sí" if respuesta == 'yes' else "Has clicado no")

def preguntar_ok_cancel():
    respuesta = messagebox.askokcancel('Pregunta OK/Cancelar', '¿Estás seguro?')
    resultado.set("Has clicado sí" if respuesta else "Has clicado no")

def preguntar_yes_no():
    respuesta = messagebox.askyesno('Pregunta Sí/No', '¿Aceptas los términos?')
    resultado.set("Has clicado sí" if respuesta else "Has clicado no")

# Crear ventana
finestra = tk.Tk()
finestra.title("Ventanas Emergentes")

# Variable para almacenar la respuesta
resultado = tk.StringVar()

# Crear etiqueta para mostrar la respuesta
etiqueta_resultado = tk.Label(finestra, textvariable=resultado)
etiqueta_resultado.pack()

# Crear botones para mostrar diferentes tipos de ventanas emergentes
btn_info = tk.Button(finestra, text="Mostrar Información", command=mostrar_info)
btn_info.pack()

btn_aviso = tk.Button(finestra, text="Mostrar Aviso", command=mostrar_aviso)
btn_aviso.pack()

btn_error = tk.Button(finestra, text="Mostrar Error", command=mostrar_error)
btn_error.pack()

btn_pregunta = tk.Button(finestra, text="Pregunta", command=preguntar)
btn_pregunta.pack()

btn_ok_cancel = tk.Button(finestra, text="Pregunta OK/Cancelar", command=preguntar_ok_cancel)
btn_ok_cancel.pack()

btn_yes_no = tk.Button(finestra, text="Pregunta Sí/No", command=preguntar_yes_no)
btn_yes_no.pack()

# Iniciar la aplicación
finestra.mainloop()
