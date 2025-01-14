import os
import sys
import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas

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

    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("PDF files", "*.pdf")],
        title="Guardar QR como"
    )
    if save_path:
        if save_path.endswith(".png"):
            img.save(save_path)
            messagebox.showinfo("Éxito", f"El QR se ha guardado como PNG en: {save_path}")
        elif save_path.endswith(".pdf"):
            pdf = canvas.Canvas(save_path)
            img_path = "temp_qr.png"
            img.save(img_path)
            pdf.drawImage(img_path, 100, 500, 200, 200)  # Ajusta las coordenadas y tamaño del QR
            pdf.save()
            os.remove(img_path)
            messagebox.showinfo("Éxito", f"El QR se ha guardado como PDF en: {save_path}")
        else:
            messagebox.showwarning("Formato no válido", "Selecciona un formato válido (PNG o PDF).")
    else:
        messagebox.showwarning("Cancelado", "No se guardó el QR.")

def actualizar_programa():
    """Actualiza el programa usando `git pull` y reinicia la aplicación."""
    try:
        result = subprocess.run(["git", "pull", "origin", "main"], capture_output=True, text=True)
        if "Already up to date." in result.stdout:
            messagebox.showinfo("Actualización", "El programa ya está actualizado.")
        else:
            messagebox.showinfo("Actualización", "El programa se actualizó correctamente. Reiniciando...")
            root.destroy()  # Cierra la ventana actual
            os.execl(sys.executable, sys.executable, *sys.argv)  # Reinicia el programa
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar el programa.\n{e}")


def cambiar_idioma(idioma):
    """Cambia los textos de la interfaz según el idioma seleccionado."""
    textos = {
        "es": {
            "title": "Generador de QR de Agata Faucets",
            "generate": "Generar ",
            "update": "Buscar Actualizaciones",
            "exit": "Salir",
            "about": "Acerca de",
            "info": "Este programa genera códigos QR a partir de texto."
        },
        "en": {
            "title": "Agata Faucets QR Generator",
            "generate": "Generate QR",
            "update": "Check for Updates",
            "exit": "Exit",
            "about": "About",
            "info": "This program generates QR codes from text."
        }
    }

    lang = textos.get(idioma, textos["es"])
    root.title(lang["title"])
    label_title.config(text=lang["title"])
    btn_generate.config(text=lang["generate"])
    btn_update.config(text=lang["update"])
    btn_exit.config(text=lang["exit"])
    menu_about.entryconfig(0, label=lang["about"])
    menu_about.entryconfig(1, label=lang["info"])

# Configuración principal de la ventana
root = tk.Tk()
root.title("Agata Faucets QR Generator")
root.geometry("800x600")
root.resizable(False, False)

# Menú superior
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
menu_about = tk.Menu(menu_bar, tearoff=0)
menu_about.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Este programa genera códigos QR a partir de texto."))
menu_about.add_command(label="Info", command=lambda: messagebox.showinfo("Info", "Generador de QR por Agata Faucets"))
menu_bar.add_cascade(label="Ayuda", menu=menu_about)

menu_language = tk.Menu(menu_bar, tearoff=0)
menu_language.add_command(label="Español", command=lambda: cambiar_idioma("es"))
menu_language.add_command(label="English", command=lambda: cambiar_idioma("en"))
menu_bar.add_cascade(label="Idioma", menu=menu_language)

# Título
label_title = tk.Label(root, text="Agata Faucets QR Generator", font=("Arial", 18, "bold"), fg="blue")
label_title.pack(pady=10)

# Texto de entrada
frame_text = tk.Frame(root)
frame_text.pack(pady=20)
scrollbar = tk.Scrollbar(frame_text)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
entry_text = tk.Text(frame_text, height=15, width=70, wrap=tk.WORD, yscrollcommand=scrollbar.set)
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

# Marca registrada
label_footer = tk.Label(root, text="© 2025 Agata Faucets-Todos los derechos reservados\n Desarrollado por: Ezequiel Tauil", font=("Arial", 10), fg="gray")
label_footer.pack(side=tk.BOTTOM, pady=10)

# Inicializar la interfaz
root.mainloop()
