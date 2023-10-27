import tkinter as tk
from PIL import Image, ImageTk
import os


script_directory = os.path.dirname(os.path.abspath(__file__))
# Lista de rutas de imágenes
ruta_imagenes = [
    os.path.join(script_directory, "fotos", "fondo1.jpg"),
    os.path.join(script_directory, "fotos", "fondo2.jpg"),
    os.path.join(script_directory, "fotos", "fondo3.jpg"),
    os.path.join(script_directory, "fotos", "fondo4.jpg"),
    os.path.join(script_directory, "fotos", "fondo5.jpg")
]

# Variables globales
imagen_actual = 0  # Índice de la imagen actual
imagen = None  # Variable global para la imagen
imagen_label = None  # Etiqueta para mostrar la imagen actual
total_imagenes = len(ruta_imagenes)  # Número total de imágenes


# Función para mostrar la imagen actual
def mostrar_imagen():
    global imagen_label
    global imagen
    imagen = Image.open(ruta_imagenes[imagen_actual])
    imagen = ImageTk.PhotoImage(imagen)
    if imagen_label:
        imagen_label.grid_forget()
    imagen_label = tk.Label(finestra, image=imagen, bd=2, relief=tk.SUNKEN)
    imagen_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W + tk.E)
    actualizar_texto()


# Función para mostrar la imagen siguiente
def imagen_siguiente():
    global imagen_actual
    if imagen_actual < len(ruta_imagenes) - 1:
        imagen_actual += 1
        mostrar_imagen()
    actualizar_botones()


# Función para mostrar la imagen anterior
def imagen_anterior():
    global imagen_actual
    if imagen_actual > 0:
        imagen_actual -= 1
        mostrar_imagen()
    actualizar_botones()


# Función para actualizar la habilitación de los botones
def actualizar_botones():
    if imagen_actual == 0:
        boton_anterior.config(state=tk.DISABLED)
    else:
        boton_anterior.config(state=tk.NORMAL)
    if imagen_actual == len(ruta_imagenes) - 1:
        boton_siguiente.config(state=tk.DISABLED)
    else:
        boton_siguiente.config(state=tk.NORMAL)


# Función para actualizar el texto "Imatge x de total"
def actualizar_texto():
    texto = f'Imagen {imagen_actual + 1} de {total_imagenes}'
    etiqueta_texto.config(text=texto)


finestra = tk.Tk()
finestra.title('Visor de Imágenes')

boton_salir = tk.Button(finestra, text='Salir', command=finestra.quit, bg='black', fg='white', width=10, height=1)
boton_siguiente = tk.Button(finestra, text='Siguiente', command=imagen_siguiente)
boton_anterior = tk.Button(finestra, text='Atras', command=imagen_anterior)

etiqueta_texto = tk.Label(finestra, anchor=tk.E)
etiqueta_texto.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W + tk.E)

mostrar_imagen()

# Colocar botones
boton_salir.grid(row=3, column=0, padx=10, pady=10)
boton_anterior.grid(row=3, column=1, padx=10, pady=10)
boton_siguiente.grid(row=3, column=2, padx=10, pady=10)

# Actualizar la habilitación de los botones inicialmente
actualizar_botones()

# Iniciar la aplicación
finestra.mainloop()
