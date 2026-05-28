#!/bin/bash
# Arranca Calenton con todas las variables de entorno necesarias

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Debian: QGIS instalado en /usr
# Otra opción (compilado manualmente): QGIS_PREFIX="$HOME/qgis-qt6"
QGIS_PREFIX="/usr"

export LD_LIBRARY_PATH="$SCRIPT_DIR/src/componentes/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export PYTHONPATH="$SCRIPT_DIR/src/componentes/build/ts/build/lib.linux-x86_64-cpython-313:/usr/lib/python3/dist-packages${PYTHONPATH:+:$PYTHONPATH}"
export QGIS_PREFIX_PATH="$QGIS_PREFIX"

# Plugins y recursos de QGIS
export GDAL_DATA="$QGIS_PREFIX/share/gdal"
export QT_ACCESSIBILITY=0
export QT_QPA_PLATFORM=xcb  # fuerza X11, evita conflicto con WAYLAND_DISPLAY en entorno mixto

exec python3 "$SCRIPT_DIR/src/calenton/calenton.py" "$@"
