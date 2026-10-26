"""
corregir_html_interactivo.py
============================
Corrige el mapa interactivo (folium) cuyo join polígono-datos se hizo por nombre mal asignado.
Reasigna datos y colores de cada polígono según el código DPA oficial (permutación de filas).
No recalcula índices.

USO: python corregir_html_interactivo.py --html <in.html> --maestro <xlsx_original> --dpa <dpa.csv> --out <out.html>
"""
import argparse, json, re, sys, unicodedata
from pathlib import Path
import pandas as pd

CONFIG = {
    "HOJA_DATOS": "IBTC_221_Cantones", "FILA_ENCABEZADO": 3,
    "COL_COD": "Cód. DPA", "COL_CANTON": "Cantón", "COL_PROV": "Provincia",
    "PROP_NOMBRE": "CANTON_SHP", "PROP_PROV": "PROVINCIA_SHP",
    # propiedades de datos que viajan con el dato (todas menos nombre y provincia)
    "PROPS_FIJAS": ("CANTON_SHP", "PROVINCIA_SHP"),
    "RECODIFICAR_DPA": {"0808": "2302"},
    "ALIAS_DPA_A_NOMBRE": {  # nombre DPA normalizado -> nombre normalizado en el polígono/XLSX
        "ORELLANA": "FRANCISCO DE ORELLANA", "QUITO": "DISTRITO METROPOLITANO DE QUITO",
        "EMPALME": "EL EMPALME", "GNRAL ANTONIO ELIZALDE": "GENERAL ANTONIO ELIZALDE",
        "CRNEL MARCELINO MARIDUENA": "CORONEL MARCELINO MARIDUENA"},
    "PREFIJOS_EXCLUIR": ("90",),
    "PATRON_CAPA": r"_add\((\{\"bbox\")",
}

def norm(s):
    s = unicodedata.normalize("NFKD", str(s).upper()).encode("ascii", "ignore").decode()
    s = re.sub(r"\(.*?\)", "", s); s = re.sub(r"[^A-Z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def main():
    ap = argparse.ArgumentParser()
    for a in ("html", "maestro", "dpa", "out"): ap.add_argument(f"--{a}", required=True)
    a = ap.parse_args(); C = CONFIG
    html = Path(a.html).read_text(encoding="utf-8")

    dpa = pd.read_csv(a.dpa, dtype={"cod": str})
    dpa["cod"] = dpa["cod"].str.zfill(4).replace(C["RECODIFICAR_DPA"])
    dpa = dpa[~dpa["cod"].str.startswith(C["PREFIJOS_EXCLUIR"])]
    mx = pd.read_excel(a.maestro, sheet_name=C["HOJA_DATOS"], header=C["FILA_ENCABEZADO"]-1, dtype={C["COL_COD"]: str})
    mx = mx[mx[C["COL_COD"]].notna()].copy(); mx["cod"] = mx[C["COL_COD"]].str.zfill(4)
    label_by_cod = dict(zip(mx["cod"], mx[C["COL_CANTON"]].map(norm)))   # etiqueta publicada (errónea)
    prov_by_cod = dict(zip(mx["cod"], mx[C["COL_PROV"]].map(norm)))

    # Capas GeoJSON embebidas
    dec = json.JSONDecoder(); capas = []
    for m in re.finditer(C["PATRON_CAPA"], html):
        obj, end = dec.raw_decode(html, m.start(1)); capas.append((m.start(1), end, obj))
    if not capas: sys.exit("[ERROR] No se encontraron capas GeoJSON.")
    n = len(capas[0][2]["features"])
    ids = [f["id"] for f in capas[0][2]["features"]]
    for _, _, o in capas:
        if [f["id"] for f in o["features"]] != ids or \
           [f["properties"][C["PROP_NOMBRE"]] for f in o["features"]] != [f["properties"][C["PROP_NOMBRE"]] for f in capas[0][2]["features"]]:
            sys.exit("[ERROR] Las capas no comparten el mismo orden de polígonos.")

    # Para cada polígono i: código correcto -> etiqueta publicada de ese código -> polígono j que hoy muestra esos datos
    pos_by_key = {}
    for i, f in enumerate(capas[0][2]["features"]):
        pos_by_key[(norm(f["properties"][C["PROP_PROV"]]), norm(f["properties"][C["PROP_NOMBRE"]]))] = i
    dpa_by_prov = {}
    for _, r in dpa.iterrows():
        nm = norm(r["canton"]); nm = norm(C["ALIAS_DPA_A_NOMBRE"].get(nm, nm))
        dpa_by_prov.setdefault(r["cod"][:2], {})[nm] = r["cod"]
    prov2 = {}
    for cod, p in prov_by_cod.items(): prov2.setdefault(p, cod[:2])
    perm, cod_pol = {}, {}
    for i, f in enumerate(capas[0][2]["features"]):
        p, nm = norm(f["properties"][C["PROP_PROV"]]), norm(f["properties"][C["PROP_NOMBRE"]])
        cod = dpa_by_prov.get(prov2.get(p), {}).get(nm)
        if cod is None: sys.exit(f"[ERROR] Polígono sin código DPA: {p} / {nm}")
        j = pos_by_key.get((prov_by_cod[cod], label_by_cod[cod]))
        if j is None: sys.exit(f"[ERROR] Sin polígono para la etiqueta publicada del código {cod}")
        perm[i], cod_pol[i] = j, cod
    if sorted(perm.values()) != list(range(n)): sys.exit("[ERROR] La permutación no es biyectiva.")
    cambian = sum(1 for i, j in perm.items() if i != j)

    # Reasignar propiedades de datos
    nuevas = []
    for _, _, o in capas:
        viejas = [dict(f["properties"]) for f in o["features"]]
        for i, f in enumerate(o["features"]):
            for k, v in viejas[perm[i]].items():
                if k not in C["PROPS_FIJAS"]: f["properties"][k] = v
        nuevas.append(o)

    # Reescribir stylers: color del polígono i = color que tenía el polígono j
    salida = html
    for (ini, fin, _), o in sorted(zip(capas, nuevas), key=lambda t: -t[0][0]):
        salida = salida[:ini] + json.dumps(o) + salida[fin:]
    def reescribir(m):
        cuerpo = m.group(2)
        casos = re.findall(r'((?:case "\d+":\s*)+)return (\{.*?\});', cuerpo)
        defecto = re.search(r"default:\s*return (\{.*?\});", cuerpo).group(1)
        estilo = {}
        for ids_txt, st in casos:
            for idv in re.findall(r'case "(\d+)"', ids_txt): estilo[int(idv)] = st
        nuevo = {i: estilo.get(perm[i], defecto) for i in range(n)}
        grupos = {}
        for i, st in nuevo.items():
            if st != defecto: grupos.setdefault(st, []).append(i)
        txt = "switch(feature.id) {\n"
        for st, lst in grupos.items():
            txt += "                " + " ".join(f'case "{i}":' for i in sorted(lst)) + f"\n                    return {st};\n"
        txt += f"                default:\n                    return {defecto};\n            }}"
        return m.group(1) + txt
    pat = re.compile(r"(function geo_json_\w+_styler\(feature\) \{\s*)(switch\(feature\.id\) \{.*?default:\s*return \{.*?\};\s*\})", re.S)
    salida, k = pat.subn(reescribir, salida)
    if k != len(capas): sys.exit(f"[ERROR] Se reescribieron {k} stylers de {len(capas)} capas.")
    Path(a.out).write_text(salida, encoding="utf-8")
    print(f"Capas: {len(capas)} | polígonos: {n} | polígonos con datos reasignados: {cambian} | salida: {a.out}")

if __name__ == "__main__":
    main()
