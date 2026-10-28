# Codigo

| Archivo | Descripcion | Estado |
|---------|-------------|--------|
| config.py | Parámetros centralizados (sección 2 = estructura real del repo) | vigente |
| 02_generar_mapas.py | Genera los 5 mapas estáticos (PNG+PDF) desde `02_datos/ibtc_cantones_final.csv` + `02_datos/geo/*.geojson`, uniendo por código DPA | **reproducible con los datos del repo** |
| utilidades/corregir_nombres_dpa.py | Reasigna nombres de cantón por código DPA en XLSX y CSV | vigente |
| utilidades/corregir_html_interactivo.py | Reasigna datos y colores del mapa interactivo por código DPA | vigente |
| 01_pipeline_ibtc.py | Pipeline de especificación original (ETL desde fuentes crudas) | **No reproduce el dataset publicado**: define D2 con cobertura CDI/CNH y D3 con TNR provincial, mientras el dataset usa proxy 0-3 años y NBI. Requiere fuentes crudas que no están en el repo. |

Generar mapas:

    pip install -r requirements.txt
    python 01_codigo/02_generar_mapas.py

Regla de oro: la unión entre geometría y datos se hace por código DPA (texto, 4 caracteres), nunca por nombre ni por orden.
