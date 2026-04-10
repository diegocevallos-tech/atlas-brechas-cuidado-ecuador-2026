"""
config.py — Parámetros centrales del proyecto
===============================================
EDITAR ESTE ARCHIVO para adaptar el proyecto a un nuevo contexto o entorno.
NO hardcodear rutas ni parámetros en los scripts de procesamiento.
"""

from pathlib import Path

# ------------------------------------------------------------------------------
# RUTAS BASE — ajustar si el proyecto se mueve a otra máquina
# ------------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent  # raíz del proyecto

RUTA_RAW_CENSO          = ROOT / "00_datos" / "00_raw" / "censo_2022"
RUTA_RAW_CDI            = ROOT / "00_datos" / "00_raw" / "cdi_cnh_mies"
RUTA_RAW_TNR            = ROOT / "00_datos" / "00_raw" / "cnrh_tnr_2023"
RUTA_RAW_SHP            = ROOT / "00_datos" / "00_raw" / "shapefiles_cantonales"
RUTA_PROCESSED          = ROOT / "00_datos" / "01_processed"
RUTA_FINAL              = ROOT / "00_datos" / "02_final"
RUTA_MAPAS_ESTATICOS    = ROOT / "02_mapas" / "estaticos"
RUTA_MAPAS_INTERACTIVOS = ROOT / "02_mapas" / "interactivos"
RUTA_DASHBOARD          = ROOT / "03_dashboard"
RUTA_INFORME            = ROOT / "05_informe"
RUTA_ENTREGA            = ROOT / "06_entrega_final"

# ------------------------------------------------------------------------------
# PARÁMETROS DE DATOS — editar si cambian los nombres de archivos fuente
# ------------------------------------------------------------------------------
ARCHIVO_CENSO_CSV     = "censo_2022_cantonal.csv"   # nombre del archivo que descargue DC
ARCHIVO_CDI_CSV       = "cdi_cnh_mies_q4_2024.csv"  # datos abiertos MIES
ARCHIVO_TNR_CSV       = "cnrh_tnr_2023_provincial.csv"
ARCHIVO_SHP_CANTON    = "cantones_ecuador.shp"       # shapefile IGM/INEC

# Campo clave de unión cantón (verificar nombre exacto en el shapefile)
CAMPO_CODIGO_CANTON   = "DPA_CANTON"  # ajustar si el campo tiene otro nombre

# ------------------------------------------------------------------------------
# PARÁMETROS DEL IBTC — ponderaciones declaradas en el formulario aprobado
# NO cambiar sin validación metodológica del equipo
# ------------------------------------------------------------------------------
PESO_D1 = 0.40   # Demanda potencial de cuidados
PESO_D2 = 0.40   # Oferta institucional (invertida: menor cobertura = mayor brecha)
PESO_D3 = 0.20   # Carga estructural de trabajo no remunerado femenino

# Método de clasificación tipológica
METODO_CLASIFICACION = "cuartiles"  # opciones: "cuartiles", "jenks", "igual_intervalo"

# Etiquetas de la tipología (en orden de mayor a menor brecha)
TIPOLOGIA_ETIQUETAS = {
    4: "Crítico",
    3: "Vulnerable",
    2: "En Transición",
    1: "Cobertura Relativa",
}

# ------------------------------------------------------------------------------
# PARÁMETROS CARTOGRÁFICOS
# ------------------------------------------------------------------------------
CRS_PROYECTO    = "EPSG:4326"   # WGS84 para mapas web
CRS_CALCULO     = "EPSG:32717"  # UTM Zona 17S para cálculos de área si aplica
DPI_ESTATICO    = 300           # resolución exportación PNG/PDF
FORMATO_ESTATICO = "png"        # "png" o "pdf"

# Paleta de colores del IBTC (de menor a mayor brecha)
PALETA_IBTC = {
    "Cobertura Relativa": "#d4e8c2",
    "En Transición":      "#f5d67a",
    "Vulnerable":         "#e8924a",
    "Crítico":            "#c0392b",
}

# ------------------------------------------------------------------------------
# PARÁMETROS DE EXPORTACIÓN
# ------------------------------------------------------------------------------
NOMBRE_DATASET_FINAL = "ibtc_cantones_final.csv"
NOMBRE_GEOPACKAGE    = "ibtc_ecuador.gpkg"
NOMBRE_MAPA_PRINCIPAL = "mapa_04_ibtc_tipologia"

# Nombre de la capa dentro del GeoPackage
NOMBRE_CAPA_GPKG = "ibtc_cantones"

# ------------------------------------------------------------------------------
# METADATA DEL PROYECTO (para títulos de mapas, README, etc.)
# ------------------------------------------------------------------------------
TITULO_PROYECTO = "Atlas Territorial de Brechas de Cuidado"
SUBTITULO       = "Modelo de priorización cantonal para políticas de igualdad de género en Ecuador"
EVENTO          = "DAT4CCIÓN 2026 — ONU Mujeres"
FUENTE_DATOS    = "INEC Censo 2022 | MIES SIIMIES Q4 2024 | CNRH 2023 | IGM Ecuador"
FECHA_DATOS     = "2022-2024"
