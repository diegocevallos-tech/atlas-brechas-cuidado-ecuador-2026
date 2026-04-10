# Atlas Territorial de Brechas de Cuidado
## Modelo de priorización cantonal para políticas de igualdad de género en Ecuador
### DAT4CCIÓN 2026 — ONU Mujeres

---

## ¿Qué es este proyecto?

El **Índice de Brecha Territorial de Cuidado (IBTC)** clasifica los 221 cantones de Ecuador
en cuatro categorías de urgencia de intervención para políticas de cuidado, integrando:

- **D1** — Demanda Potencial de Cuidados (peso 40%)
- **D2** — Presión de Demanda Infantil — proxy oferta CDI/CNH (peso 40%)
- **D3** — Vulnerabilidad Estructural — proxy carga TNR (peso 20%)

**Fórmula:** `IBTC = 0.40 × D1_norm + 0.40 × D2_norm + 0.20 × D3_norm`

**Tipología:** Crítico · Vulnerable · En Transición · Cobertura Relativa

---

## Resultados principales

| Categoría | N° Cantones | IBTC |
|-----------|------------|------|
| Crítico | 55 | > 0.455 |
| Vulnerable | 55 | 0.372 – 0.455 |
| En Transición | 55 | 0.279 – 0.372 |
| Cobertura Relativa | 56 | < 0.279 |

---

## Estructura del repositorio## Estructura del repositorio
atlas-brechas-cuidado-ecuador-2026/
├── codigo/
│   ├── config.py                    ← parámetros editables centralizados
│   ├── 01_pipeline_ibtc.py          ← ETL + cálculo IBTC
│   ├── 02_generar_mapas.py          ← mapas estáticos e interactivos
│   └── requirements.txt
├── datos/
│   └── ibtc_cantones_final.csv      ← dataset maestro 221 cantones
├── mapas/
│   ├── estaticos/                   ← PNG 300 dpi
│   └── interactivos/                ← HTML folium
└── docs/
└── Metodologia_IBTC_DAT4CCION2026.docx---

## Cómo ejecutar

```bash
pip install -r codigo/requirements.txt
python codigo/01_pipeline_ibtc.py
python codigo/02_generar_mapas.py
```

---

## Datos necesarios

| Fuente | Archivo | Origen |
|--------|---------|--------|
| Censo 2022 | CPV_2022_Población_Canton.csv | ecuadorencifras.gob.ec |
| Censo 2022 | CPV_2022_Hogar_Canton.csv | ecuadorencifras.gob.ec |
| CNRH 2023 | Tabulados_CSTNRH_CSV/ | ecuadorencifras.gob.ec |
| CONALI 2022 | cantones_ecuador.shp | geoportaligm.gob.ec |

---

## Replicabilidad en América Latina

Para replicar en otro país: ajustar `config.py` con nombres de columnas locales.
Requisitos mínimos: censo municipal reciente + cartografía de límites + datos de servicios de cuidado.

---

## Fuentes

- INEC Ecuador — Censo de Población y Vivienda 2022
- INEC Ecuador — Cuenta Satélite del Trabajo No Remunerado 2023
- MIES Ecuador — SIIMIES Q4 2024 (portal no disponible durante procesamiento)
- CONALI / IGM — Shapefiles División Político-Administrativa 2022

---

## Evento

**DAT4CCIÓN 2026 — Datatón Regional para la Igualdad**
ONU Mujeres · Abril 2026

*Categoría: Mapa · Temática: Cuidados y Trabajo No Remunerado · País: Ecuador*
