"""
02_generar_mapas.py
====================
Genera los 5 mapas estáticos (PNG) e interactivos (HTML) del Atlas.
REQUIERE que 01_pipeline_ibtc.py ya haya corrido exitosamente.

OUTPUT:
  - 02_mapas/estaticos/mapa_01_demanda.png
  - 02_mapas/estaticos/mapa_02_oferta.png
  - 02_mapas/estaticos/mapa_03_brecha.png
  - 02_mapas/estaticos/mapa_04_ibtc_tipologia.png  ← MAPA PRINCIPAL
  - 02_mapas/estaticos/mapa_05_tnr_contextual.png
  - 02_mapas/interactivos/mapa_04_ibtc_tipologia.html (y los demás)

EJECUTAR: python 02_generar_mapas.py
"""

# ESQUELETO — DC debe completar con lógica de matplotlib/folium
# Este archivo establece la estructura y parámetros; la lógica de graficación
# se completa en la siguiente iteración con el script completo de mapas.

import sys
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import folium
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config import (
    RUTA_FINAL, RUTA_MAPAS_ESTATICOS, RUTA_MAPAS_INTERACTIVOS,
    NOMBRE_GEOPACKAGE, NOMBRE_CAPA_GPKG,
    PALETA_IBTC, TIPOLOGIA_ETIQUETAS,
    DPI_ESTATICO, FORMATO_ESTATICO,
    TITULO_PROYECTO, FUENTE_DATOS, CRS_PROYECTO,
)

print("\n=== GENERACIÓN DE MAPAS — Atlas Brechas de Cuidado ===")

# Cargar GeoPackage
gdf = gpd.read_file(RUTA_FINAL / NOMBRE_GEOPACKAGE, layer=NOMBRE_CAPA_GPKG)
print(f"  ✓ GeoPackage cargado: {len(gdf)} cantones")

# Función base para mapa estático coroplético
def exportar_mapa_estatico(gdf, columna, titulo, leyenda_label, nombre_archivo,
                            cmap="YlOrRd", categorico=False, paleta_cat=None):
    fig, ax = plt.subplots(1, 1, figsize=(12, 14))
    if categorico and paleta_cat:
        colores = gdf[columna].map(paleta_cat)
        gdf.plot(ax=ax, color=colores, edgecolor="white", linewidth=0.3)
        parches = [mpatches.Patch(color=v, label=k) for k, v in paleta_cat.items()]
        ax.legend(handles=parches, title=leyenda_label, loc="lower right", fontsize=9)
    else:
        gdf.plot(column=columna, ax=ax, cmap=cmap, legend=True,
                 legend_kwds={"label": leyenda_label, "orientation": "vertical"},
                 edgecolor="white", linewidth=0.3, missing_kwds={"color": "#cccccc"})
    ax.set_title(titulo, fontsize=14, fontweight="bold", pad=15)
    ax.set_axis_off()
    ax.annotate(f"Fuente: {FUENTE_DATOS}", xy=(0.01, 0.01),
                xycoords="axes fraction", fontsize=7, color="#666666")
    plt.tight_layout()
    ruta_salida = RUTA_MAPAS_ESTATICOS / f"{nombre_archivo}.{FORMATO_ESTATICO}"
    plt.savefig(ruta_salida, dpi=DPI_ESTATICO, bbox_inches="tight")
    plt.close()
    print(f"  ✓ Exportado: {ruta_salida.name}")

# --- Mapa 1: Demanda Potencial ---
exportar_mapa_estatico(
    gdf, "D1_norm",
    "Mapa 1 — Demanda Potencial de Cuidados\nEcuador, escala cantonal",
    "Índice D1 (0=menor, 1=mayor demanda)",
    "mapa_01_demanda", cmap="Blues"
)

# --- Mapa 2: Oferta Institucional ---
exportar_mapa_estatico(
    gdf, "D2_norm",
    "Mapa 2 — Brecha de Oferta Institucional CDI/CNH\nEcuador, escala cantonal",
    "Índice D2 invertido (0=más cobertura, 1=menos cobertura)",
    "mapa_02_oferta", cmap="Reds"
)

# --- Mapa 3: Brecha Oferta-Demanda ---
exportar_mapa_estatico(
    gdf, "IBTC",
    "Mapa 3 — Brecha Oferta-Demanda de Cuidados\nEcuador, escala cantonal",
    "Valor IBTC (componentes D1+D2)",
    "mapa_03_brecha", cmap="OrRd"
)

# --- Mapa 4: IBTC y Tipología (MAPA PRINCIPAL) ---
exportar_mapa_estatico(
    gdf, "tipologia",
    f"Mapa 4 — {TITULO_PROYECTO}\nTipología Territorial · Ecuador · Escala cantonal",
    "Categoría IBTC",
    "mapa_04_ibtc_tipologia",
    categorico=True, paleta_cat=PALETA_IBTC
)

# --- Mapa 5: TNR contextual (provincial) ---
exportar_mapa_estatico(
    gdf, "D3_norm",
    "Mapa 5 — Carga de Trabajo No Remunerado Femenino (contexto provincial)\nEcuador",
    "Brecha TNR normalizada (horas mujer − hombre)",
    "mapa_05_tnr_contextual", cmap="PuRd"
)

# --- Mapa interactivo principal (folium) ---
print("\n  Generando mapa interactivo principal (folium)...")
gdf_wgs = gdf.to_crs(CRS_PROYECTO)
centro = [gdf_wgs.geometry.centroid.y.mean(), gdf_wgs.geometry.centroid.x.mean()]
m = folium.Map(location=centro, zoom_start=6, tiles="CartoDB positron")

def estilo_ibtc(feature):
    tipologia = feature["properties"].get("tipologia", "Sin datos")
    color = PALETA_IBTC.get(tipologia, "#cccccc")
    return {"fillColor": color, "color": "white", "weight": 0.5, "fillOpacity": 0.8}

folium.GeoJson(
    gdf_wgs.__geo_interface__,
    name="IBTC Tipología",
    style_function=estilo_ibtc,
    tooltip=folium.GeoJsonTooltip(
        fields=["DPA_DESCAN", "DPA_DESPRO", "IBTC", "tipologia", "D1_norm", "D2_norm", "D3_norm"],
        aliases=["Cantón", "Provincia", "IBTC", "Categoría", "D1 Demanda", "D2 Oferta (inv.)", "D3 TNR"],
        localize=True
    )
).add_to(m)

folium.LayerControl().add_to(m)
ruta_html = RUTA_MAPAS_INTERACTIVOS / "mapa_04_ibtc_tipologia.html"
m.save(str(ruta_html))
print(f"  ✓ Mapa interactivo exportado: {ruta_html.name}")

print("\n=== MAPAS COMPLETADOS ===")
