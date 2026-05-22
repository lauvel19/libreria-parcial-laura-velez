# Librería del Centro — Módulo de Precios
**Parcial 1 | Pruebas de Software | Laura Vélez | Ing. Software | Quinto Semestre**

---

## Análisis previo al código

### Regla 1 — Particiones de equivalencia: Precio base

| Partición | Tipo | Valor representativo | Resultado esperado |
|-----------|------|---------------------|-------------------|
| Precio mayor que cero | Válida | 50000 | Producto creado correctamente |
| Precio igual a cero | Inválida | 0 | Error: "El precio base debe ser mayor que cero" |
| Precio negativo | Inválida | -100 | Error: "El precio base debe ser mayor que cero" |

---

### Regla 2 — Particiones de equivalencia: Descuento

| Partición | Tipo | Valor representativo | Resultado esperado |
|-----------|------|---------------------|-------------------|
| Descuento entre 0% y 40% | Válida | 20 | Descuento aplicado correctamente |
| Descuento igual a 0% | Válida | 0 | Precio sin descuento |
| Descuento igual a 40% | Válida | 40 | Descuento máximo aplicado |
| Descuento mayor a 40% | Inválida | 50 | Error: "El descuento no puede superar el 40%" |
| Descuento negativo | Inválida | -5 | Error: "El descuento no puede ser negativo" |

---

### Regla 2 — Análisis de valores límite: rango 0%–40%

| Valor | Tipo | Resultado esperado |
|-------|------|--------------------|
| -1% | Fuera del límite inferior | Rechazado |
| 0% | Límite inferior exacto | Aceptado |
| 1% | Justo dentro del límite inferior | Aceptado |
| 39% | Justo dentro del límite superior | Aceptado |
| 40% | Límite superior exacto | Aceptado |
| 41% | Fuera del límite superior | Rechazado |

---

### Regla 3 — Pregunta al administrador

**Pregunta:** Si el precio base es muy pequeño y el descuento es 0%, ¿el precio final con IVA puede tener decimales, o debe redondearse a un valor entero?

**Justificación:** La fórmula `precio_final = precio_base * (1 - descuento/100) * 1.19` puede producir valores con muchos decimales dependiendo del precio base, y sin saber si se redondea (y cómo) no es posible definir el resultado esperado exacto en los tests.

---
