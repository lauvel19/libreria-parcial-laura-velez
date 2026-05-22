## SM-1
**Respuesta: C**

Desarrollo tradicional con pruebas al final. El problema es que los defectos se detectan tarde, cuando corregirlos cuesta hasta 100 veces más que si se hubieran encontrado en etapas tempranas.

A y B son incorrectas porque Shift-left testing es lo contrario porque busca adelantar las pruebas lo más posible en el ciclo y se refiere a probar en producción con usuarios reales no describe este escenario. D es incorrecta porque la integración continua implica automatización y despliegues frecuente no describe un equipo que prueba solo al final

---

## SM-2
**Respuesta: B**

La primera regla de Uncle Bob: no escribir código de producción sin que exista primero un test que falle. El código fue escrito antes de que ningún test lo requiriera.

A es incorrecta porque el refactor es el tercer paso del ciclo, no tiene relación con escribir tests después del código, C es incorrecta la regla del Green sí pide código mínimo, pero la violación principal ocurre antes: nunca hubo un RED, D es incorrecta TDD es estricto en el orden Red → Green → Refactor. No existe una variante que permita escribir el código primero

---

## PA-1

En el paso GREEN de TDD, el objetivo no es escribir código bonito sino hacer pasar el test que falló en el RED de la forma más rápida y sencilla posible, se obliga a hacer esto porque si se escribe código limpio y completo desde el inicio, se empieza a anticipar casos que todavía no tienen un test que los respalde, rompiendo el ciclo. El código "feo" del GREEN es intencional porque confirma que el test controla el diseño y no al revés, si alguien aprovecha el GREEN para escribir código complejo, pierde la trazabilidad entre cada test y cada decisión de diseño, y el REFACTOR deja de tener sentido porque ya se mezcló todo

---

## PA-2

TDD y BDD resuelven problemas distintos aunque trabajan juntos, TDD está dirigido al desarrollador y su problema es el diseño interno que obliga a pensar en cómo debe comportarse el código antes de escribirlo, usando tests técnicos como guía, BDD está dirigido a todo el equipo incluyendo producto y cliente, y su problema es la comunicación porque asegura que todos entienden lo mismo sobre cómo debe comportarse el sistema, usando lenguaje natural que es Gherkin en lugar de código, TDD responde: está bien construido por dentro? y BDD responde estamos construyendo lo correcto, se complementan porque los escenarios BDD escritos con el cliente se convierten en la especificación que guía los ciclos TDD del desarrollador, la idea de reemplazar uno con el otro dejaría un vacío sin TDD el código interno puede ser caótico aunque los escenarios pasen, y sin BDD el equipo técnico puede construir algo perfecto que nadie pidió

---

## PA-3

Tener 95% de cobertura significa que el 95% de las líneas fueron ejecutadas durante las pruebas, pero no dice nada sobre si las verificaciones son correctas, un test puede ejecutar una línea sin hacer ningún assert útil sobre su resultado.

**Ejemplo concreto:** Supón que tenemos esta función:

```python
def dividir(a, b):
    return a / b
```

Un test así da cobertura del 100%:

```python
def test_dividir():
    dividir(10, 2)  
```

La función nunca fue verificada, asi que si alguien cambia el operador a `*`, el test sigue pasando, además, el caso `dividir(10, 0)` nunca se probó y lanzaría una excepción en producción. Alta cobertura sin asserts significativos es una falsa sensación de seguridad.

---

## PA-4

Probar solo el 20% es insuficiente porque ese valor está en el centro del rango válido y no revela nada sobre los bordes donde suelen ocurrir los errores, la lógica "si funciona con uno funciona con todos" ignora que los defectos se concentran en los límites y en los valores justo fuera del rango

Los valores concretos que yo probaría para la Regla 2 son:

- **0%** — límite inferior válido, debe aceptarse
- **40%** — límite superior válido, debe aceptarse
- **-1%** — justo fuera del rango por abajo, debe rechazarse
- **41%** — justo fuera del rango por arriba, debe rechazarse
- **20%** — valor representativo del interior, debe aceptarse
- **100%** — valor claramente inválido, debe rechazarse

Estos valores siguen la técnica de análisis de valores límite, que prueba los bordes exactos y sus vecinos inmediatos porque ahí es donde los errores de condición (`<` vs `<=`) se hacen visibles.

---

## PA-5

TDD y BDD producen una suite de tests automatizados que es exactamente lo que necesita un pipeline de CI/CD para funcionar, cuando el equipo hace push, el pipeline ejecuta todos los tests y decide si el código puede avanzar a la siguiente etapa, sin esa suite, el pipeline no tiene forma de saber si el nuevo código rompe algo, así que básicamente se convierte en un sistema de despliegue automático sin ninguna red de seguridad, el equipo estaría entregando a producción sin verificación, que es peor que no tener CI/CD porque da una falsa confianza de automatización, TDD garantiza que cada unidad funciona aislada, BDD garantiza que el comportamiento del sistema es el esperado por el negocio, y CI/CD es el mecanismo que ejecuta todo eso en cada cambio, por lo tanto, los tres juntos forman el ciclo de calidad continua

