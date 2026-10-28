# Geometría cantonal

`cantones_ecuador_221.geojson` — 221 polígonos cantonales (EPSG:4326, 5 decimales) con las propiedades:

| Propiedad | Descripción |
|-----------|-------------|
| `cod_dpa` | Código DPA de cantón, texto de 4 caracteres (clave de unión) |
| `canton`  | Nombre del cantón según el código DPA |
| `provincia` | Provincia |

Origen: geometría simplificada (CONALI 2022) tal como estaba embebida en el mapa interactivo del Atlas;
el código DPA se asignó cruzando nombre de polígono con `../dpa_cantones_oficial.csv`.
Para máxima precisión cartográfica, sustituir por el shapefile oficial manteniendo la propiedad `cod_dpa`.
