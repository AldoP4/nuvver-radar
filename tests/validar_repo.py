#!/usr/bin/env python3
"""Revisa que el repo esté sano: manifiestos, frontmatter de la skill, referencias y el reloj."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SKILL = RAIZ / "skills" / "radar"
errores: list[str] = []


def revisar(condicion: bool, mensaje: str) -> None:
    if not condicion:
        errores.append(mensaje)


# Manifiestos
for nombre in ("plugin.json", "marketplace.json"):
    ruta = RAIZ / ".claude-plugin" / nombre
    try:
        datos = json.loads(ruta.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        errores.append(f"{nombre}: JSON inválido ({e})")
        continue
    revisar(bool(datos.get("name")), f"{nombre}: falta 'name'")

plugin = json.loads((RAIZ / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
market = json.loads((RAIZ / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
revisar(market["plugins"][0]["name"] == plugin["name"], "el plugin del marketplace no coincide con plugin.json")
revisar(market["plugins"][0]["version"] == plugin["version"], "las versiones de plugin.json y marketplace.json no coinciden")

# Frontmatter de la skill
texto = (SKILL / "SKILL.md").read_text(encoding="utf-8")
m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
revisar(m is not None, "SKILL.md: falta el frontmatter")
if m:
    fm = m.group(1)
    revisar(re.search(r"^name: radar$", fm, re.M) is not None, "SKILL.md: 'name' debe ser radar")
    desc = re.search(r"^description: (.+)$", fm, re.M)
    revisar(desc is not None, "SKILL.md: falta 'description'")
    if desc:
        revisar(len(desc.group(1)) <= 1024, "SKILL.md: la descripción pasa de 1024 caracteres")

# Cada referencia mencionada existe
for ref in set(re.findall(r"`(references/[\w\-]+\.md|scripts/[\w\-]+\.py)`", texto)):
    revisar((SKILL / ref).exists(), f"SKILL.md menciona {ref}, pero no existe")

# El reloj corre
salida = subprocess.run([sys.executable, str(SKILL / "scripts" / "ahora.py"), "--json", "--hasta", "2030-01-01"],
                        capture_output=True, text=True, encoding="utf-8")
revisar(salida.returncode == 0, f"ahora.py falló: {salida.stderr.strip()}")
if salida.returncode == 0:
    datos = json.loads(salida.stdout)
    revisar(len(datos["fechas"]) == 1, "ahora.py no calculó la fecha pedida")

if errores:
    print("FALLÓ:")
    for e in errores:
        print(f"  - {e}")
    sys.exit(1)
print("OK: manifiestos, skill, referencias y reloj en orden.")
