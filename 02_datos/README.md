# Datos

Dataset maestro IBTC con los 221 cantones de Ecuador. **Clave de unión: código DPA (texto de 4 caracteres, con cero inicial).**

| Archivo | Descripcion |
|---------|-------------|
| ibtc_cantones_final.csv | Dataset maestro 221 cantones: código DPA, nombre, provincia, D1-D3, IBTC, tipología y variables censales |
| IBTC_Dataset_Maestro_DAT4CCION2026.xlsx | Excel con 4 hojas: datos, resumen tipología, top 20, GeoPackages |
| dpa_cantones_oficial.csv | Tabla DPA (código-cantón-provincia) usada para validar nombres. La Concordia figura como 2302 (Censo 2022). **Validar contra INEC/CONALI antes de citar.** |
| reporte_correccion_nombres_dpa.csv | Una fila por cantón: nombre publicado antes de la corrección vs nombre corregido |
| geo/cantones_ecuador_221.geojson | Geometría cantonal con `cod_dpa` |
| DICCIONARIO_BDD_CANTON.md | Diccionario de variables Censo 2022 |
| geopaquetes/README_GEOPAQUETES.md | GeoPackages disponibles en Google Drive |

Los archivos GeoPackage (.gpkg) no estan en este repositorio por tamano.

## Corrección de nombres (octubre 2026)

La versión inicial del XLSX rotulaba con nombre equivocado 173 de 221 cantones (el nombre pertenecía a otro cantón
de la misma provincia). Los códigos DPA y los valores D1, D2, D3 e IBTC **no cambiaron**; se corrigió la columna Cantón,
la hoja Top20_Mayor_Brecha, el mapa interactivo y los 5 mapas estáticos. Detalle por cantón en
`reporte_correccion_nombres_dpa.csv`. **Usar siempre el código DPA como clave, nunca el nombre.**
