#!/bin/bash

# Variables
NOMBRE_PROGRAMA="Generador de QR"
RUTA_ICONO="$PWD/icono.ico"
RUTA_SCRIPT="$PWD/tu_script.py"
RUTA_DESTINO="/opt/generador_qr"
RUTA_DESKTOP="$HOME/.local/share/applications/generador_qr.desktop"

# Crear carpeta de destino
echo "Creando carpeta de instalación..."
sudo mkdir -p $RUTA_DESTINO

# Copiar archivos al destino
echo "Copiando archivos..."
sudo cp "$RUTA_SCRIPT" "$RUTA_ICONO" $RUTA_DESTINO

# Crear archivo .desktop
echo "Creando acceso directo..."
cat << EOF > $RUTA_DESKTOP
[Desktop Entry]
Version=1.0
Type=Application
Name=$NOMBRE_PROGRAMA
Exec=python3 $RUTA_DESTINO/tu_script.py
Icon=$RUTA_DESTINO/icono.ico
Terminal=false
EOF

# Dar permisos de ejecución
sudo chmod +x $RUTA_SCRIPT
chmod +x $RUTA_DESKTOP

echo "Instalación completada. Puedes encontrar '$NOMBRE_PROGRAMA' en tu menú de aplicaciones."
