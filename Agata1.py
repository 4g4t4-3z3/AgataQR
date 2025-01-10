import tkinter as tk
from tkinter import messagebox
import qrcode
import os
from tkinter.filedialog import askdirectory
from PIL import ImageTk, Image
import webbrowser

# Función para generar el QR
def generar_qr():
    mensaje = entrada_texto.get("1.0", "end-1c")  # Obtenemos el texto ingresado en el Text widget
    if not mensaje.strip():  # Validamos si el mensaje está vacío
        messagebox.showwarning("Advertencia", "Por favor ingresa el mensaje para generar el QR.")
        return
    
    print("\n[ Generando tu QR... ]")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(mensaje)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Selección de carpeta de destino
    carpeta_destino = askdirectory(title="Seleccionar carpeta de destino")
    if carpeta_destino:
        nombre_archivo = f"{carpeta_destino}/Receta_Lavatorio_Monocomando.png"
        img.save(nombre_archivo)
        print(f"\n✅ Tu QR ha sido guardado como '{nombre_archivo}'.")
        messagebox.showinfo("Éxito", f"El QR fue guardado en: {nombre_archivo}")
    else:
        messagebox.showerror("Error", "No se seleccionó una carpeta de destino.")

# Función para actualizar el programa
def buscar_actualizaciones():
    url_github = "https://github.com/TuUsuario/TuRepositorio"
    messagebox.showinfo("Actualización", "Revisando actualizaciones en GitHub...")
    webbrowser.open(url_github)

# Función para salir del programa
def salir():
    ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agata Faucets Generator QR")
ventana.geometry("800x550")
ventana.resizable(False, False)  # Para que no se pueda redimensionar

# Colores y fuentes personalizadas
ventana.config(bg="#f0f0f0")

# Crear un marco superior con el título
marco_titulo = tk.Frame(ventana, bg="#2196F3", padx=20, pady=10)
marco_titulo.pack(fill="x")
titulo = tk.Label(marco_titulo, text="Agata Faucets Generator QR", font=("Arial", 18, "bold"), fg="white", bg="#2196F3")
titulo.pack()

# Crear el área de texto para ingresar el mensaje
texto_label = tk.Label(ventana, text="Escribe la receta del producto:", font=("Arial", 12), bg="#f0f0f0")
texto_label.pack(pady=10)
entrada_texto = tk.Text(ventana, height=10, width=50, font=("Arial", 12))
entrada_texto.pack(pady=10)

# Crear botones con iconos
boton_qr = tk.Button(ventana, text="Generar QR", font=("Arial", 12), bg="#4CAF50", fg="white", command=generar_qr)
boton_qr.pack(pady=10)

boton_actualizar = tk.Button(ventana, text="Buscar Actualizaciones", font=("Arial", 12), bg="#FF9800", fg="white", command=buscar_actualizaciones)
boton_actualizar.pack(pady=10)

boton_salir = tk.Button(ventana, text="Salir", font=("Arial", 12), bg="#F44336", fg="white", command=salir)
boton_salir.pack(pady=10)

# Mostrar la ventana
ventana.mainloop()
