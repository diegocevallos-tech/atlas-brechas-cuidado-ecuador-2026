# Atlas Territorial de Brechas de Cuidado
## Modelo de priorización cantonal para políticas de igualdad de género en Ecuador
### DAT4CCIÓN 2026 — Datatón Regional para la Igualdad | ONU Mujeres

---

## Sobre el proyecto

El **Índice de Brecha Territorial de Cuidado (IBTC)** clasifica los **221 cantones de Ecuador**
en cuatro categorías de urgencia de intervención para políticas de cuidado, integrando tres
dimensiones del déficit territorial:

| Dimensión | Código | Descripción | Peso |
|-----------|--------|-------------|------|
| Demanda Potencial | D1 | % menores 5, mayores 65, discapacidad, jefatura femenina | 40% |
| Oferta CDI/CNH (proxy) | D2 | Ratio población 0-3 años / población total | 40% |
| Vulnerabilidad Estructural | D3 | % hogares con NBI | 20% |

**Fórmula:** `IBTC = 0.40 × D1_norm + 0.40 × D2_norm + 0.20 × D3_norm`

---

## Resultados principales

| Categoría | Cantones | Descripción | Prioridad |
|-----------|----------|-------------|-----------|
| 🔴 Crítico | 55 (25%) | Mayor brecha acumulada en las 3 dimensiones | Máxima |
| 🟠 Vulnerable | 55 (25%) | Brecha significativa | Alta |
| 🟡 En Transición | 55 (25%) | Brecha moderada | Media |
| 🟢 Cobertura Relativa | 56 (25%) | Menor brecha relativa | Mantenimiento |

---

## Entregables del proyecto

### 📊 Mapas estáticos (PNG 300 dpi + PDF)
Carpeta: `03_mapas/estaticos/`

| Archivo | Descripción |
|---------|-------------|
| `mapa_01_demanda_final.png` | Demanda Potencial de Cuidados (D1) |
| `mapa_02_oferta_final.png` | Presión de Demanda Infantil — proxy CDI/CNH (D2) |
| `mapa_03_vulnerabilidad_final.png` | Vulnerabilidad Estructural NBI (D3) |
| `mapa_04_ibtc_continuo_final.png` | Índice IBTC — valor continuo |
| `mapa_05_ibtc_tipologia_final.png` | **Tipología Territorial — MAPA PRINCIPAL** |

### 🗺️ Mapa interactivo
Carpeta: `03_mapas/interactivos/`

- `atlas_brechas_interactivo_final.html` — Explorador cantonal con tooltip
  por cantón mostrando IBTC, tipología, D1, D2, D3.
  **Abrir directamente en el navegador — no requiere instalación.**

### 📋 Infografía
Carpeta: `04_infografia/`

- `infografia_atlas_brechas_cuidado_A3.png` — Infografía A3 completa
- `infografia_atlas_brechas_cuidado_A3.pdf` — Versión PDF

### 📄 Informe técnico oficial
Carpeta: `05_informe/`

- `Datacccion2026_Mapa_Atlas_Territorial_Brechas_Cuidado.docx`
  Informe según plantilla oficial DAT4CCIÓN 2026. Incluye:
  introducción, justificación, datos y metodología, desarrollo,
  conclusiones, uso de IA y fuentes.

### 📖 Documentación técnica
Carpeta: `06_docs/`

- `Metodologia_IBTC_DAT4CCION2026.docx` — Metodología detallada
  con 10 secciones: objetivo, fuentes, dimensiones, fórmula,
  normalización, tipología, proceso técnico, limitaciones,
  replicabilidad y usuarios.

### 🗃️ Datos procesados
Carpeta: `02_datos/`

| Archivo | Descripción |
|---------|-------------|
| `ibtc_cantones_final.csv` | Dataset maestro 221 cantones |
| `IBTC_Dataset_Maestro_DAT4CCION2026.xlsx` | Excel con 3 hojas: datos completos, resumen tipología, top 20 |
| `DICCIONARIO_BDD_CANTON.md` | Diccionario de variables del Censo 2022 |

### 💻 Código fuente
Carpeta: `01_codigo/`

| Archivo | Descripción |
|---------|-------------|
| `config.py` | **Todos los parámetros editables centralizados** |
| `01_pipeline_ibtc.py` | ETL + cálculo IBTC completo |
| `02_generar_mapas.py` | Generación de mapas estáticos e interactivos |
| `requirements.txt` | Dependencias Python |

---

## Cómo reproducir el análisis

```bash
# 1. Clonar el repositorio
git clone https://github.com/diegocevallos-tech/atlas-brechas-cuidado-ecuador-2026

# 2. Instalar dependencias
pip install -r 01_codigo/requirements.txt

# 3. Colocar datos fuente en las rutas indicadas en config.py
#    (ver sección Datos fuente más abajo)

# 4. Ejecutar pipeline
python 01_codigo/01_pipeline_ibtc.py

# 5. Generar mapas
python 01_codigo/02_generar_mapas.py
```

---

## Datos fuente requeridos

| Fuente | Institución | URL |
|--------|------------|-----|
| Censo de Población y Vivienda 2022 | INEC Ecuador | ecuadorencifras.gob.ec |
| Cuenta Satélite TNR 2023 | INEC Ecuador | ecuadorencifras.gob.ec |
| Shapefiles cantonales CONALI 2022 | IGM Ecuador | geoportaligm.gob.ec |

---

## Limitaciones documentadas

1. **D2 proxy censal** — datos MIES no disponibles durante el procesamiento
2. **D3 proxy NBI** — CNRH 2023 sin desagregación cantonal
3. **Escala cantonal** — brechas intracantonales no visibles

Ver documentación completa en `06_docs/Metodologia_IBTC_DAT4CCION2026.docx`

---

## Uso de inteligencia artificial

Se utilizó **Claude (Anthropic)** como asistente de codificación y redacción,
y **Antigravity/Codex** como entorno de ejecución Python.
Las decisiones metodológicas, validación de datos e interpretación
de resultados fueron realizadas por el equipo.

---

## Contexto normativo

- ODS 5 — Igualdad de género (ONU, 2015)
- Convención de Belém do Pará (OEA, 1995)
- Reconocimiento del derecho humano al cuidado — CIDH (agosto 2025)
- Agenda Nacional de Cuidados — Ecuador

---

## Equipo

**DC · CDLC · MA · RD**
DAT4CCIÓN 2026 — Datatón Regional para la Igualdad
ONU Mujeres | Categoría: Mapa | Cuidados y TNR | Ecuador · Abril 2026

---

*Todos los datos utilizados son de acceso público y gratuito.*
*El código es de uso libre bajo licencia MIT.*
