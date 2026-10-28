"""
02_generar_mapas.py
===================
Genera los 5 mapas estáticos del Atlas (PNG y PDF) desde UNA sola fuente:
  - 02_datos/ibtc_cantones_final_con_nombres.csv   (valores + código DPA)
  - 02_datos/geo/cantones_ecuador_221.geojson      (geometría + código DPA)
La unión polígono-dato se hace SIEMPRE por código DPA (texto de 4 caracteres),
nunca por nombre ni por orden de filas.

Dependencias: matplotlib, numpy (ver requirements.txt). No requiere geopandas.

EJECUTAR (desde cualquier carpeta):
  python 01_codigo/02_generar_mapas.py [--salida <carpeta>] [--solo 1 2 3 4 5]

QUÉ EDITAR: config.py (rutas, colores) y el bloque MAPAS de este archivo (textos, paletas).
"""

import argparse
import csv
import json
import math
import sys
from pathlib import Path

import warnings
import matplotlib
matplotlib.use("Agg")
warnings.filterwarnings("ignore", message="Ignoring fixed .* limits")
import logging
logging.getLogger("matplotlib").setLevel(logging.ERROR)   # avisos de aspect/limits sin efecto
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm, colors as mcolors
from matplotlib.collections import PathCollection
from matplotlib.patches import Rectangle
from matplotlib.path import Path as MPath

sys.path.insert(0, str(Path(__file__).parent))
import config as C

# ─────────────────────────── DEFINICIÓN DE MAPAS ───────────────────────────
# tipo: "continuo" (colorbar de la columna) | "categorico" (tipología)
# texto: lista de (estilo, línea). estilo: "h" subtítulo, "b" viñeta, "t" texto
MAPAS = [
    {
        "id": 1, "archivo": "mapa_01_demanda_final", "tipo": "continuo",
        "columna": "D1_norm", "cmap": "YlGnBu",
        "titulo": "Demanda Potencial de Cuidados",
        "subtitulo": "Índice D1 normalizado por cantón · Ecuador · Censo 2022",
        "texto": [
            ("h", "Índice D1 — Demanda Potencial"),
            ("b", "Variables utilizadas (Censo 2022):"),
            ("t", "– % población menor de 5 años"), ("t", "– % población mayor de 65 años"),
            ("t", "– % personas con discapacidad"), ("t", "– % hogares con jefatura femenina"),
            ("b", "Método de construcción:"),
            ("t", "1. Normalización min-max [0–1]"), ("t", "2. Promedio simple de los 4 factores"),
        ],
        "descripcion": [
            "El índice D1 identifica los cantones con mayor concentración de población con necesidad potencial de servicios de cuidado. Los cantones más oscuros",
            "presentan mayor presión estructural sobre las mujeres en edad activa, encargadas de absorber la carga en ausencia de servicios.",
        ],
        "fuente": "Fuente de datos: INEC — Censo de Población y Vivienda 2022 | Cartografía: CONALI 2022",
    },
    {
        "id": 2, "archivo": "mapa_02_oferta_final", "tipo": "continuo",
        "columna": "D2_norm", "cmap": "YlOrRd",
        "titulo": "Presión de Demanda Infantil",
        "subtitulo": "Proxy de brecha de oferta CDI/CNH · Ecuador · Censo 2022",
        "texto": [
            ("h", "Índice D2 — Proxy Oferta"),
            ("b", "Variable utilizada (Censo 2022):"), ("t", "– Proporción de población 0-3 años"),
            ("b", "Justificación y Limitación:"),
            ("t", "Al no disponer de cobertura CDI/CNH"), ("t", "(fuente MIES caída), se usa la masa"),
            ("t", "crítica de demanda como proxy de"), ("t", "la magnitud de la brecha territorial."),
        ],
        "descripcion": [
            "El índice D2 mide la presión sobre los servicios de desarrollo infantil basándose en la proporción poblacional de primera infancia (0-3 años). A falta",
            "de datos MIES, este indicador asume que a mayor presión sin cobertura verificable, mayor carga de cuidado no remunerado.",
        ],
        "fuente": "Fuente de datos: INEC — Censo de Población y Vivienda 2022 | Cartografía: CONALI 2022",
    },
    {
        "id": 3, "archivo": "mapa_03_vulnerabilidad_final", "tipo": "continuo",
        "columna": "D3_norm", "cmap": "RdPu",
        "titulo": "Vulnerabilidad Estructural del Territorio",
        "subtitulo": "Índice D3 — Necesidades Básicas Insatisfechas · Ecuador · Censo 2022",
        "texto": [
            ("h", "Índice D3 — Proxy Estructural"),
            ("b", "Variable utilizada (Censo 2022):"), ("t", "– % hogares con NBI"),
            ("b", "Limitación documentada:"),
            ("t", "La Cuenta Satélite de Trabajo No"), ("t", "Remunerado solo llega a nivel"),
            ("t", "provincial. Por lo que se emplea"), ("t", "NBI como proxy cantonal."),
        ],
        "descripcion": [
            "El índice D3 captura el estado socioeconómico del territorio como agravante del déficit de cuidado. Cantones con mayor pobreza por Necesidades Básicas",
            "Insatisfechas (NBI) experimentan un endurecimiento de las condiciones que facilitan el trabajo de cuidado no remunerado.",
        ],
        "fuente": "Fuente de datos: INEC — Censo de Población y Vivienda 2022 | Cartografía: CONALI 2022",
    },
    {
        "id": 4, "archivo": "mapa_04_ibtc_continuo_final", "tipo": "continuo",
        "columna": "IBTC", "cmap": "YlOrBr",
        "titulo": "Índice de Brecha Territorial de Cuidado (IBTC)",
        "subtitulo": "Índice Sintético de Priorización · Ecuador · Censo 2022",
        "texto": [
            ("h", "IBTC — Índice Sintético"),
            ("b", "Fórmula metodológica:"), ("t", "IBTC = {PESO_D1:.2f}(D1) + {PESO_D2:.2f}(D2) + {PESO_D3:.2f}(D3)"),
            ("b", "Ponderación Institucional:"),
            ("t", "Equidad en parámetros de demanda y"), ("t", "menor peso a variables proxy."),
            ("b", "Mayor valor (Rojo) = Máxima brecha"),
        ],
        "descripcion": [
            "El IBTC combina las dimensiones de demanda potencial (D1), presión infantil (D2) y vulnerabilidad (D3). Identifica el nivel acumulado de déficits",
            "estructurales que condicionan la carga de cuidado no remunerado. Máximo teórico: 1.0. Rango nacional: {min:.2f} a {max:.2f}.",
        ],
        "fuente": "Fuente de datos: INEC — Censo de Población y Vivienda 2022 | Metodología ONU Mujeres | Cartografía: CONALI 2022",
    },
    {
        "id": 5, "archivo": "mapa_05_ibtc_tipologia_final", "tipo": "categorico",
        "columna": "tipologia", "cmap": None,
        "titulo": "Atlas Territorial de Brechas de Cuidado",
        "subtitulo": "Tipología cantonal estratégica para la política pública · Ecuador · 2022",
        "texto": [
            ("h", "Tipología territorial"),
            ("b", "Método de discretización:"), ("t", "Clasificación por Cuartiles del IBTC."),
            ("b", "Categorías:"),
            ("t", "– Crítico: > percentil 75 (Q4)"), ("t", "– Vulnerable: Q3"),
            ("t", "– En Transición: Q2"), ("t", "– Cobertura Relativa: < p25 (Q1)"),
        ],
        "descripcion": [
            "Clasificación accionable de los {n} cantones en cuatro niveles de urgencia. Los cantones Críticos concentran alta presión y vulnerabilidad estructural",
            "simultánea, representando territorios prioritarios para expansión acelerada de servicios.",
        ],
        "fuente": "Fuente de datos: INEC — Censo de Población y Vivienda 2022 | Cartografía: CONALI 2022",
    },
]

COLUMNAS_REQUERIDAS = ["D1_norm", "D2_norm", "D3_norm", "IBTC", "tipologia", "NOMBRE_CANTON"]
ORDEN_TIPOLOGIA = ["Crítico", "Vulnerable", "En Transición", "Cobertura Relativa"]


# ─────────────────────────── CARGA Y VALIDACIÓN ───────────────────────────
def cargar_datos(ruta_csv: Path) -> dict:
    if not ruta_csv.exists():
        raise FileNotFoundError(f"CSV no encontrado: {ruta_csv}")
    with open(ruta_csv, encoding="utf-8-sig", newline="") as f:
        filas = list(csv.DictReader(f))
    faltan = [c for c in [C.COL_CSV_CODIGO] + COLUMNAS_REQUERIDAS if c not in filas[0]]
    if faltan:
        raise KeyError(f"Columnas no encontradas en {ruta_csv.name}: {faltan}")
    datos = {}
    for r in filas:
        cod = r[C.COL_CSV_CODIGO].strip().zfill(C.LARGO_CODIGO_DPA)
        if cod in datos:
            raise ValueError(f"Código DPA duplicado en el CSV: {cod}")
        for k in ("D1_norm", "D2_norm", "D3_norm", "IBTC"):
            r[k] = float(r[k])
        datos[cod] = r
    return datos


def cargar_geometria(ruta_geo: Path) -> list:
    if not ruta_geo.exists():
        raise FileNotFoundError(f"GeoJSON no encontrado: {ruta_geo}")
    fc = json.loads(ruta_geo.read_text(encoding="utf-8"))
    feats = fc["features"]
    cods = [f["properties"][C.COL_GEO_CODIGO] for f in feats]
    if len(set(cods)) != len(cods):
        raise ValueError("Códigos DPA duplicados en el GeoJSON.")
    return feats


def validar_union(datos: dict, feats: list):
    g = {f["properties"][C.COL_GEO_CODIGO] for f in feats}
    d = set(datos)
    if g != d:
        raise ValueError(f"La unión por código DPA no cierra. Solo en geometría: {sorted(g - d)} | "
                         f"solo en datos: {sorted(d - g)}")


# ─────────────────────────── GEOMETRÍA → MATPLOTLIB ───────────────────────────
def anillos(geom: dict):
    """Devuelve lista de polígonos; cada polígono = lista de anillos [(x,y),...] (exterior + huecos)."""
    if geom["type"] == "Polygon":
        return [geom["coordinates"]]
    if geom["type"] == "MultiPolygon":
        return geom["coordinates"]
    raise ValueError(f"Geometría no soportada: {geom['type']}")


def a_path(geom: dict) -> MPath:
    verts, codes = [], []
    for poli in anillos(geom):
        for anillo in poli:
            pts = np.asarray(anillo, dtype=float)
            verts.extend(pts.tolist())
            codes.extend([MPath.MOVETO] + [MPath.LINETO] * (len(pts) - 2) + [MPath.CLOSEPOLY])
    return MPath(verts, codes)


def limites(feats):
    xs, ys = [], []
    for f in feats:
        for poli in anillos(f["geometry"]):
            for anillo in poli:
                a = np.asarray(anillo)
                xs.append(a[:, 0]); ys.append(a[:, 1])
    xs, ys = np.concatenate(xs), np.concatenate(ys)
    return xs.min(), xs.max(), ys.min(), ys.max()


def dibujar_capa(ax, feats, color_de):
    paths = [a_path(f["geometry"]) for f in feats]
    fc = [color_de(f["properties"][C.COL_GEO_CODIGO]) for f in feats]
    ax.add_collection(PathCollection(paths, facecolors=fc, edgecolors="white", linewidths=0.35))


def preparar_eje_mapa(ax, feats, margen=0.15):
    x0, x1, y0, y1 = limites(feats)
    ax.set_xlim(x0 - margen, x1 + margen)
    ax.set_ylim(y0 - margen, y1 + margen)
    ax.set_aspect("equal", adjustable="datalim")
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_facecolor(C.COLOR_FONDO_MAPA)
    for s in ax.spines.values():
        s.set_color("#BFC5CC"); s.set_linewidth(1.0)


# ─────────────────────────── RENDER DE UN MAPA ───────────────────────────
def renderizar(m: dict, datos: dict, feats: list, carpeta: Path):
    peninsula = [f for f in feats if f["properties"]["provincia"].upper().replace("Á", "A") != C.PROVINCIA_INSULAR]
    insular = [f for f in feats if f["properties"]["provincia"].upper().replace("Á", "A") == C.PROVINCIA_INSULAR]
    if not insular:
        raise ValueError(f"No hay polígonos de la provincia insular '{C.PROVINCIA_INSULAR}'.")

    valores = [datos[f["properties"][C.COL_GEO_CODIGO]][m["columna"]] for f in feats]
    ctx = {"n": len(datos)}
    if m["tipo"] == "continuo":
        vmin, vmax = min(valores), max(valores)
        norm = mcolors.Normalize(vmin=vmin, vmax=vmax)
        cmap = matplotlib.colormaps[m["cmap"]]
        color_de = lambda cod: cmap(norm(datos[cod][m["columna"]]))
        ctx.update({"min": vmin, "max": vmax})
    else:
        color_de = lambda cod: C.PALETA_TIPOLOGIA_MAPAS.get(datos[cod]["tipologia"], C.COLOR_SIN_DATO)

    fig = plt.figure(figsize=C.TAMANO_MAPA_PULG, dpi=C.DPI_MAPA, facecolor="white")
    # barra superior y encabezado
    fig.add_artist(Rectangle((0, 0.9885), 1, 0.0035, transform=fig.transFigure, color=C.COLOR_ACENTO))
    fig.text(0.5, 0.947, m["titulo"], ha="center", va="center", fontsize=30, fontweight="bold", color=C.COLOR_TEXTO)
    fig.text(0.5, 0.912, m["subtitulo"], ha="center", va="center", fontsize=19, style="italic", color=C.COLOR_TEXTO_SUAVE)
    fig.text(0.992, 0.948, "DAT4CCIÓN 2026", ha="right", va="center", fontsize=14, fontweight="bold", color=C.COLOR_ACENTO)
    fig.text(0.992, 0.912, "ONU Mujeres", ha="right", va="center", fontsize=13, color=C.COLOR_TEXTO_SUAVE)

    # mapa principal
    ax = fig.add_axes([0.0064, 0.155, 0.668, 0.711])
    dibujar_capa(ax, peninsula, color_de)
    preparar_eje_mapa(ax, peninsula)
    x0, x1 = ax.get_xlim(); y0, y1 = ax.get_ylim()
    # norte
    nx = x1 - 0.06 * (x1 - x0); ny0 = y1 - 0.15 * (y1 - y0); ny1 = y1 - 0.05 * (y1 - y0)
    ax.annotate("", xy=(nx, ny1), xytext=(nx, ny0), arrowprops=dict(arrowstyle="-|>", color=C.COLOR_TEXTO, lw=3))
    ax.text(nx, ny1 + 0.01 * (y1 - y0), "N", ha="center", va="bottom", fontsize=20, fontweight="bold", color=C.COLOR_TEXTO)
    # escala (grados de longitud para LONGITUD_ESCALA_KM en la latitud central)
    lat_c = (y0 + y1) / 2
    grados = C.LONGITUD_ESCALA_KM / (111.32 * math.cos(math.radians(lat_c)))
    sx0 = x0 + 0.64 * (x1 - x0); sy = y0 + 0.29 * (y1 - y0)   # zona libre (mar/Perú), sin tapar cantones
    ax.plot([sx0, sx0 + grados], [sy, sy], color=C.COLOR_TEXTO, lw=3)
    for xx in (sx0, sx0 + grados):
        ax.plot([xx, xx], [sy - 0.012 * (y1 - y0), sy + 0.012 * (y1 - y0)], color=C.COLOR_TEXTO, lw=3)
    ax.text(sx0 + grados / 2, sy + 0.025 * (y1 - y0), f"≈ {C.LONGITUD_ESCALA_KM} km", ha="center", fontsize=12, color=C.COLOR_TEXTO)

    # recuadro Galápagos
    axg = fig.add_axes([0.4997, 0.172, 0.154, 0.111])
    dibujar_capa(axg, insular, color_de)
    preparar_eje_mapa(axg, insular, margen=0.1)
    axg.set_xlim(axg.get_xlim()); axg.set_ylim(axg.get_ylim())
    fig.text(0.4997 + 0.077, 0.172 + 0.111 + 0.008, "Islas Galápagos", ha="center", fontsize=11,
             fontweight="bold", color=C.COLOR_TEXTO_SUAVE)

    # panel derecho
    panel = fig.add_axes([0.685, 0.140, 0.307, 0.741])
    panel.set_xlim(0, 1); panel.set_ylim(0, 1); panel.axis("off")
    panel.add_patch(Rectangle((0, 0), 1, 1, transform=panel.transAxes, facecolor="#FAFBFD",
                              edgecolor="#E2E5EA", lw=1, zorder=0))
    panel.text(0.08, 0.935, "LEYENDA", fontsize=14, fontweight="bold", color=C.COLOR_TEXTO, va="center")
    panel.plot([0.08, 0.95], [0.905, 0.905], color="#D9DCE1", lw=1)
    y_texto = 0.45
    if m["tipo"] == "categorico":
        conteo = {t: 0 for t in ORDEN_TIPOLOGIA}
        sin_dato = 0
        for cod in datos:
            t = datos[cod]["tipologia"]
            if t in conteo: conteo[t] += 1
            else: sin_dato += 1
        y = 0.835
        for t in ORDEN_TIPOLOGIA:
            panel.add_patch(Rectangle((0.08, y - 0.021), 0.10, 0.042, transform=panel.transAxes,
                                      facecolor=C.PALETA_TIPOLOGIA_MAPAS[t], edgecolor="none"))
            panel.text(0.23, y + 0.012, t, fontsize=14, fontweight="bold", color=C.COLOR_TEXTO, va="center")
            panel.text(0.23, y - 0.020, f"{conteo[t]} cantones ({100 * conteo[t] / len(datos):.1f}%)",
                       fontsize=11, color="#666666", va="center")
            y -= 0.092
        if sin_dato:
            panel.add_patch(Rectangle((0.08, y - 0.021), 0.10, 0.042, transform=panel.transAxes,
                                      facecolor=C.COLOR_SIN_DATO, edgecolor="none"))
            panel.text(0.23, y, f"Sin dato ({sin_dato})", fontsize=12, style="italic", color="#666666", va="center")
            y -= 0.092
        y_texto = y - 0.015
    else:
        cax = panel.inset_axes([0.10, 0.50, 0.07, 0.38])
        sm = cm.ScalarMappable(norm=norm, cmap=cmap)
        cb = fig.colorbar(sm, cax=cax)
        cb.ax.tick_params(labelsize=10)
        cb.outline.set_linewidth(0.6)
        panel.text(0.08, 0.465, f"Rango: {ctx['min']:.3f} – {ctx['max']:.3f}", fontsize=10, color="#666666", va="center")
        panel.text(0.08, 0.435, "Mayor valor = mayor brecha", fontsize=11, fontweight="bold", color=C.COLOR_TEXTO, va="center")
        y_texto = 0.395
    panel.text(0.08, y_texto, "CÓMO SE CONSTRUYÓ ESTE MAPA", fontsize=13, fontweight="bold", color=C.COLOR_ACENTO, va="center")
    panel.plot([0.08, 0.95], [y_texto - 0.03, y_texto - 0.03], color="#EBB4D0", lw=1.5)
    y = y_texto - 0.075
    fmt = {"PESO_D1": C.PESO_D1, "PESO_D2": C.PESO_D2, "PESO_D3": C.PESO_D3}
    for estilo, linea in m["texto"]:
        linea = linea.format(**fmt)
        if estilo == "h":
            panel.text(0.08, y, linea, fontsize=13, fontweight="bold", color=C.COLOR_TEXTO, va="center"); y -= 0.045
        elif estilo == "b":
            panel.text(0.08, y, "● " + linea, fontsize=11.5, color="#333333", va="center"); y -= 0.034
        else:
            panel.text(0.09, y, linea, fontsize=11, color="#222222", va="center"); y -= 0.030
    if y < 0.0:
        raise ValueError(f"Mapa {m['id']}: el texto del panel excede el recuadro; reducir líneas en MAPAS.")

    # pie
    fig.add_artist(plt.Line2D([0.0064, 0.992], [0.123, 0.123], color="#D9DCE1", lw=1, transform=fig.transFigure))
    fig.text(0.0064, 0.107, "Descripción", fontsize=14, fontweight="bold", color=C.COLOR_TEXTO, va="center")
    for i, linea in enumerate(m["descripcion"]):
        fig.text(0.0064, 0.082 - i * 0.025, linea.format(**ctx), fontsize=12.5, color="#222222", va="center")
    fig.text(0.0064, 0.021, m["fuente"], fontsize=11, color=C.COLOR_TEXTO_SUAVE, va="center")
    fig.text(0.992, 0.021, "Atlas Territorial de Brechas de Cuidado · Ecuador · 2022", ha="right", fontsize=11,
             style="italic", color=C.COLOR_TEXTO_SUAVE, va="center")

    carpeta.mkdir(parents=True, exist_ok=True)
    for ext in C.FORMATOS_MAPA:
        fig.savefig(carpeta / f"{m['archivo']}.{ext}", dpi=C.DPI_MAPA, facecolor="white")
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--salida", default=None, help="Carpeta de salida (por defecto config.RUTA_SALIDA_MAPAS)")
    ap.add_argument("--solo", nargs="*", type=int, default=None, help="IDs de mapas a generar (1-5)")
    a = ap.parse_args()
    carpeta = Path(a.salida).resolve() if a.salida else C.RUTA_SALIDA_MAPAS

    datos = cargar_datos(C.CSV_DATASET)
    feats = cargar_geometria(C.GEOJSON_CANTONES)
    validar_union(datos, feats)
    cuenta = {}
    for r in datos.values():
        cuenta[r["tipologia"]] = cuenta.get(r["tipologia"], 0) + 1
    print(f"Unión por código DPA OK: {len(datos)} cantones | tipología: {cuenta}")
    for m in MAPAS:
        if a.solo and m["id"] not in a.solo:
            continue
        renderizar(m, datos, feats, carpeta)
        print(f"  ✓ {m['archivo']}")


if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, KeyError, ValueError) as e:
        sys.exit(f"[ERROR] {e}")
