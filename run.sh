#!/bin/bash
# Arranca Calenton con todas las variables de entorno necesarias

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
QGIS_PREFIX="$HOME/qgis-qt6"

export LD_LIBRARY_PATH="$SCRIPT_DIR/src/componentes/lib:$QGIS_PREFIX/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export PYTHONPATH="$QGIS_PREFIX/share/qgis/python${PYTHONPATH:+:$PYTHONPATH}"
export QGIS_PREFIX_PATH="$QGIS_PREFIX"

# Plugins y recursos de QGIS
export QT_PLUGIN_PATH="$QGIS_PREFIX/lib/qt6/plugins${QT_PLUGIN_PATH:+:$QT_PLUGIN_PATH}"
export GDAL_DATA="$QGIS_PREFIX/share/gdal"

exec python3 "$SCRIPT_DIR/src/calenton/calenton.py" "$@"
