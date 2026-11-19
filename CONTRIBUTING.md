# Contribuir a /radar

Gracias por ayudar. Lo que más sirve, en orden:

1. **Resultados reales.** Usaste /radar, hiciste la prueba de 7 días y funcionó o no: abre un issue con el perfil, la oportunidad, qué hiciste y qué pasó. Con eso se ajusta la rúbrica.
2. **Fuentes de tu país.** Organismos, diarios oficiales, directorios o comunidades donde se juntan los compradores. Agrégalas a `skills/radar/references/fuentes.md`.
3. **Metodologías.** Si un método que usas en la práctica falta, agrégalo a `metodologias.md` con de dónde viene y cómo se aplica.
4. **Errores del reloj** (`scripts/ahora.py`): zonas horarias, formatos, días hábiles.

Antes del PR corre:

```
python tests/validar_repo.py
```

Reglas: nada de cifras sin fuente, y nada que prometa ingresos.
