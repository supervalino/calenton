# Calenton — Herramienta de Inventario de Emisiones

**Calenton** es una aplicación de escritorio para calcular, gestionar y elaborar informes sobre emisiones de contaminantes atmosféricos procedentes de múltiples tipos de fuentes. Fue desarrollada por LITEC (Laboratorio de Investigación en Tecnologías de la Combustión — CSIC) y Trustserver SL (2009–2010).

La herramienta está diseñada para analistas medioambientales que necesitan:

- Gestionar múltiples **escenarios** de inventario (diferentes años normativos o metodologías)
- Incorporar datos de medición de instalaciones industriales, redes de transporte, fuentes agrícolas, etc.
- Calcular emisiones de contaminantes mediante fórmulas JavaScript flexibles definidas por el usuario
- Agregar resultados a zonas geográficas administrativas (municipio, provincia, comunidad autónoma)
- Generar tablas y gráficas de calidad para informes basados en LaTeX

---

## Índice

1. [Cómo funciona](#cómo-funciona)
2. [Requisitos y dependencias](#requisitos-y-dependencias)
3. [Instalación](#instalación)
4. [Configuración de la base de datos](#configuración-de-la-base-de-datos)
5. [Ejecución de la aplicación](#ejecución-de-la-aplicación)
6. [Guía de uso](#guía-de-uso)
7. [Generación de informes](#generación-de-informes)
8. [Importación de datos mediante CSV](#importación-de-datos-mediante-csv)
9. [Estructura del proyecto](#estructura-del-proyecto)
10. [Conceptos clave](#conceptos-clave)

---

## Cómo funciona

Calenton sigue un flujo de cálculo **basado en escenarios y fórmulas**:

```
Escenario
  └── Fuentes de datos (fuentes)
        └── Puntos de medición / instalaciones (aforós)
              ├── Datos de entrada (valordato)    ← consumo de combustible, conteo de vehículos, etc.
              ├── Parámetros (parametro)           ← factores de emisión con sobreescritura por zona
              └── Fórmulas (formula)               ← expresiones JavaScript que producen:
                    └── Emisiones (contaminanteaforo)   ← por contaminante, por punto
                          └── Agregadas por zona (contaminantezona)  ← resultado final
```

**Pasos del flujo de cálculo:**

1. Un *escenario* agrupa toda la configuración de un inventario (p. ej., "España 2020 SNAP").
2. Las *fuentes de datos* vinculan puntos de medición con un motor de cálculo y un esquema de clasificación (SNAP, IPCC, …).
3. Para cada *punto de medición* (aforo), el usuario registra *valores de datos* (p. ej., consumo anual de combustible en GJ).
4. Las *fórmulas* expresadas en JavaScript transforman esos valores —junto con los *parámetros* del escenario (factores de emisión, constantes de conversión)— en cantidades de contaminantes.
5. Los parámetros admiten una jerarquía de sobreescritura de tres niveles: escenario → zona → punto de medición.
6. Una *matriz de distribución espacial* (`mapaforozona`) distribuye las emisiones de cada punto de medición entre una o más zonas administrativas por porcentaje (útil para carreteras que atraviesan varios municipios).
7. El motor de cálculo escribe los resultados en `contaminanteaforo` (por punto) y `contaminantezona` (agregado por zona, fuente y clasificación).
8. El subsistema de informes lee esas tablas y genera gráficas `.eps` y tablas `.tex` listas para incluir en documentos LaTeX.

---

## Requisitos y dependencias

### Distribuciones soportadas

Calenton requiere **QGIS 4.x compilado contra Qt6** (`python3-qgis` Qt6). A mayo de 2026, los sistemas donde esto está disponible son:

| Sistema | Estado |
|---|---|
| **Ubuntu 24.04 LTS** (noble) | Funciona — repo oficial QGIS |
| **Debian 13** (trixie) | Funciona — repo oficial QGIS |
| Debian sid/forky | Bloqueado — conflicto de dependencias GDAL |
| Ubuntu 22.04 / Debian 12 | Bloqueado — solo QGIS Qt5 disponible |

### Paquetes del sistema (Ubuntu 24.04 / Debian trixie)

```bash
# Añadir el repo oficial de QGIS (necesario para obtener QGIS 4.x Qt6)
sudo mkdir -p /etc/apt/keyrings
sudo wget -O /etc/apt/keyrings/qgis-archive-keyring.gpg \
    https://download.qgis.org/downloads/qgis-archive-keyring.gpg

# Crear /etc/apt/sources.list.d/qgis.sources con el codename de tu distro:
# noble  → Ubuntu 24.04
# trixie → Debian 13
sudo tee /etc/apt/sources.list.d/qgis.sources <<'EOF'
Types: deb deb-src
URIs: https://qgis.org/debian
Suites: noble
Architectures: amd64
Components: main
Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg
EOF

sudo apt update

# PostgreSQL con extensión espacial PostGIS
sudo apt install postgresql postgis

# QGIS 4.x con Qt6
sudo apt install qgis python3-qgis

# Dependencias Python
sudo apt install python3-pyqt6 python3-cairo

# Librerías gráficas para la generación de informes
pip install pycha pychart configobj
```

### Compilación local obligatoria

**No se distribuyen ejecutables precompilados.** El código fuente debe compilarse en la máquina de destino antes de poder ejecutar la aplicación. Hay dos componentes que compilar:

**1. Librería C++ y módulo Python `ts` (`src/componentes/`)**

Un único build produce dos artefactos, ambos necesarios:

- `src/componentes/lib/libcomponentes.so` — la librería compartida C++ que se carga en tiempo de ejecución
- `src/componentes/sip/generated/ts.so` — el módulo de extensión Python (`import ts`) que expone los widgets y modelos de tabla a la aplicación

```bash
cd src/componentes
pip install sip build
python -m build
```

`run.sh` añade `src/componentes/lib/` a `LD_LIBRARY_PATH` automáticamente. También hay que asegurarse de que `src/componentes/sip/generated/` (o donde quede `ts.so` tras el build) esté en `PYTHONPATH` para que Python pueda importarlo.

> **Nota:** Los ficheros `.so` compilados no se incluyen en el repositorio — son binarios específicos de arquitectura. Cada máquina debe compilar desde el código fuente.

### Resumen de paquetes Python

| Paquete | Finalidad |
|---|---|
| `PyQt6` | Framework de interfaz gráfica |
| `qgis` (API Python) | Renderizado de mapas |
| `pycha` / `pychart` | Generación de gráficas en informes |
| `cairo` | Renderizado de gráficas EPS |
| `configobj` | Lectura de configuración `.dat` de informes |
| `sip >= 6, < 7` | Enlace C++ para `componentes` |

---

## Instalación

### 1. Obtener el código fuente

```bash
git clone <url-del-repositorio> calenton
cd calenton
```

### 2. Compilar la librería de widgets C++

```bash
cd src/componentes
python -m build
cd ../..
```

Verificar que `src/componentes/lib/libcomponentes.so` existe tras la compilación.

### 3. Instalar el módulo `ts`

Colocar o instalar el paquete Python `ts` de forma que sea importable. Si existe un directorio `ts/` en el proyecto:

```bash
export PYTHONPATH="$PWD/src:$PYTHONPATH"
```

O instalarlo con pip si se proporciona `setup.py` / `pyproject.toml`.

### 4. Configurar QGIS

El script lanzador (`run.sh`) espera una instalación Qt6 de QGIS en `$HOME/qgis-qt6`. Si QGIS está instalado en el sistema, modificar la variable `QGIS_PREFIX` en `run.sh`:

```bash
# En run.sh, cambiar:
QGIS_PREFIX="$HOME/qgis-qt6"
# por la ruta donde está instalado QGIS, p. ej.:
QGIS_PREFIX="/usr"
```

---

## Configuración de la base de datos

Calenton utiliza **PostgreSQL con PostGIS**. Los pasos siguientes crean la base de datos `emisiones` desde cero.

### 1. Crear un usuario PostgreSQL (si es necesario)

```bash
sudo -u postgres createuser --superuser $USER
```

### 2. Crear la base de datos

```bash
dropdb --if-exists emisiones
createdb -E UTF-8 emisiones
```

### 3. Activar PostGIS y PL/pgSQL

```bash
psql emisiones -c "CREATE EXTENSION IF NOT EXISTS postgis;"
psql emisiones -c "CREATE EXTENSION IF NOT EXISTS plpgsql;"
```

### 4. Cargar el esquema

```bash
psql emisiones < sql/calenton.sql   # Tablas, secuencias, restricciones
psql emisiones < sql/codigo.sql     # Funciones PL/pgSQL y disparadores
psql emisiones < sql/datos.sql      # Datos iniciales (clasificación SNAP, motores de cálculo)
```

### 5. Crear el esquema de trabajo para datos temporales

```bash
psql emisiones -c "CREATE SCHEMA IF NOT EXISTS temp AUTHORIZATION $USER;"
```

### 6. (Opcional) Asignar contraseña a la base de datos

```bash
psql emisiones -c "ALTER USER $USER WITH PASSWORD 'tu-contraseña';"
```

### Restauración desde una copia de seguridad

Si se dispone de un volcado `pg_dump`:

```bash
# Copia de seguridad en formato personalizado:
pg_restore -F c -d emisiones copia.dmp

# Copia de seguridad en SQL plano:
psql emisiones -f copia.sql
```

---

## Ejecución de la aplicación

```bash
./run.sh
```

El script lanzador:
1. Determina el directorio raíz del proyecto.
2. Establece `LD_LIBRARY_PATH` para incluir `src/componentes/lib/` y las librerías de QGIS.
3. Establece `PYTHONPATH` para incluir la API Python de QGIS.
4. Configura `QT_PLUGIN_PATH` y `GDAL_DATA` para QGIS.
5. Ejecuta `python3 src/calenton/calenton.py`.

Si el script no tiene permisos de ejecución:

```bash
chmod +x run.sh
./run.sh
```

---

## Guía de uso

La aplicación se abre como una ventana MDI (Interfaz de Documentos Múltiples). El flujo habitual para un nuevo inventario es el siguiente:

### Paso 1 — Crear un Escenario

*Menú: Escenario → Nuevo*

Un escenario agrupa toda la configuración de una instancia de inventario (p. ej., "Aragón 2022 SNAP"). Cada escenario es independiente; los parámetros y resultados no se comparten entre escenarios.

### Paso 2 — Definir jerarquías de clasificación

*Menú: Clasificación → Editar*

Cargar o definir un esquema de clasificación como SNAP (Nomenclatura Seleccionada para Contaminantes Atmosféricos) o IPCC. El árbol es jerárquico: sector SNAP → subsector → actividad. Los datos SNAP precargados se incluyen en `sql/datos.sql`.

### Paso 3 — Añadir contaminantes

*Menú: Contaminantes → Editar*

Definir los contaminantes que se van a seguir (CO₂, CH₄, NOₓ, PM₁₀, COVNM, …) y opcionalmente configurar factores de equivalencia de CO₂ para cálculos de potencial de calentamiento global.

### Paso 4 — Configurar fuentes de datos

*Menú: Fuentes → Editar*

Una *fuente de datos* (fuente) vincula un esquema de clasificación con un motor de cálculo. El motor integrado actualmente es `ParamLineal` (cálculo lineal por parámetros).

### Paso 5 — Definir tipos de datos de entrada y fórmulas

*Menú: Datos → Editar / Fórmulas → Editar*

- **Tipos de dato de entrada** (dato): declarar qué se va a medir, p. ej., `consumo_combustible` en GJ/año, `conteo_vehiculos` en vehículos/día.
- **Fórmulas** (mapdatocontaminante): mapear datos de entrada a contaminantes usando expresiones JavaScript, p. ej.:

  ```javascript
  ds("consumo_combustible") * factor_emision
  ```

  `ds("nombre")` recupera el valor de un dato de entrada por nombre. Los parámetros como `factor_emision` se resuelven desde la tabla de parámetros del escenario.

### Paso 6 — Configurar zonas geográficas

*Menú: Zonas → Editar*

Definir la jerarquía administrativa (p. ej., municipio → provincia → comunidad autónoma) y configurar los niveles de zona (`nivelzona`).

### Paso 7 — Añadir puntos de medición

*Menú: Puntos de Medición → Editar*

Cada aforo representa una instalación, tramo de carretera o área donde se recogen datos. Se asigna cada aforo a una fuente de datos y a una clasificación.

### Paso 8 — Introducir valores de datos

*Menú: Valores de Datos → Editar*

Registrar los valores medidos o estimados para cada punto de medición (p. ej., consumo anual de combustible de cada instalación industrial).

### Paso 9 — Configurar la distribución espacial

*Menú: Mapa Aforo–Zona → Editar*

Para cada punto de medición, especificar qué porcentaje de sus emisiones corresponde a cada zona. Una carretera que atraviesa dos municipios podría repartirse 40 % / 60 %.

### Paso 10 — Ejecutar el cálculo

*Menú: Calcular → Ejecutar Escenario*

El motor:
1. Carga todos los valores de datos y parámetros de cada punto de medición.
2. Evalúa la fórmula JavaScript para cada contaminante.
3. Escribe los resultados en `contaminanteaforo`.
4. Agrega entre zonas usando la matriz de distribución y escribe en `contaminantezona`.

Un diálogo de progreso muestra el estado del cálculo.

### Paso 11 — Consultar y exportar resultados

*Menú: Resultados → Ver / Informes → Generar*

Consultar resultados por zona, contaminante, clasificación o fuente. Generar tablas y gráficas para incluir en informes.

---

## Generación de informes

Los informes se configuran mediante archivos `.dat` ubicados en subdirectorios de `src/calenton/reports/`. Cada fichero define una tabla o gráfica.

### Activar una plantilla de informe

*Menú: Informe → Plantillas → Seleccionar → Activar*

(Actualmente se requiere reiniciar el programa para que el cambio surta efecto.)

### Formato del fichero de configuración

Los ficheros de informe siguen un formato estilo INI:

```ini
# Título del informe (uso interno; el pie de figura se define en el fichero LaTeX)
titulo = 'Emisiones de CH4 por sector SNAP'

# Etiquetas de ejes y leyenda (usados en gráficas de barras / barras acumuladas)
nombreX = Sectores
nombreY = Toneladas
encabezado = ,

descripcion = 'Emisiones anuales de CH4 agrupadas por código SNAP de 2 dígitos'

# Tipo de gráfica:
#   pychart: tarta1, barras1, barrasAc1
#   pycha:   tarta2, barras2, barrasAc2
tipo = tarta1

# Consultas SQL que proporcionan los datos
fila = sql1,

[sql]
sql1 = '''
    SELECT c2.codigo, SUM(valor)
    FROM contaminantezona cz
    JOIN clasificacion c  ON cz.idclasificacion = c.id
    JOIN contaminante co  ON cz.idcontaminante  = co.id
    JOIN clasificacion c2 ON substr(c.codigo, 1, 2) = c2.codigo
    WHERE cz.idfuente IN (
        SELECT id FROM fuente WHERE idescenario = _ESCENARIO_
    )
    AND co.nombre = 'CH4'
    GROUP BY c2.codigo
    ORDER BY c2.codigo
'''

[columnas]
```

`_ESCENARIO_` se sustituye en tiempo de ejecución por el ID del escenario activo.

### Ficheros de salida

- **`.eps`** — gráficas vectoriales (una por fichero de configuración de gráfica, con nombre `g_*.eps`)
- **`.tex`** — fragmentos de tabla LaTeX (uno por fichero de configuración de tabla)

Incluirlos en el documento LaTeX:

```latex
\begin{figure}
  \includegraphics{reports/miinforme/g_ch4_snap.eps}
  \caption{Emisiones de CH4 por sector SNAP}
\end{figure}

\input{reports/miinforme/t_resumen_emisiones.tex}
```

---

## Importación de datos mediante CSV

Para importar datos en bloque a cualquier tabla de la base de datos desde un fichero CSV:

```bash
./inserta_en_tabla.sh nombre_tabla fichero_datos.csv
```

### Requisitos del formato CSV

- Separador de campos: **punto y coma** (`;`)
- **Sin fila de cabecera**
- **Sin comillas** alrededor de los campos de texto
- Codificación: UTF-8

El script usa internamente el comando `COPY` de PostgreSQL.

**Paquete necesario:** `postgresql-client`

---

## Estructura del proyecto

```
calenton/
├── run.sh                        # Lanzador de la aplicación (configura variables de entorno e inicia Python)
├── sql/
│   ├── calenton.sql              # Esquema completo de la BD (tablas, secuencias, restricciones)
│   ├── codigo.sql                # Funciones PL/pgSQL y disparadores
│   └── datos.sql                 # Datos iniciales (jerarquía SNAP, motores de cálculo)
├── doc/
│   ├── instalacion.txt           # Instrucciones de instalación originales
│   ├── crear_informe.txt         # Guía de usuario del sistema de informes
│   ├── graficas_informe.txt      # Referencia de configuración de gráficas
│   └── inserta_en_tablas.sh.txt  # Guía de importación CSV
└── src/
    ├── componentes/              # Librería de widgets C++ (compilada con SIP)
    │   ├── pyproject.toml        # Configuración de compilación
    │   ├── sip/                  # Ficheros de definición de interfaz SIP
    │   └── lib/                  # Salida compilada: libcomponentes.so
    └── calenton/                 # Aplicación Python principal
        ├── calenton.py           # Punto de entrada
        ├── calculo/              # Motor de cálculo
        │   ├── calcula.py        # Orquestador CalculaEscenario
        │   └── aforo.py          # Cargador de datos por punto de medición con caché
        ├── modelo/               # Modelos de tablas de BD (envoltorios tipo ORM)
        │   ├── escenario.py      # Escenario, Origen
        │   ├── zona.py           # Modelos de jerarquía de zonas
        │   ├── clasificacion.py  # Modelos de árbol de clasificación
        │   ├── contaminante.py   # Modelos de contaminantes
        │   ├── aforo.py          # Modelos de puntos de medición
        │   └── ...               # Un fichero por grupo de entidades
        ├── forms/                # Diálogos Qt6 y ventana principal
        │   ├── main.py           # Ventana MDI principal
        │   └── ...               # Un diálogo por entidad
        ├── widgets/              # Componentes de widget Qt6 reutilizables
        ├── js/
        │   └── motor.py          # Motor de fórmulas JavaScript (envoltorio de QJSEngine)
        ├── informe/              # Subsistema de generación de informes
        │   ├── tablas.py         # Generador de tablas LaTeX
        │   └── graficas.py       # Generador de gráficas EPS
        ├── config/
        │   └── unidades.xml      # Definiciones del sistema de unidades (dimensiones, ratios, precisión)
        └── reports/              # Directorios de plantillas de informes (creados por el usuario)
```

---

## Conceptos clave

### Escenario

El contenedor de nivel superior para un inventario. Todos los parámetros, fuentes de datos y resultados pertenecen a exactamente un escenario, lo que permite comparaciones metodológicas en paralelo.

### Clasificación

Un esquema de codificación jerárquico para las fuentes de emisión. Se admiten las jerarquías SNAP e IPCC. La función de base de datos `jerarquia_clasificacion()` recorre las cadenas padre-hijo para las consultas de agregación.

### Motor de fórmulas

Las fórmulas son expresiones JavaScript evaluadas por `QJSEngine` de Qt. La función especial `ds("nombre")` recupera el valor de un dato de entrada por nombre. Las variables con nombre (parámetros) se inyectan en el contexto JS antes de la evaluación.

### Jerarquía de sobreescritura de parámetros

Cuando el motor busca el valor de un parámetro para un punto de medición, comprueba en orden:
1. **Sobreescritura por punto de medición** (`parametroaforo`) — más específico
2. **Sobreescritura por zona** (`parametrozona`) — para diferencias regionales
3. **Valor por defecto del escenario** (`parametro`) — valor de respaldo

### Matriz de distribución espacial

`mapaforozona` almacena pesos porcentuales que mapean cada punto de medición a una o más zonas. Esto permite gestionar fuentes distribuidas (p. ej., una carretera) que abarcan varios límites administrativos.

### Sistema de unidades

`config/unidades.xml` define un sistema completo de conversión de unidades que cubre caudal, masa, energía, presión, potencia, temperatura y más. El módulo `ts` lee este fichero para ofrecer campos de entrada con conversión de unidades en la interfaz gráfica.

---

## Licencia

Copyright © 2009–2010 LITEC (CSIC) y Trustserver SL.

Este programa es software libre; puedes redistribuirlo y/o modificarlo bajo los términos de la **GNU General Public License versión 2** (o cualquier versión posterior) publicada por la Free Software Foundation. Consulta [LICENSE](LICENSE) para el texto completo.
