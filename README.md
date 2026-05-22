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

## Casos de prueba

| ID | Regla | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo |
|----|-------|-------------|--------------|-----------------|-------|--------------------|------|
| TC-01 | R1 | Crear producto con precio válido | Ninguna | nombre="Libro", precio=50000 | Instanciar Producto | Producto creado con precio 50000 | Positivo |
| TC-02 | R1 | Crear producto con precio cero | Ninguna | nombre="Libro", precio=0 | Instanciar Producto | ValueError: precio debe ser mayor que cero | Negativo |
| TC-03 | R1 | Crear producto con precio negativo | Ninguna | nombre="Libro", precio=-100 | Instanciar Producto | ValueError: precio debe ser mayor que cero | Negativo |
| TC-04 | R2 | Aplicar descuento válido del 20% | Producto con precio 10000 | descuento=20 | Llamar aplicar_descuento(20) | Descuento aplicado, precio con descuento = 8000 | Positivo |
| TC-05 | R2 | Aplicar descuento en límite inferior 0% | Producto con precio 10000 | descuento=0 | Llamar aplicar_descuento(0) | Descuento aplicado, precio con descuento = 10000 | Borde |
| TC-06 | R2 | Aplicar descuento en límite superior 40% | Producto con precio 10000 | descuento=40 | Llamar aplicar_descuento(40) | Descuento aplicado, precio con descuento = 6000 | Borde |
| TC-07 | R2 | Aplicar descuento mayor al 40% | Producto con precio 10000 | descuento=41 | Llamar aplicar_descuento(41) | ValueError: descuento no puede superar el 40% | Negativo |
| TC-08 | R3 | Calcular precio final con IVA | Producto con precio 10000, descuento 20% | ninguno | Llamar calcular_precio_final() | 10000 * 0.80 * 1.19 = 9520.0 | Positivo |
| TC-09 | R3 | Precio final con descuento 0% incluye solo IVA | Producto con precio 10000, descuento 0% | ninguno | Llamar calcular_precio_final() | 10000 * 1.19 = 11900.0 | Borde |
| TC-10 | R2 | Aplicar descuento negativo | Producto con precio 10000 | descuento=-5 | Llamar aplicar_descuento(-5) | ValueError: descuento no puede ser negativo | Negativo |