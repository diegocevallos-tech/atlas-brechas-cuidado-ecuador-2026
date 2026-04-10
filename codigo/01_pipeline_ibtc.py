"""
01_pipeline_ibtc.py
====================
Pipeline completo: lectura de datos → limpieza → cálculo IBTC → exportación.

INPUT requerido (colocar en las rutas definidas en config.py):
  - censo_2022_cantonal.csv
  - cdi_cnh_mies_q4_2024.csv
  - cnrh_tnr_2023_provincial.csv
  - cantones_ecuador.shp (+ archivos .dbf, .shx, .prj)

OUTPUT:
  - 00_datos/01_processed/d1_demanda.csv
  - 00_datos/01_processed/d2_oferta.csv
  - 00_datos/01_processed/d3_tnr.csv
  - 00_datos/02_final/ibtc_cantones_final.csv
  - 00_datos/02_final/ibtc_ecuador.gpkg

EJECUTAR: python 01_pipeline_ibtc.py
"""

# ── Importaciones ─────────────────────────────────────────────────────────
import sys
import pandas as pd
import geopandas as gpd
from pathlib import Path

# Agrega la carpeta del proyecto al path para importar config
sys.path.insert(0, str(Path(__file__).parent))
from config import (
    RUTA_RAW_CENSO, RUTA_RAW_CDI, RUTA_RAW_TNR, RUTA_RAW_SHP,
    RUTA_PROCESSED, RUTA_FINAL,
    ARCHIVO_CENSO_CSV, ARCHIVO_CDI_CSV, ARCHIVO_TNR_CSV, ARCHIVO_SHP_CANTON,
    CAMPO_CODIGO_CANTON,
    PESO_D1, PESO_D2, PESO_D3,
    METODO_CLASIFICACION, TIPOLOGIA_ETIQUETAS,
    CRS_PROYECTO, NOMBRE_DATASET_FINAL, NOMBRE_GEOPACKAGE, NOMBRE_CAPA_GPKG,
)

# ── Utilidades ────────────────────────────────────────────────────────────

def normalizar_minmax(serie: pd.Series) -> pd.Series:
    """Normaliza al rango [0,1]. Si rango es cero, devuelve 0."""
    rango = serie.max() - serie.min()
    if rango == 0:
        return pd.Series([0.0] * len(serie), index=serie.index)
    return (serie - serie.min()) / rango


def clasificar_tipologia(serie_ibtc: pd.Series, metodo: str) -> pd.Series:
    """Asigna categoría 1-4 según el método de clasificación configurado."""
    if metodo == "cuartiles":
        return pd.qcut(serie_ibtc, q=4, labels=[1, 2, 3, 4]).astype(int)
    elif metodo == "igual_intervalo":
        return pd.cut(serie_ibtc, bins=4, labels=[1, 2, 3, 4]).astype(int)
    else:
        raise ValueError(f"Método de clasificación no reconocido: {metodo}")


def validar_archivo(ruta: Path):
    """Lanza error claro si el archivo no existe."""
    if not ruta.exists():
        raise FileNotFoundError(
            f"\n[ERROR] Archivo no encontrado: {ruta}"
            f"\nVerificar nombre y ubicación en config.py"
        )

# ── PASO 1: Leer y validar fuentes ────────────────────────────────────────

print("\n=== PIPELINE IBTC — Atlas Brechas de Cuidado ===")
print("\n[1/6] Leyendo fuentes de datos...")

archivo_censo = RUTA_RAW_CENSO / ARCHIVO_CENSO_CSV
archivo_cdi   = RUTA_RAW_CDI   / ARCHIVO_CDI_CSV
archivo_tnr   = RUTA_RAW_TNR   / ARCHIVO_TNR_CSV
archivo_shp   = RUTA_RAW_SHP   / ARCHIVO_SHP_CANTON

for f in [archivo_censo, archivo_cdi, archivo_tnr, archivo_shp]:
    validar_archivo(f)

censo = pd.read_csv(archivo_censo, dtype={CAMPO_CODIGO_CANTON: str})
cdi   = pd.read_csv(archivo_cdi,   dtype={CAMPO_CODIGO_CANTON: str})
tnr   = pd.read_csv(archivo_tnr)
gdf   = gpd.read_file(archivo_shp).to_crs(CRS_PROYECTO)

print(f"  ✓ Censo: {len(censo)} filas | CDI: {len(cdi)} filas | TNR: {len(tnr)} filas | SHP: {len(gdf)} cantones")

# ── PASO 2: Calcular D1 — Demanda Potencial ───────────────────────────────

print("\n[2/6] Calculando D1 (Demanda Potencial)...")
# NOTA para DC: ajustar los nombres de columna según el CSV real del Censo.
# Las columnas esperadas son aproximaciones — verificar con value_counts() primero.
# Variables requeridas (nombres a confirmar):
#   pct_menores_5   : % población < 5 años sobre total cantón
#   pct_mayores_65  : % población > 65 años sobre total cantón
#   pct_discapacidad: % hogares con al menos 1 miembro con discapacidad
#   pct_jef_fem_sola: % hogares con jefatura femenina sin pareja

COLUMNAS_D1 = ["pct_menores_5", "pct_mayores_65", "pct_discapacidad", "pct_jef_fem_sola"]
for col in COLUMNAS_D1:
    if col not in censo.columns:
        raise KeyError(f"[ERROR D1] Columna '{col}' no encontrada en censo. Verificar nombres reales.")

d1 = censo[[CAMPO_CODIGO_CANTON] + COLUMNAS_D1].copy()
for col in COLUMNAS_D1:
    d1[col + "_norm"] = normalizar_minmax(d1[col])
d1["D1"] = d1[[c + "_norm" for c in COLUMNAS_D1]].mean(axis=1)
d1[["D1_norm"]] = d1[["D1"]].apply(normalizar_minmax)

d1.to_csv(RUTA_PROCESSED / "d1_demanda.csv", index=False)
print(f"  ✓ D1 calculado. Rango: {d1['D1'].min():.3f} – {d1['D1'].max():.3f}")

# ── PASO 3: Calcular D2 — Oferta Institucional ────────────────────────────

print("\n[3/6] Calculando D2 (Oferta Institucional)...")
# NOTA para DC: ajustar nombres de columna según el CSV real del MIES.
# Variables esperadas:
#   usuarios_cdi_cnh : número de usuarios atendidos en CDI/CNH por cantón
#   pob_0_3_censo    : población 0-3 años según Censo 2022 (puede venir del censo)

if "usuarios_cdi_cnh" not in cdi.columns or "pob_0_3_censo" not in cdi.columns:
    raise KeyError("[ERROR D2] Verificar nombres de columnas en cdi_cnh_mies. Ajustar en este script.")

d2 = cdi[[CAMPO_CODIGO_CANTON, "usuarios_cdi_cnh", "pob_0_3_censo"]].copy()
d2["cobertura_cdi"] = (d2["usuarios_cdi_cnh"] / d2["pob_0_3_censo"]).clip(0, 1)
d2["cobertura_norm"] = normalizar_minmax(d2["cobertura_cdi"])
d2["D2_norm"] = 1 - d2["cobertura_norm"]  # Invertir: menor cobertura = mayor brecha

d2.to_csv(RUTA_PROCESSED / "d2_oferta.csv", index=False)
print(f"  ✓ D2 calculado (invertido). Cobertura media: {d2['cobertura_cdi'].mean():.3f}")

# ── PASO 4: Calcular D3 — Carga TNR ───────────────────────────────────────

print("\n[4/6] Calculando D3 (Carga TNR femenino)...")
# NOTA: CNRH 2023 tiene escala PROVINCIAL. Se asigna valor provincial a cada cantón.
# Variables esperadas en cnrh_tnr_2023_provincial.csv:
#   cod_provincia   : código de provincia (2 dígitos)
#   brecha_tnr_horas: diferencia horas TNR mujer - hombre

if "cod_provincia" not in tnr.columns or "brecha_tnr_horas" not in tnr.columns:
    raise KeyError("[ERROR D3] Verificar nombres de columnas en cnrh_tnr. Ajustar en este script.")

tnr["D3_norm"] = normalizar_minmax(tnr["brecha_tnr_horas"])
tnr.to_csv(RUTA_PROCESSED / "d3_tnr.csv", index=False)
print(f"  ✓ D3 calculado. Brecha promedio: {tnr['brecha_tnr_horas'].mean():.1f} horas")

# ── PASO 5: Calcular IBTC y tipología ─────────────────────────────────────

print("\n[5/6] Calculando IBTC y tipología territorial...")

# Unir D1 y D2 por código cantón
ibtc = d1[[CAMPO_CODIGO_CANTON, "D1_norm"]].merge(
    d2[[CAMPO_CODIGO_CANTON, "D2_norm"]],
    on=CAMPO_CODIGO_CANTON, how="left"
)

# Derivar código provincia del cantón (primeros 2 dígitos) y unir D3
ibtc["cod_provincia"] = ibtc[CAMPO_CODIGO_CANTON].str[:2]
ibtc = ibtc.merge(
    tnr[["cod_provincia", "D3_norm"]],
    on="cod_provincia", how="left"
)

# Calcular IBTC ponderado
ibtc["IBTC"] = (
    PESO_D1 * ibtc["D1_norm"] +
    PESO_D2 * ibtc["D2_norm"] +
    PESO_D3 * ibtc["D3_norm"]
)

# Clasificar tipología
ibtc["tipologia_num"] = clasificar_tipologia(ibtc["IBTC"], METODO_CLASIFICACION)
ibtc["tipologia"]     = ibtc["tipologia_num"].map(TIPOLOGIA_ETIQUETAS)

ibtc.to_csv(RUTA_FINAL / NOMBRE_DATASET_FINAL, index=False)
print(f"  ✓ IBTC calculado para {len(ibtc)} cantones.")
print(f"  Distribución tipología:\n{ibtc['tipologia'].value_counts().to_string()}")

# ── PASO 6: Unir con shapefile y exportar GeoPackage ──────────────────────

print("\n[6/6] Uniendo con shapefile y exportando GeoPackage...")

if CAMPO_CODIGO_CANTON not in gdf.columns:
    raise KeyError(f"[ERROR SHP] Campo '{CAMPO_CODIGO_CANTON}' no encontrado en shapefile. Ajustar en config.py.")

gdf[CAMPO_CODIGO_CANTON] = gdf[CAMPO_CODIGO_CANTON].astype(str)
ibtc[CAMPO_CODIGO_CANTON]  = ibtc[CAMPO_CODIGO_CANTON].astype(str)

gdf_ibtc = gdf.merge(ibtc, on=CAMPO_CODIGO_CANTON, how="left")

sin_datos = gdf_ibtc["IBTC"].isna().sum()
if sin_datos > 0:
    print(f"  ⚠ ADVERTENCIA: {sin_datos} cantones sin datos IBTC. Verificar claves de unión.")

gdf_ibtc.to_file(RUTA_FINAL / NOMBRE_GEOPACKAGE, layer=NOMBRE_CAPA_GPKG, driver="GPKG")
print(f"  ✓ GeoPackage exportado: {NOMBRE_GEOPACKAGE}")
print(f"\n=== PIPELINE COMPLETADO ===")
print(f"Dataset final: {RUTA_FINAL / NOMBRE_DATASET_FINAL}")
print(f"GeoPackage   : {RUTA_FINAL / NOMBRE_GEOPACKAGE}")
