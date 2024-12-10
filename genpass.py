import tkinter as tk
from tkinter import messagebox
import string
import random

# Función para generar la contraseña
def generar_contrasena():
    try:
        # Ocultar el mensaje de "Copiada con éxito"
        label_mensaje.config(text="", fg="green")

        longitud = int(entry_longitud.get())  # Obtiene la longitud de la entrada
        if longitud <= 0:
            raise ValueError("La longitud debe ser mayor que 0")
        
        caracteres = string.ascii_letters + string.digits + string.punctuation + "ñÑ"
        contrasena = "".join(random.choice(caracteres) for i in range(longitud))
        entry_contrasena.delete(0, tk.END)  # Limpia el campo de contraseña
        entry_contrasena.insert(0, contrasena)  # Muestra la contraseña generada
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido para la longitud")

# Función para copiar la contraseña al portapapeles
def copiar_contrasena():
    contrasena = entry_contrasena.get()
    if contrasena:
        ventana.clipboard_clear()  # Limpia el portapapeles
        ventana.clipboard_append(contrasena)  # Copia la contraseña
        ventana.update()  # Actualiza el portapapeles
        
        # Muestra el mensaje de "Copiada con éxito"
        label_mensaje.config(text="¡Copiada con éxito!", fg="green")
    else:
        messagebox.showwarning("Advertencia", "No hay ninguna contraseña para copiar")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas Seguras")
ventana.geometry("450x300")
ventana.resizable(False, False)

# Etiqueta y entrada para la longitud
label_longitud = tk.Label(ventana, text="Tamaño de la contraseña:", font=("Arial", 12))
label_longitud.pack(pady=10)
entry_longitud = tk.Entry(ventana, font=("Arial", 12), width=10)
entry_longitud.pack()

# Botón para generar la contraseña
btn_generar = tk.Button(ventana, text="Generar Contraseña", font=("Arial", 12), command=generar_contrasena)
btn_generar.pack(pady=10)

# Etiqueta y entrada para mostrar la contraseña generada
label_contrasena = tk.Label(ventana, text="Contraseña generada:", font=("Arial", 12))
label_contrasena.pack(pady=10)

frame_contrasena = tk.Frame(ventana)  # Crear un marco para alinear entrada y botón
frame_contrasena.pack()

entry_contrasena = tk.Entry(frame_contrasena, font=("Arial", 12), width=30)
entry_contrasena.grid(row=0, column=0)

btn_copiar = tk.Button(frame_contrasena, text="Copiar", font=("Arial", 10), command=copiar_contrasena)
btn_copiar.grid(row=0, column=1, padx=10)

# Etiqueta para mostrar mensajes (como "Copiada con éxito")
label_mensaje = tk.Label(ventana, text="", font=("Arial", 10))
label_mensaje.pack(pady=10)

# Inicia el bucle de la interfaz
ventana.mainloop()
