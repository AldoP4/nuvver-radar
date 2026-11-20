#!/usr/bin/env python3
"""Reloj del radar: le dice al agente qué día es HOY y cuánto falta para cada fecha.

Los modelos de lenguaje no saben qué día es: suponen el año de sus datos de
entrenamiento. Este script ancla el "hoy" con el reloj de la computadora.

Uso:
    python ahora.py                      # hoy, semana, cierres de mes, trimestre y año
    python ahora.py --hasta 2027-01-01   # días que faltan para una o varias fechas
    python ahora.py --json               # lo mismo, en JSON
    python ahora.py --utc -3             # con la zona horaria de la persona (aquí, Argentina)

Solo usa la biblioteca estándar de Python 3.8+.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timedelta, timezone

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
         "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def fecha_larga(d: date) -> str:
    return f"{DIAS[d.weekday()]} {d.day} de {MESES[d.month - 1]} de {d.year}"


def fin_de_mes(d: date) -> date:
    siguiente = date(d.year + (d.month == 12), d.month % 12 + 1, 1)
    return siguiente - timedelta(days=1)


def fin_de_trimestre(d: date) -> date:
    mes_fin = ((d.month - 1) // 3 + 1) * 3
    return fin_de_mes(date(d.year, mes_fin, 1))


def dias_habiles(desde: date, hasta: date) -> int:
    """Días de lunes a viernes entre dos fechas (sin contar 'desde')."""
    if hasta <= desde:
        return 0
    total, d = 0, desde
    while d < hasta:
        d += timedelta(days=1)
        if d.weekday() < 5:
            total += 1
    return total


def describir(hoy: date, objetivo: date) -> dict:
    dias = (objetivo - hoy).days
    if dias > 0:
        texto = f"faltan {dias} días ({dias_habiles(hoy, objetivo)} hábiles, ~{dias / 7:.1f} semanas)"
    elif dias == 0:
        texto = "es hoy"
    else:
        texto = f"ya pasó hace {-dias} días"
    return {"fecha": objetivo.isoformat(), "dia": fecha_larga(objetivo), "dias": dias, "texto": texto}


def main() -> int:
    p = argparse.ArgumentParser(description="Ancla el 'hoy' para un agente de IA.")
    p.add_argument("--hasta", nargs="*", default=[], metavar="AAAA-MM-DD",
                   help="fechas para calcular cuánto falta")
    p.add_argument("--json", action="store_true", help="salida en JSON")
    p.add_argument("--utc", type=float, default=None, metavar="HORAS",
                   help="diferencia con UTC de la persona (ej. -3 para Argentina); por defecto, la de esta computadora")
    a = p.parse_args()
    try:  # consolas de Windows que no usan UTF-8
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

    if a.utc is not None:
        ahora = datetime.now(timezone(timedelta(hours=a.utc)))
    else:
        ahora = datetime.now().astimezone()
    hoy = ahora.date()
    iso = hoy.isocalendar()
    datos = {
        "hoy": hoy.isoformat(),
        "hoy_texto": fecha_larga(hoy),
        "hora_local": ahora.strftime("%H:%M"),
        "zona_utc": ahora.strftime("%z"),
        "semana_iso": iso[1],
        "ventana_90_dias_desde": (hoy - timedelta(days=90)).isoformat(),
        "fin_de_mes": describir(hoy, fin_de_mes(hoy)),
        "fin_de_trimestre": describir(hoy, fin_de_trimestre(hoy)),
        "fin_de_año": describir(hoy, date(hoy.year, 12, 31)),
        "fechas": [],
    }
    for f in a.hasta:
        try:
            datos["fechas"].append(describir(hoy, date.fromisoformat(f)))
        except ValueError:
            print(f"Fecha inválida: {f} (usa AAAA-MM-DD)", file=sys.stderr)
            return 2

    if a.json:
        print(json.dumps(datos, ensure_ascii=False, indent=2))
        return 0

    print(f"HOY: {datos['hoy_texto']} ({datos['hoy']}), {datos['hora_local']} hora local (UTC{datos['zona_utc']})")
    print(f"Semana {datos['semana_iso']} del año. Ventana de 90 días: desde {datos['ventana_90_dias_desde']}.")
    print(f"Fin de mes: {datos['fin_de_mes']['texto']}.")
    print(f"Fin de trimestre: {datos['fin_de_trimestre']['texto']}.")
    print(f"Fin de año: {datos['fin_de_año']['texto']}.")
    for f in datos["fechas"]:
        print(f"{f['fecha']} ({f['dia']}): {f['texto']}.")
    print("Regla: todo lo que digas de 'hoy', 'reciente' o 'el año pasado' se calcula desde esta fecha, no desde tus datos de entrenamiento.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
