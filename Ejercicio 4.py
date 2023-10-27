import tkinter as tk
from tkinter import filedialog as quelcom
from tkinter import Toplevel
from tkinter.filedialog import asksaveasfile
from PIL import Image, ImageTk
import os

# Variable global para almacenar la imagen
imagen_tk = None


# Función para abrir y mostrar una imagen en una ventana secundaria
def abrir_archivo_imagen():
    global imagen_tk
    archivo = quelcom.askopenfilename(filetypes=[("Imágenes", "*.jpg *.png *.gif *.bmp *.ppm *.pgm *.pbm")])
    if archivo:
        nombre_archivo = os.path.basename(archivo)

        ventana_imagen = Toplevel()
        ventana_imagen.title("Imagen Seleccionada")

        etiqueta_path = tk.Label(ventana_imagen, text=f"Ruta de la imagen: {archivo}")
        etiqueta_path.pack()

        etiqueta_nombre = tk.Label(ventana_imagen, text=f"Nombre del archivo: {nombre_archivo}")
        etiqueta_nombre.pack()

        imagen = Image.open(archivo)
        imagen = imagen.resize((400, 400))  # Ajusta el tamaño de la imagen según tus necesidades
        imagen_tk = ImageTk.PhotoImage(imagen)

        etiqueta = tk.Label(ventana_imagen, image=imagen_tk)
        etiqueta.pack()

        # Agregar botón para guardar la imagen con otro nombre
        boton_guardar = tk.Button(ventana_imagen, text="Guardar como...", command=lambda: guardar_imagen(imagen))
        boton_guardar.pack()


# Función para guardar la imagen con otro nombre
def guardar_imagen(imagen):
    opciones = {
        'defaultextension': '.jpg',
        'filetypes': [("Imágenes", "*.jpg *.png *.gif *.bmp *.ppm *.pgm *.pbm")],
        'initialfile': 'nueva_imagen.jpg',
    }

    archivo_guardado = asksaveasfile(**opciones)
    if archivo_guardado:
        imagen.save(archivo_guardado.name)
        archivo_guardado.close()


# Crear ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Abrir Archivo de Imagen")

# Botón para abrir archivo de imagen
boton_abrir = tk.Button(ventana_principal, text="Abrir Imagen", command=abrir_archivo_imagen)
boton_abrir.pack()

# Iniciar la aplicación
ventana_principal.mainloop()
