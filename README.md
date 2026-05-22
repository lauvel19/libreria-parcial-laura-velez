# Librería del Centro — Módulo de Precios
**Parcial 1 | Pruebas de Software | Laura Vélez | Ing. Software | Quinto Semestre**

---

## Análisis previo al código

### Regla 1 — Particiones de equivalencia: Precio base

- **Precio mayor que cero** (Válida) → valor representativo: 50000 → Producto creado correctamente
- **Precio igual a cero** (Inválida) → valor representativo: 0 → Error: "El precio base debe ser mayor que cero"
- **Precio negativo** (Inválida) → valor representativo: -100 → Error: "El precio base debe ser mayor que cero"

---

### Regla 2 — Particiones de equivalencia: Descuento

- **Descuento entre 0% y 40%** (Válida) → valor representativo: 20 → Descuento aplicado correctamente
- **Descuento igual a 0%** (Válida) → valor representativo: 0 → Precio sin descuento
- **Descuento igual a 40%** (Válida) → valor representativo: 40 → Descuento máximo aplicado
- **Descuento mayor a 40%** (Inválida) → valor representativo: 50 → Error: "El descuento no puede superar el 40%"
- **Descuento negativo** (Inválida) → valor representativo: -5 → Error: "El descuento no puede ser negativo"

---

### Regla 2 — Análisis de valores límite: rango 0%–40%

- **-1%** → Fuera del límite inferior → Rechazado
- **0%** → Límite inferior exacto → Aceptado
- **1%** → Justo dentro del límite inferior → Aceptado
- **39%** → Justo dentro del límite superior → Aceptado
- **40%** → Límite superior exacto → Aceptado
- **41%** → Fuera del límite superior → Rechazado

---

### Regla 3 — Pregunta al administrador

**Pregunta:** Si el precio base es muy pequeño y el descuento es 0%, ¿el precio final con IVA puede tener decimales, o debe redondearse a un valor entero?

**Justificación:** La fórmula `precio_final = precio_base * (1 - descuento/100) * 1.19` puede producir valores con muchos decimales dependiendo del precio base, y sin saber si se redondea (y cómo) no es posible definir el resultado esperado exacto en los tests.

---

## Casos de prueba

- **TC-01** | R1 | Crear producto con precio válido | Sin precondición | nombre="Libro", precio=50000 | Instanciar Producto | Producto creado con precio 50000 | Positivo
- **TC-02** | R1 | Crear producto con precio cero | Sin precondición | nombre="Libro", precio=0 | Instanciar Producto | ValueError: precio debe ser mayor que cero | Negativo
- **TC-03** | R1 | Crear producto con precio negativo | Sin precondición | nombre="Libro", precio=-100 | Instanciar Producto | ValueError: precio debe ser mayor que cero | Negativo
- **TC-04** | R2 | Aplicar descuento válido del 20% | Producto con precio 10000 | descuento=20 | Llamar aplicar_descuento(20) | Descuento aplicado, precio con descuento = 8000 | Positivo
- **TC-05** | R2 | Descuento en límite inferior 0% | Producto con precio 10000 | descuento=0 | Llamar aplicar_descuento(0) | Precio con descuento = 10000 | Borde
- **TC-06** | R2 | Descuento en límite superior 40% | Producto con precio 10000 | descuento=40 | Llamar aplicar_descuento(40) | Precio con descuento = 6000 | Borde
- **TC-07** | R2 | Descuento mayor al 40% | Producto con precio 10000 | descuento=41 | Llamar aplicar_descuento(41) | ValueError: descuento no puede superar el 40% | Negativo
- **TC-08** | R3 | Precio final con IVA y descuento 20% | Producto con precio 10000, descuento 20% | — | Llamar calcular_precio_final() | 9520.0 | Positivo
- **TC-09** | R3 | Precio final sin descuento incluye solo IVA | Producto con precio 10000, descuento 0% | — | Llamar calcular_precio_final() | 11900.0 | Borde
- **TC-10** | R2 | Descuento negativo rechazado | Producto con precio 10000 | descuento=-5 | Llamar aplicar_descuento(-5) | ValueError: descuento no puede ser negativo | Negativo

---

## Reporte de cobertura


C:\Users\laura\OneDrive\Documentos\Universidad\5to semestre\uni\pruebas\parcial 1>python -m pytest tests/ --cov=src --cov-report=term-missing
============================================================================== test session starts ==============================================================================
platform win32 -- Python 3.14.0, pytest-8.3.5, pluggy-1.6.0
rootdir: C:\Users\laura\OneDrive\Documentos\Universidad\5to semestre\uni\pruebas\parcial 1
plugins: bdd-8.1.0, cov-6.1.0
collected 11 items                                                                                                                                                               

tests\test_producto.py ...........                                                                                                                                         [100%]

================================================================================ tests coverage =================================================================================
________________________________________________________________ coverage: platform win32, python 3.14.0-final-0 ________________________________________________________________

Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
src\__init__.py       0      0   100%
src\producto.py      22      0   100%
-----------------------------------------------
TOTAL                22      0   100%
============================================================================== 11 passed in 0.14s ===============================================================================

