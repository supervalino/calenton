# Calenton — Emissions Inventory Tool

**Calenton** is a desktop application for calculating, managing, and reporting air pollutant emissions from multiple source types. It was developed by LITEC (Laboratorio de Investigación en Tecnologías de la Combustión — CSIC) and Trustserver SL (2009–2010). The name comes from the Spanish word for a large heater, reflecting its focus on combustion-related emissions research.

The tool is designed for environmental analysts who need to:

- Manage multiple inventory **scenarios** (different regulatory years or methodologies)
- Ingest measurement data from industrial facilities, transport networks, agricultural sources, etc.
- Compute pollutant emissions using flexible, user-defined JavaScript formulas
- Aggregate results to administrative geographic zones (municipality, province, region)
- Generate publication-quality tables and charts for LaTeX-based reports

---

## Table of Contents

1. [How It Works](#how-it-works)
2. [Requirements & Dependencies](#requirements--dependencies)
3. [Installation](#installation)
4. [Database Setup](#database-setup)
5. [Running the Application](#running-the-application)
6. [Usage Walkthrough](#usage-walkthrough)
7. [Report Generation](#report-generation)
8. [Data Import via CSV](#data-import-via-csv)
9. [Project Structure](#project-structure)
10. [Key Concepts](#key-concepts)

---

## How It Works

Calenton follows a **scenario-based, formula-driven** calculation pipeline:

```
Scenario
  └── Data Sources (fuentes)
        └── Measurement Points / Facilities (aforós)
              ├── Input Data (valordato)     ← fuel consumption, vehicle count, etc.
              ├── Parameters (parametro)     ← emission factors with zone overrides
              └── Formulas (formula)         ← JavaScript expressions that produce:
                    └── Emissions (contaminanteaforo)   ← per pollutant, per point
                          └── Aggregated by zone (contaminantezona)  ← final output
```

**Core pipeline steps:**

1. A *scenario* groups all the configuration for one inventory (e.g., "Spain 2020 SNAP").
2. *Data sources* link measurement points to a calculation engine and a classification scheme (SNAP, IPCC, …).
3. For each *measurement point* (aforo), the user records *data values* (e.g., annual fuel consumption in GJ).
4. *Formulas* expressed as JavaScript map those data values — plus scenario *parameters* (emission factors, conversion constants) — to pollutant quantities.
5. Parameters support a three-level override hierarchy: scenario-wide → zone-specific → measurement-point-specific.
6. A *spatial distribution matrix* (`mapaforozona`) distributes each measurement point's emissions across one or more administrative zones by percentage (useful for roads that cross multiple municipalities).
7. The calculation engine writes results to `contaminanteaforo` (per point) and `contaminantezona` (aggregated by zone, source, and classification).
8. The report subsystem reads those tables and generates `.eps` graphics and `.tex` tables ready for inclusion in LaTeX documents.

---

## Requirements & Dependencies

### Supported distributions

Calenton requires **QGIS 4.x built against Qt6** (`python3-qgis` Qt6). As of May 2026, the systems where this is available are:

| System | Status |
|---|---|
| **Ubuntu 24.04 LTS** (noble) | Works — official QGIS repo |
| **Debian 13** (trixie) | Works — official QGIS repo |
| Debian sid/forky | Blocked — GDAL dependency conflict |
| Ubuntu 22.04 / Debian 12 | Blocked — only Qt5 QGIS available |

### System packages (Ubuntu 24.04 / Debian trixie)

```bash
# Add the official QGIS repo (required to get QGIS 4.x Qt6)
sudo mkdir -p /etc/apt/keyrings
sudo wget -O /etc/apt/keyrings/qgis-archive-keyring.gpg \
    https://download.qgis.org/downloads/qgis-archive-keyring.gpg

# Create /etc/apt/sources.list.d/qgis.sources with your distro codename:
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

# PostgreSQL with PostGIS spatial extension
sudo apt install postgresql postgis

# QGIS 4.x with Qt6
sudo apt install qgis python3-qgis

# Python dependencies
sudo apt install python3-pyqt6 python3-cairo

# Graphics libraries for report generation
pip install pycha pychart configobj
```

### Mandatory local compilation

**No pre-built binaries are distributed.** The source code must be compiled on the target machine before the application can run. If the build fails, paste the error message into an AI assistant — that is usually enough to resolve dependency or path issues. There are two components to build:

**1. C++ widget library and `ts` Python module (`src/componentes/`)**

A single build produces two artefacts that are both required:

- `src/componentes/lib/libcomponentes.so` — the C++ shared library loaded at runtime
- `src/componentes/sip/generated/ts.so` — the Python extension module (`import ts`) that exposes the widgets and table models to the application

```bash
cd src/componentes
pip install sip build
python -m build
```

`run.sh` adds `src/componentes/lib/` to `LD_LIBRARY_PATH` automatically. You must also ensure `src/componentes/sip/generated/` (or wherever `ts.so` lands after the build) is on `PYTHONPATH` so Python can import it.

> **Note:** The compiled `.so` files are not included in the repository — they are architecture-specific binaries. Every machine must build from source.

### Python packages summary

| Package | Purpose |
|---|---|
| `PyQt6` | GUI framework |
| `qgis` (Python API) | Map rendering |
| `pycha` / `pychart` | Chart generation in reports |
| `cairo` | EPS graphics rendering |
| `configobj` | Report `.dat` configuration parsing |
| `sip >= 6, < 7` | C++ binding for `componentes` |

---

## Installation

### 1. Clone / obtain the source

```bash
git clone <repository-url> calenton
cd calenton
```

### 2. Build the C++ widget library

```bash
cd src/componentes
python -m build
cd ../..
```

Verify that `src/componentes/lib/libcomponentes.so` exists after the build.

### 3. Install the `ts` module

Place or install the `ts` Python package so it is importable. If you have a `ts/` directory in the project:

```bash
export PYTHONPATH="$PWD/src:$PYTHONPATH"
```

Or install it with pip if a `setup.py` / `pyproject.toml` is provided.

### 4. Set up QGIS

The launcher script (`run.sh`) expects a QGIS Qt6 installation at `$HOME/qgis-qt6`. If QGIS is installed system-wide, adjust the `QGIS_PREFIX` variable in `run.sh`:

```bash
# In run.sh, change:
QGIS_PREFIX="$HOME/qgis-qt6"
# to wherever QGIS is installed, e.g.:
QGIS_PREFIX="/usr"
```

---

## Database Setup

Calenton uses **PostgreSQL with PostGIS**. The following steps create the `emisiones` database from scratch.

### 1. Create a PostgreSQL user (if needed)

```bash
sudo -u postgres createuser --superuser $USER
```

### 2. Create the database

```bash
dropdb --if-exists emisiones
createdb -E UTF-8 emisiones
```

### 3. Enable PostGIS and PL/pgSQL

```bash
psql emisiones -c "CREATE EXTENSION IF NOT EXISTS postgis;"
psql emisiones -c "CREATE EXTENSION IF NOT EXISTS plpgsql;"
```

### 4. Load the schema

```bash
psql emisiones < sql/calenton.sql   # Tables, sequences, constraints
psql emisiones < sql/codigo.sql     # PL/pgSQL functions and triggers
psql emisiones < sql/datos.sql      # Seed data (SNAP classification, calculation engines)
```

### 5. Create a working schema for temporary data

```bash
psql emisiones -c "CREATE SCHEMA IF NOT EXISTS temp AUTHORIZATION $USER;"
```

### 6. (Optional) Set a database password

```bash
psql emisiones -c "ALTER USER $USER WITH PASSWORD 'yourpassword';"
```

### Restoring from a backup

If you have a `pg_dump` backup:

```bash
# Custom-format backup:
pg_restore -F c -d emisiones backup.dmp

# Plain SQL backup:
psql emisiones -f backup.sql
```

---

## Running the Application

```bash
./run.sh
```

The launcher script:
1. Determines the project root directory.
2. Sets `LD_LIBRARY_PATH` to include `src/componentes/lib/` and the QGIS libraries.
3. Sets `PYTHONPATH` to include the QGIS Python API.
4. Configures `QT_PLUGIN_PATH` and `GDAL_DATA` for QGIS.
5. Executes `python3 src/calenton/calenton.py`.

If the script is not executable, run:

```bash
chmod +x run.sh
./run.sh
```

---

## Usage Walkthrough

The application opens as an MDI (Multiple Document Interface) window. The typical workflow for a new inventory is:

### Step 1 — Create a Scenario

*Menu: Scenario → New*

A scenario groups all configuration for one inventory instance (e.g., "Aragón 2022 SNAP"). Each scenario is independent; parameters and results do not cross scenario boundaries.

### Step 2 — Define Classification Hierarchies

*Menu: Classification → Edit*

Load or define a classification scheme such as SNAP (Selected Nomenclature for Air Pollutants) or IPCC. The tree is hierarchical: SNAP sector → sub-sector → activity. Pre-loaded SNAP data is included in `sql/datos.sql`.

### Step 3 — Add Pollutants

*Menu: Pollutants → Edit*

Define which pollutants to track (CO₂, CH₄, NOₓ, PM₁₀, NMVOC, …) and optionally configure CO₂-equivalence factors for global warming potential calculations.

### Step 4 — Configure Data Sources

*Menu: Sources → Edit*

A *data source* (fuente) links a classification scheme to a calculation engine. Currently the built-in engine is `ParamLineal` (linear parameter calculation).

### Step 5 — Define Input Data Types and Formulas

*Menu: Data → Edit / Formulas → Edit*

- **Input data types** (dato): declare what you will measure, e.g., `fuel_consumption` in GJ/year, `vehicle_count` in vehicles/day.
- **Formulas** (mapdatocontaminante): map data inputs to pollutant outputs using JavaScript expressions, e.g.:

  ```javascript
  ds("fuel_consumption") * emission_factor
  ```

  `ds("name")` retrieves the value of a named data input. Parameters like `emission_factor` are resolved from the scenario's parameter table.

### Step 6 — Set Up Geographic Zones

*Menu: Zones → Edit*

Define your administrative hierarchy (e.g., municipality → province → autonomous community) and configure the zone levels (`nivelzona`).

### Step 7 — Add Measurement Points

*Menu: Measurement Points → Edit*

Each aforo represents a facility, road segment, or area where data is collected. Assign each aforo to a data source and a classification.

### Step 8 — Enter Data Values

*Menu: Data Values → Edit*

Record the measured or estimated values for each measurement point (e.g., annual fuel consumption for each industrial facility).

### Step 9 — Configure Spatial Distribution

*Menu: Aforo–Zone Map → Edit*

For each measurement point, specify what percentage of its emissions fall within each zone. A highway crossing two municipalities might be split 40% / 60%.

### Step 10 — Run the Calculation

*Menu: Calculate → Run Scenario*

The engine:
1. Loads all data values and parameters for each measurement point.
2. Evaluates the JavaScript formula for each pollutant.
3. Writes results to `contaminanteaforo`.
4. Aggregates across zones using the distribution matrix and writes to `contaminantezona`.

A progress dialog shows calculation status.

### Step 11 — View and Export Results

*Menu: Results → View / Reports → Generate*

Query results by zone, pollutant, classification, or source. Generate tables and charts for inclusion in reports.

---

## Report Generation

Reports are driven by `.dat` configuration files located in subdirectories of `src/calenton/reports/`. Each file defines one table or chart.

### Activating a report template

*Menu: Report → Templates → Select → Activate*

(A restart is currently required for the change to take effect.)

### Configuration file format

Report files follow an INI-style format:

```ini
# Report title (used internally; set the caption in your LaTeX file)
titulo = 'CH4 emissions by SNAP sector'

# Axis labels and legend (used for bar/stacked-bar charts)
nombreX = Sectors
nombreY = Tonnes
encabezado = ,

descripcion = 'Annual CH4 emissions grouped by 2-digit SNAP code'

# Chart type:
#   pychart: tarta1, barras1, barrasAc1
#   pycha:   tarta2, barras2, barrasAc2
tipo = tarta1

# Which SQL queries provide the data rows
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

`_ESCENARIO_` is replaced at runtime with the active scenario ID.

### Output files

- **`.eps`** — vector graphics (one per chart config file, named `g_*.eps`)
- **`.tex`** — LaTeX table fragments (one per table config file)

Include them in your LaTeX document:

```latex
\begin{figure}
  \includegraphics{reports/myreport/g_ch4_snap.eps}
  \caption{CH4 emissions by SNAP sector}
\end{figure}

\input{reports/myreport/t_emissions_summary.tex}
```

---

## Data Import via CSV

To bulk-import data into any database table from a CSV file:

```bash
./inserta_en_tabla.sh table_name data_file.csv
```

### CSV format requirements

- Field separator: **semicolon** (`;`)
- **No header row**
- **No quotes** around text fields
- Encoding: UTF-8

The script uses the PostgreSQL `COPY` command internally.

**Required package:** `postgresql-client`

---

## Project Structure

```
calenton/
├── run.sh                        # Application launcher (sets env vars, starts Python)
├── sql/
│   ├── calenton.sql              # Full database schema (tables, sequences, constraints)
│   ├── codigo.sql                # PL/pgSQL functions and triggers
│   └── datos.sql                 # Seed data (SNAP hierarchy, calculation engines)
├── doc/
│   ├── instalacion.txt           # Original installation instructions
│   ├── crear_informe.txt         # Report system user guide
│   ├── graficas_informe.txt      # Chart configuration reference
│   └── inserta_en_tablas.sh.txt  # CSV import guide
└── src/
    ├── componentes/              # C++ custom widget library (compiled with SIP)
    │   ├── pyproject.toml        # Build configuration
    │   ├── sip/                  # SIP interface definition files
    │   └── lib/                  # Compiled output: libcomponentes.so
    └── calenton/                 # Main Python application
        ├── calenton.py           # Entry point
        ├── calculo/              # Calculation engine
        │   ├── calcula.py        # CalculaEscenario orchestrator
        │   └── aforo.py          # Per-measurement-point data loader with caching
        ├── modelo/               # Database table models (ORM-like wrappers)
        │   ├── escenario.py      # Scenario, Origin
        │   ├── zona.py           # Zone hierarchy models
        │   ├── clasificacion.py  # Classification tree models
        │   ├── contaminante.py   # Pollutant models
        │   ├── aforo.py          # Measurement point models
        │   └── ...               # One file per entity group
        ├── forms/                # Qt6 GUI dialogs and main window
        │   ├── main.py           # MDI main window
        │   └── ...               # One dialog per entity
        ├── widgets/              # Reusable Qt6 widget components
        ├── js/
        │   └── motor.py          # JavaScript formula engine (QJSEngine wrapper)
        ├── informe/              # Report generation subsystem
        │   ├── tablas.py         # LaTeX table builder
        │   └── graficas.py       # EPS chart builder
        ├── config/
        │   └── unidades.xml      # Unit system definitions (dimensions, ratios, precision)
        └── reports/              # Report template directories (user-created)
```

---

## Key Concepts

### Scenario (Escenario)

The top-level container for an inventory. All parameters, data sources, and results belong to exactly one scenario, enabling side-by-side methodology comparisons.

### Classification (Clasificacion)

A hierarchical coding scheme for emission sources. SNAP and IPCC hierarchies are supported. The `jerarquia_clasificacion()` database function traverses parent-child chains for aggregation queries.

### Formula Engine

Formulas are JavaScript expressions evaluated by Qt's `QJSEngine`. The special function `ds("name")` retrieves a named input data value. Named variables (parameters) are injected into the JS context before evaluation.

### Parameter Override Hierarchy

When the engine looks up a parameter value for a measurement point, it checks in order:
1. **Measurement-point override** (`parametroaforo`) — most specific
2. **Zone override** (`parametrozona`) — for regional differences
3. **Scenario default** (`parametro`) — fallback

### Spatial Distribution Matrix

`mapaforozona` stores percentage weights mapping each measurement point to one or more zones. This handles distributed sources (e.g., a highway) that span multiple administrative boundaries.

### Unit System

`config/unidades.xml` defines a complete unit conversion system covering flow, mass, energy, pressure, power, temperature, and more. The `ts` module reads this file to offer unit-aware input fields in the GUI.

---

## License

Copyright © 2009–2010 LITEC (CSIC) and Trustserver SL.

This program is free software; you can redistribute it and/or modify it under the terms of the **GNU General Public License version 2** (or any later version) as published by the Free Software Foundation. See [LICENSE](LICENSE) for the full text.
