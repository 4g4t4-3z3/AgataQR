import os
import winshell
import shutil

def instalar_programa():
    nombre_programa = "Generador de QR"
    ruta_origen = os.path.dirname(os.path.abspath(__file__))
    ruta_destino = os.path.join("C:\\", "Generador_QR")
    ruta_icono = os.path.join(ruta_destino, "qrgo.ico")
    ruta_script = os.path.join(ruta_destino, "QRGenerate.py")
    ruta_acceso_directo = os.path.join(winshell.desktop(), f"{nombre_programa}.lnk")

    # Crear carpeta de destino
    if not os.path.exists(ruta_destino):
        os.makedirs(ruta_destino)

    # Copiar archivos al destino
    shutil.copyfile(os.path.join(ruta_origen, "QRGenerate.py"), ruta_script)
    shutil.copyfile(os.path.join(ruta_origen, "qrgo.ico"), ruta_icono)

    # Crear acceso directo
    with winshell.shortcut(ruta_acceso_directo) as acceso_directo:
        acceso_directo.path = f"python {ruta_script}"
        acceso_directo.icon_location = ruta_icono
        acceso_directo.description = nombre_programa

    print("Instalación completada. Acceso directo creado en el escritorio.")

if __name__ == "__main__":
    instalar_programa()
