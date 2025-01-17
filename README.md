# AgataQR
Agata Faucets Generator QR

Agata Faucets Generator QR es una herramienta intuitiva y fácil de usar para generar códigos QR personalizados. Este programa permite a los usuarios ingresar las piezas o mensajes que quieres que sean privados, y luego genera un código QR que puede ser escaneado para acceder a esa información de manera rápida y eficiente.
Características

    Generación de QR: Permite ingresar texto con instrucciones o mensajes que quieres que sean privados, y luego genera un código QR que almacena dicha información.

    Interfaz Gráfica Intuitiva: Con una interfaz limpia y profesional, los usuarios pueden ingresar texto fácilmente y generar los QR sin complicaciones. La ventana tiene un tamaño fijo y opciones claras para realizar cada acción.

    Selección de Carpeta de Destino: Los usuarios pueden seleccionar la carpeta donde desean guardar el código QR generado, facilitando la organización de los archivos.

    Actualización Automática: El programa incluye una opción para verificar si hay actualizaciones disponibles directamente desde GitHub, lo que asegura que siempre estés utilizando la última versión.

    Formatos de Exportación: Los QR generados se guardan en formato PNG, pero se pueden agregar opciones para exportar en otros formatos como PDF en futuras versiones.

    Fácil de Usar: La herramienta está diseñada para ser simple y accesible, sin necesidad de configuraciones complejas, lo que la convierte en una opción ideal para quienes buscan eficiencia en el proceso de creación de códigos QR.

Requisitos

    Python 3.x
    Tkinter (Para la interfaz gráfica)
    Pillow (Para manejar imágenes)
    qrcode (Para generar los códigos QR)
    En Windows: winshell (para el script de instalación).

Instalación

Clona este repositorio en tu máquina local:

    git clone https://github.com/4g4t4-3z3/AgataQR.git

Instala las dependencias necesarias:

    pip install -r requirements.txt

Ejecuta el programa:

    python QRGenerator.py

Opcional: Instalación del programa con acceso directo

Si prefieres que el programa tenga un acceso directo y se ejecute como cualquier otra aplicación, sigue estas instrucciones según tu sistema operativo:
Linux

Ejecuta el script de instalación para Linux:

    chmod +x setupLinux.sh
    ./setupLinux.sh

Esto creará un acceso directo en tu menú de aplicaciones. Busca QRGo y ejecútalo.

El ícono personalizado (icono.ico) y el programa se instalarán automáticamente en las rutas adecuadas.

Windows

Ejecuta el script de instalación para Windows:

    python setupWindows.py

Esto creará un acceso directo en tu escritorio con el ícono personalizado.
Si el módulo winshell no está instalado, instálalo primero:

    pip install winshell



Contribuciones

Si tienes sugerencias, mejoras o correcciones, no dudes en abrir un "issue" o enviar un "pull request". ¡Toda contribución es bienvenida!

Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.
