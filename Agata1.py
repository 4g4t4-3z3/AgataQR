import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import qrcode
from PIL import ImageTk, Image

def generar_qr():
    """Genera un QR con el texto proporcionado por el usuario y permite guardarlo."""
    mensaje = entry_text.get("1.0", tk.END).strip()
    if not mensaje:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un texto para generar el QR.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(mensaje)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")],
                                             title="Guardar QR como")
    if save_path:
        img.save(save_path)
        messagebox.showinfo("Éxito", f"El QR se ha guardado en: {save_path}")
    else:
        messagebox.showwarning("Cancelado", "No se guardó el QR.")

def actualizar_programa():
    """Actualiza el programa usando `git pull`."""
    try:
        # Ejecuta el comando git pull en el directorio actual
        result = subprocess.run(["git", "pull", "origin", "main"], capture_output=True, text=True)
        if "Already up to date." in result.stdout:
            messagebox.showinfo("Actualización", "El programa ya está actualizado.")
        else:
            messagebox.showinfo("Actualización", "El programa se actualizó correctamente. Reinicia para aplicar los cambios.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar el programa.\n{e}")

# Configuración principal de la ventana
root = tk.Tk()
root.title("Agata Faucets QR Generator")
root.geometry("800x750")
root.resizable(False, False)

# Título
label_title = tk.Label(root, text="Agata Faucets QR Generator", font=("Arial", 18, "bold"), fg="blue")
label_title.pack(pady=10)

# Texto de entrada
frame_text = tk.Frame(root)
frame_text.pack(pady=20)
scrollbar = tk.Scrollbar(frame_text)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
entry_text = tk.Text(frame_text, height=10, width=70, wrap=tk.WORD, yscrollcommand=scrollbar.set)
entry_text.pack()
scrollbar.config(command=entry_text.yview)

# Botones
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=20)

btn_generate = tk.Button(frame_buttons, text="Generar QR", font=("Arial", 12), bg="green", fg="white", command=generar_qr)
btn_generate.grid(row=0, column=0, padx=10)

btn_update = tk.Button(frame_buttons, text="Buscar Actualizaciones", font=("Arial", 12), bg="orange", fg="white", command=actualizar_programa)
btn_update.grid(row=0, column=1, padx=10)

btn_exit = tk.Button(frame_buttons, text="Salir", font=("Arial", 12), bg="red", fg="white", command=root.quit)
btn_exit.grid(row=0, column=2, padx=10)

# Inicializar la interfaz
root.mainloop()
