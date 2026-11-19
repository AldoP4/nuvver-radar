---
name: radar
description: "Encuentra oportunidades de negocio que existen HOY, para una persona concreta, y dice cómo cobrarlas. Ancla la fecha real, busca señales de 'por qué ahora' (leyes con fecha, cambios de plataformas, quejas recurrentes, dinero que ya se gasta), las filtra con una rúbrica dura (¿alguien ya paga?, ¿llegas al comprador en 7 días?) y entrega el top 3 con comprador, precio, canal y una prueba de 7 días antes de construir. Úsala cuando alguien pregunte qué vender, qué construir, qué app o servicio hacer, qué oportunidades hay en su país o nicho, o quiera validar una idea antes de programarla."
argument-hint: 'radar dev en México con Claude Code, sin capital | radar nicho: escuelas privadas en Colombia | radar validar: checador por WhatsApp'
allowed-tools: Bash, Read, Write, WebSearch, WebFetch, AskUserQuestion
license: MIT
user-invocable: true
---

# /radar: oportunidades de hoy, para ti

Una idea no es una oportunidad. Una oportunidad es **alguien concreto que ya tiene el problema, ya gasta dinero o tiempo en él, al que puedes llegar esta semana, con una razón para que pase ahora.** Esta skill busca eso y no da por buena ninguna idea sin evidencia.

Habla en el idioma de la persona. Sé directo: primero la respuesta, después el detalle.

## Modos

| Lo que escribe | Qué haces |
|---|---|
| `/radar` sin nada | Paso 1 completo (preguntas de perfil) y luego todo el flujo |
| `/radar <perfil, país o nicho>` | Saca el perfil del texto, pregunta solo lo que falte y sigue |
| `/radar validar: <idea>` | Salta los pasos 2 y 3: investiga esa idea, califícala (paso 4) y arma su prueba de 7 días (paso 5) |

## Paso 0: el reloj (siempre, antes de buscar nada)

No sabes qué día es: tu idea del "hoy" viene de tus datos de entrenamiento y puede estar meses o años atrasada.

1. Corre el script `scripts/ahora.py` de la carpeta de esta skill (`python3 scripts/ahora.py`, o `python` en Windows). Si no hay Python, usa `date`.
2. Desde ahí, todo lo "reciente" se mide en días contra esa fecha. La ventana normal de señales es de **90 días**; los hechos de fondo (una ley, el precio de un competidor) pueden tener hasta 12 meses si sigues comprobando que están vigentes.
3. Cada vez que encuentres una fecha límite (una ley que entra en vigor, un cambio de precios), calcula cuánto falta con `python3 scripts/ahora.py --hasta AAAA-MM-DD`. Una fecha que ya pasó no es "por qué ahora": es el pasado.
4. Escribe la fecha de hoy al inicio del reporte.

## Paso 1: el perfil (qué ventaja tiene esta persona)

La misma oportunidad es buena para uno y mala para otro. Antes de buscar, junta esto (de lo que ya dijo o con **máximo 4 preguntas** en un solo AskUserQuestion):

- **Ventaja:** qué sabe hacer, qué ha hecho que funcionó, a quién conoce, idioma y país.
- **Recursos:** horas a la semana, dinero para invertir (puede ser cero) y cuánto aguanta sin ingresos.
- **Restricciones:** lo que no quiere o no puede hacer (salir a visitar, salir en cámara, hacer llamadas, atender clientes).
- **Meta:** cuánto quiere ganar al mes y en cuánto tiempo.

Si no contesta, supón lo razonable, dilo en una línea y sigue. Con poco tiempo de colchón, pesa más lo que cobra rápido (servicio) que lo que tarda en dar dinero (audiencia, producto).

## Paso 2: barrido de señales "por qué ahora"

Lee `references/fuentes.md` para las búsquedas de cada tipo. Busca **en el idioma y el país de la persona**, y en inglés solo para comprobar que en otro lado alguien ya cobra por algo parecido.

Los 7 tipos de señal:
1. **Regulación con fecha:** leyes, obligaciones fiscales o laborales, multas que empiezan a aplicarse.
2. **Cambio de plataforma:** una API que empieza a cobrar, un cambio de políticas, una función nueva (Meta, Google, Apple, bancos, gobierno).
3. **Capacidad nueva de IA:** algo que hace 6 meses salía caro o no se podía y hoy cuesta centavos.
4. **Queja recurrente:** la misma frase repetida en Reddit, grupos de Facebook, foros, reseñas de 1 a 3 estrellas y comentarios de YouTube.
5. **Dinero que ya se gasta:** competidores cobrando, ingresos verificados (TrustMRR, Indie Hackers, Acquire), anuncios activos de pago.
6. **Calendario:** temporadas, cierres fiscales, regreso a clases, eventos grandes.
7. **Hueco que se abre:** un producto que cierra, que sube de precio o que no existe en tu idioma.

Reglas:
- Haz **al menos 12 búsquedas**, en tandas en paralelo. Si una tanda sale floja, cambia las palabras, no la conclusión.
- Anota cada señal con: qué dice, link, fecha y **tipo de fuente** (primaria: gobierno, documentación oficial, datos verificados · medio de noticias · proveedor que vende la solución · opinión personal). Las fuentes de proveedores exageran: nunca bastan solas.
- Busca las palabras reales del comprador, no las del vendedor: "no me alcanza el tiempo para contestar" pesa más que "automatización de atención al cliente".

## Paso 3: candidatos

Escribe de **12 a 20 candidatos** con esta forma, sin adornos:

> Para **[comprador concreto]** que **[dolor, con sus palabras]**, porque **[por qué ahora, con fecha si la hay]**: **[lo que entregas]**.

Mezcla tres formatos: **servicio hecho por ti** (cobra en días), **producto chico** (app, plantilla, skill o micro-SaaS) y **contenido o comunidad** (tarda meses pero escala). Para generar candidatos usa los ángulos de `references/metodologias.md`: localizar algo que funciona en otro idioma, desempacar una herramienta grande, vender picos y palas, convertir un servicio en producto y "lo aburrido que nadie quiere hacer".

## Paso 4: el filtro

Califica cada candidato con la rúbrica de `references/rubrica.md` (7 criterios del 1 al 5, con pesos) y aplica las **reglas de descarte** antes de sumar. Luego:

- **Abogado del diablo:** para los 5 de arriba, escribe en una línea la razón más fuerte por la que fracasaría.
- **Pre-mortem:** "pasaron 60 días y no se vendió nada: ¿por qué?". Si la respuesta es obvia y no tiene arreglo, baja ese candidato.
- Separa siempre **"hay demanda en general"** de **"le van a comprar a esta persona"**. Lo segundo depende de su llegada y su confianza, no del mercado.

## Paso 5: el top 3, a fondo

Para cada uno de los 3 mejores entrega:

1. **El comprador:** quién es, en qué lugar se junta (grupos, búsquedas, directorios, eventos) y una **frase real suya** con link.
2. **La competencia:** quién ya lo hace, cuánto cobra (con fuente) y el hueco que deja.
3. **Precio y escalera:** gratis (anzuelo) → algo barato (primer sí) → lo caro (servicio o plan). Los precios propuestos se marcan como propuesta, no como dato.
4. **Confianza:** qué necesita ese comprador para pagarle a un desconocido (cara real, factura, garantía, demo con sus datos, no pedir contraseñas) y cuánta confianza tiene hoy la persona.
5. **Llegada:** cómo llega al primer comprador **en 7 días desde su computadora** y, si hace falta, una sola acción fuera de casa. Respeta las restricciones del paso 1.
6. **Prueba de 7 días:** con `references/prueba-7-dias.md`, qué se enseña, a cuántos, qué se pregunta, y el número que dice sí, ajusta o suelta.
7. **Primer contenido:** una publicación que pueda hacer hoy y que a la vez sirva de prueba.

## Paso 6: el reporte

1. Guarda el reporte completo con `references/plantilla-reporte.md` como `radar-AAAA-MM-DD.md` en la carpeta actual (o donde la persona diga).
2. En el chat, devuelve solo esto: la fecha de hoy, el top 3 en una tabla (oportunidad, comprador, por qué ahora, primer paso), **la única acción que la persona debe hacer hoy** y la ruta del reporte.

## Reglas que no se rompen

- **Nada inventado.** Cada cifra lleva su link. Lo que no encuentres se escribe como "no encontré dato" y no se rellena.
- Los estimados y precios propuestos se marcan como tales.
- Nunca prometas ingresos. Habla de señales y de pruebas.
- Si la evidencia es floja, dilo con todas sus letras. Un "no encontré oportunidad clara para tu perfil, y esto es lo que probaría" vale más que un top 3 inflado.
- No recomiendes nada ilegal, que engañe al comprador o que dependa de saltarse las reglas de una plataforma.
