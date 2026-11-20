# Rúbrica del radar

## Primero, las reglas de descarte

Un candidato queda fuera, sin sumar puntos, si cumple cualquiera de estas:

1. **Nadie paga en ningún lado** por algo parecido y no hay una razón fuerte de por qué (por ejemplo, una ley que lo hace obligatorio desde ya).
2. **No hay forma de llegar al comprador en 7 días** con las restricciones de la persona.
3. **Es ilegal, engaña al comprador** o depende de saltarse las reglas de una plataforma.
4. **El "por qué ahora" ya pasó** (la fecha límite es del pasado) o es solo "la IA está de moda".

Hay una quinta que no descarta pero pone bandera roja: **pide más confianza de la que la persona tiene hoy**. Por ejemplo, pedir contraseñas del banco o del SAT siendo un desconocido. Se queda solo si la oferta resuelve esa confianza (garantía, que los datos no salgan de la computadora del cliente, una demo con sus datos).

## Después, los 7 criterios (del 1 al 5)

| Criterio | Peso | 1 | 3 | 5 |
|---|---|---|---|---|
| **Ya pagan** | ×3 | No encontré a nadie cobrando | Hay competidores pero sin precios ni ingresos visibles | Precios públicos o ingresos verificados de varios competidores |
| **Llegada** | ×3 | No sé dónde está el comprador | Sé dónde está, pero llegar cuesta mucho (frío, anuncios) | Lo puedo encontrar y escribirle hoy (grupo, directorio, contacto, búsqueda) |
| **Dolor** | ×2 | Molestia ocasional | Le quita horas cada semana | Le cuesta dinero, clientes o una multa, y lo dice con sus palabras |
| **Por qué ahora** | ×2 | La demanda está bajando o nada la sostiene | Demanda constante, o una tendencia sin fecha | Hay una fecha concreta en los próximos 3 meses |
| **Ajuste** | ×2 | La persona no sabe hacerlo | Puede aprenderlo en unas semanas | Ya lo ha hecho o es su fuerte |
| **Velocidad a primer cobro** | ×2 | Meses | Semanas | Días: se puede vender antes de construir |
| **Confianza requerida** (al revés: menos es mejor) | ×1 | Necesita marca, historial y contrato | Necesita demo y factura | Se compra en un clic o con una garantía |

Una fecha que **ya pasó** (compárala con `ahora.py`) vale como máximo 2 en "Por qué ahora": el cambio ya ocurrió y quien iba a moverse ya se movió.

**Máximo: 75 puntos** (15 × 5). Como guía:
- **60 o más:** vale la prueba de 7 días ya.
- **45 a 59:** prometedora; falta una pieza (normalmente llegada o evidencia de pago).
- **Menos de 45:** se guarda en la lista, no se trabaja.

Escribe la tabla con la calificación de cada criterio y **una línea de evidencia** por calificación alta. Un 5 sin link no vale 5.

**Para entrar al top 3:** al menos 3 en "Ya pagan", además de no tener descarte. Si quedan menos de 3 candidatos que cumplan, el top tiene menos de 3 y se dice por qué.

## Ajustes por perfil

Los pesos no cambian nunca, para que el máximo siga siendo 75 y los cortes sirvan. Los ajustes cambian cómo se califica y cómo se desempata:

- **Con menos de 3 meses de colchón:** en empate gana el de más velocidad, y en la duda se elige el servicio sobre el producto.
- **Restricciones de la persona** (no visitar, no hacer llamadas, no salir en cámara, no atender clientes): todo canal de llegada que dependa de algo que la persona excluyó vale 1 en "Llegada". Si la única forma de llegar al comprador es esa, el candidato cae por la regla de descarte 2.
- **Sin dinero para invertir:** vale 1 en "Llegada" todo lo que dependa de anuncios pagados.
