import sqlite3
import tkinter as tk
import os

# Ruta al archivo de la base de datos
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_subdirectorio = "db"
ruta_completa = os.path.join(directorio_actual, ruta_subdirectorio, "basquet.db")


def insertar_datos():
    # Obtener los valores de las entradas
    nombre = Entry_nom.get()
    apellido = Entry_cognom.get()
    altura = Entry_alçada.get()
    edad = Entry_edat.get()

    # Conectar a la base de datos
    var_BD = sqlite3.connect(ruta_completa)
    cur_BD = var_BD.cursor()

    # Insertar los valores en la tabla "jugadores"
    cur_BD.execute("INSERT INTO jugadores (nom, cognom, alçada, edat) VALUES (?, ?, ?, ?)",
                   (nombre, apellido, altura, edad))

    # Guardar los cambios en la base de datos
    var_BD.commit()

    # Cerrar la conexión con la base de datos
    var_BD.close()

    # Limpiar las entradas
    Entry_nom.delete(0, tk.END)
    Entry_cognom.delete(0, tk.END)
    Entry_alçada.delete(0, tk.END)
    Entry_edat.delete(0, tk.END)

    # Llamar a la función para mostrar el contenido de la base de datos
    mostrar_contenido_base_de_datos()


def mostrar_contenido_base_de_datos():
    # Ruta al archivo de la base de datos
    var_BD = sqlite3.connect(ruta_completa)
    cur_BD = var_BD.cursor()

    # Ejecutar una consulta para seleccionar todos los campos y el identificador único (oid) de la tabla "jugadores"
    cur_BD.execute("SELECT *, oid FROM jugadores")

    # Obtener los datos en una variable
    var_dades = cur_BD.fetchall()

    # Imprimir el contenido de la base de datos en la consola
    for fila in var_dades:
        print(f"Contenido de la base de datos: {fila}")

    # Cerrar la conexión con la base de datos
    var_BD.close()


# Crear una ventana
ventana = tk.Tk()
ventana.title("Introducir Datos en la Base de Datos")

# Crear etiquetas y entradas
etiqueta_nom = tk.Label(ventana, text="Nombre:")
Entry_nom = tk.Entry(ventana)

etiqueta_cognom = tk.Label(ventana, text="Apellido:")
Entry_cognom = tk.Entry(ventana)

etiqueta_alçada = tk.Label(ventana, text="Altura:")
Entry_alçada = tk.Entry(ventana)

etiqueta_edat = tk.Label(ventana, text="Edad:")
Entry_edat = tk.Entry(ventana)

# Crear botón para introducir datos
boton_introducir = tk.Button(ventana, text="Enviar datos",bg="red", command=insertar_datos)

# Organizar widgets en la ventana
etiqueta_nom.pack()
Entry_nom.pack()
etiqueta_cognom.pack()
Entry_cognom.pack()
etiqueta_alçada.pack()
Entry_alçada.pack()
etiqueta_edat.pack()
Entry_edat.pack()
boton_introducir.pack()

# Iniciar la ventana
ventana.mainloop()
