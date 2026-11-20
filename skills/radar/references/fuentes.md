# Dónde buscar cada señal

Plantillas de búsqueda. Cambia `[país]`, `[nicho]`, `[año]` y `[mes]` por los valores reales (el año y el mes salen de `scripts/ahora.py`, nunca de memoria). Busca en el idioma de la persona y agrega el nombre del país o la moneda para no traer resultados de otro lado.

## 1. Regulación con fecha
- `nueva obligación [año] [país] empresas multa`
- `entra en vigor [mes] [año] [país] pymes`
- `reforma [laboral | fiscal] [año] [país] qué cambia empresas`
- `[organismo: SAT, SUNAT, DIAN, AFIP/ARCA, SII, STPS] obligatorio [año] contribuyentes`
- Comprueba en la fuente primaria (diario oficial, portal del gobierno) antes de decir la fecha o el monto de la multa.

## 2. Cambio de plataforma
- `[WhatsApp | Meta | Google | Apple | Shopify | Mercado Libre] cambia precios [año]`
- `[plataforma] API nuevas reglas [mes] [año]`
- `[plataforma] deja de ser gratis`
- Documentación oficial y changelogs: valen más que cualquier blog.

## 3. Capacidad nueva de IA
- `[tarea manual] con IA [año] costo`
- `agente de IA que [tarea] para [nicho]`
- Pregunta: ¿qué costaba un empleado o una agencia y hoy se hace con centavos por corrida?

## 4. Queja recurrente (las palabras del comprador)
- `site:reddit.com [nicho] "hate" OR "nightmare" OR "spreadsheet" OR "manual"` (en inglés)
- `"[nicho]" "no me da tiempo" OR "todo en Excel" OR "a mano" OR "alguien que me ayude"`
- `[software que usan] reseñas 2 estrellas` o páginas de Capterra, G2 o Google Maps con quejas
- Grupos de Facebook y foros del nicho: su buscador interno con las mismas frases (el agente no siempre puede entrar; si no puede, pide a la persona que pegue lo que vea).
- Comentarios de videos de YouTube del nicho: ahí la gente cuenta su problema con sus palabras.

## 5. Dinero que ya se gasta
- `[tipo de herramienta] precios [país]` y `alternativas a [competidor]`
- `site:trustmrr.com [tema]` (ingresos verificados con Stripe)
- `site:indiehackers.com [tema] revenue` y anuncios en `acquire.com`
- `[tipo de servicio] cuánto cobra [país]`, y perfiles de freelancers que ya venden eso
- Anuncios activos: la Biblioteca de Anuncios de Meta muestra quién paga por anunciar algo. Si alguien paga anuncios hace meses, le funciona. El agente no la puede consultar solo: pídele a la persona que la revise.

## 6. Calendario
- `temporada [nicho] [país] [mes]`, cierres fiscales, regreso a clases, Buen Fin, Hot Sale, fin de año, eventos deportivos.
- Calcula con `ahora.py --hasta` cuántas semanas quedan antes del pico.

## 7. Hueco que se abre
- `[producto] cierra` / `[producto] sube precio` / `[producto] alternativa en español`
- Productos con mucha tracción en inglés (GitHub trending, Product Hunt, TrustMRR) que no tienen versión para tu país o idioma.

## Cómo calificar una fuente
| Tipo | Ejemplos | Peso |
|---|---|---|
| Primaria | Diario oficial, documentación de la plataforma, datos verificados (TrustMRR con Stripe), precios en la página del competidor | Alto |
| Medio | Periódicos, revistas de negocios | Medio: verifica la fecha |
| Proveedor | Blog de quien vende la solución | Bajo: exagera; nunca basta solo |
| Opinión | Un post, un hilo, un comentario | Bajo solo; alto si se repite mucho con las mismas palabras |
