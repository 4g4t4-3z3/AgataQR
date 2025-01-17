#!/bin/bash

# Variables
NOMBRE_PROGRAMA="QRGenerate"
RUTA_ICONO="$PWD/qrgo.ico"
RUTA_SCRIPT="$PWD/QRGenerate.py"
RUTA_DESTINO="/opt/AgataQR"
RUTA_DESKTOP="$HOME/.local/share/applications/QRGenerate.desktop"

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
Exec=/usr/bin/python3 $RUTA_DESTINO/QRGenerate.py
Icon=$RUTA_DESTINO/qrgo.ico
Terminal=false
EOF

# Dar permisos de ejecución
sudo chmod +x $RUTA_SCRIPT
chmod +x $RUTA_DESKTOP

# Actualizar caché de aplicaciones
update-desktop-database ~/.local/share/applications/

echo "Instalación completada. Puedes encontrar '$NOMBRE_PROGRAMA' en tu menú de aplicaciones."

