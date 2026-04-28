---
title: Práctica 7
layout: practice
permalink: /practice/7
---
# Soluciones TP7 - Estructuras de Datos

Este archivo contiene las soluciones de referencia para todos los ejercicios del TP7.

Los ejercicios están agrupados en 3 archivos según la estructura de datos que usan:

- `exercise_tuples.py` — ejercicios 1 a 7 (tuplas)
- `exercise_sets.py` — ejercicios 8 a 12 (sets)
- `exercise_dicts.py` — ejercicios 13 a 23 (diccionarios)

---

## Parte 1 — Tuplas (`exercise_tuples.py`)

### Ejercicio 1 — `get_coordinate`

**Objetivo:** Extraer la coordenada de una tupla `(tesoro, coordenada)`.

**Solución:**
```python
def get_coordinate(registro):
    return registro[1]
```

**Conceptos:**
- Acceso por índice a una tupla (igual que en listas).
- El índice `1` es el segundo elemento.

---

### Ejercicio 2 — `convert_coordinate`

**Objetivo:** Convertir `"2A"` en `("2", "A")`.

**Solución:**
```python
def convert_coordinate(coordenada):
    return tuple(coordenada)
```

**Conceptos:**
- `tuple(string)` construye una tupla con cada carácter como elemento.
- Para `"2A"` genera `("2", "A")`.

**Alternativa por índices:**
```python
def convert_coordinate(coordenada):
    return (coordenada[0], coordenada[1])
```

---

### Ejercicio 3 — `create_record`

**Objetivo:** Combinar registros si las coordenadas coinciden.

**Solución:**
```python
def create_record(registro_azara, registro_rui):
    coord_azara = convert_coordinate(get_coordinate(registro_azara))
    coord_rui = get_coordinate(registro_rui)

    if coord_azara == coord_rui:
        return registro_azara + registro_rui
    return "not a match"
```

**Conceptos:**
- Reutilización de funciones previas (están en el mismo archivo).
- Concatenación de tuplas con `+` (genera una tupla más larga).
- Retorno temprano con `return "not a match"`.

**Explicación de la concatenación:**
```python
('Brass Spyglass', '4B') + ('Abandoned Lighthouse', ('4', 'B'), 'Blue')
# → ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')
```

---

### Ejercicio 4 — `sum_tuple`

**Objetivo:** Sumar los elementos de una tupla recorriéndola.

**Solución:**
```python
def sum_tuple(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total
```

**Conceptos:**
- Patrón **acumulador**: inicializar una variable en 0 y sumarle en cada iteración.
- El `for` sobre una tupla vacía no ejecuta ninguna iteración, así que `total` queda en 0.

**Versión con `while`:**
```python
def sum_tuple(numeros):
    total = 0
    i = 0
    while i < len(numeros):
        total += numeros[i]
        i += 1
    return total
```

---

### Ejercicio 5 — `count_occurrences`

**Objetivo:** Contar apariciones de un elemento.

**Solución:**
```python
def count_occurrences(tupla, elemento):
    contador = 0
    for item in tupla:
        if item == elemento:
            contador += 1
    return contador
```

**Conceptos:**
- Acumulador con condición: solo incrementa cuando se cumple `item == elemento`.
- Funciona con cualquier tipo comparable (números, strings, etc).

---

### Ejercicio 6 — `find_index`

**Objetivo:** Encontrar el índice de la primera aparición.

**Solución:**
```python
def find_index(tupla, elemento):
    for i, item in enumerate(tupla):
        if item == elemento:
            return i
    return -1
```

**Conceptos:**
- `enumerate` devuelve pares `(indice, valor)`.
- **Retorno temprano** con `return i`: corta el loop en cuanto lo encuentra.
- Si termina el loop sin retornar, significa que no se encontró → retornar `-1`.

**Versión con `while` (útil cuando se usa el índice explícitamente):**
```python
def find_index(tupla, elemento):
    i = 0
    while i < len(tupla):
        if tupla[i] == elemento:
            return i
        i += 1
    return -1
```

---

### Ejercicio 7 — `filter_positives`

**Objetivo:** Construir una nueva tupla filtrando.

**Solución:**
```python
def filter_positives(numeros):
    resultado = []
    for numero in numeros:
        if numero > 0:
            resultado.append(numero)
    return tuple(resultado)
```

**Conceptos:**
- Usamos una **lista auxiliar** porque las tuplas son inmutables (no se pueden modificar).
- `tuple(lista)` convierte al formato pedido.
- El 0 queda afuera porque no cumple `> 0`.

**Alternativa con tuple comprehension (no existe, pero sí generator):**
```python
def filter_positives(numeros):
    return tuple(n for n in numeros if n > 0)
```

---

## Parte 2 — Sets (`exercise_sets.py`)

### Ejercicio 8 — `clean_ingredients`

**Objetivo:** Eliminar ingredientes duplicados usando un set.

**Solución:**
```python
def clean_ingredients(nombre_plato, ingredientes):
    return (nombre_plato, set(ingredientes))
```

**Conceptos:**
- `set(lista)` elimina duplicados automáticamente.
- Los sets no tienen orden (no garantizan orden de iteración).
- Retornar tupla con `(nombre, set_limpio)`.

---

### Ejercicio 9 — `check_drinks`

**Objetivo:** Detectar si una bebida contiene alcohol.

**Solución:**
```python
def check_drinks(nombre_bebida, ingredientes):
    for ingrediente in ingredientes:
        if ingrediente in ALCOHOLS:
            return f"{nombre_bebida} Cocktail"
    return f"{nombre_bebida} Mocktail"
```

**Conceptos:**
- Iteración sobre lista + operador `in` sobre set.
- Retorno temprano al encontrar alcohol.
- f-strings para componer el resultado.

**¿Por qué un set para ALCOHOLS?**
- La búsqueda `x in set` es O(1) (promedio).
- La búsqueda `x in list` es O(n).
- Para listas largas de ingredientes, es mucho más eficiente.

**Alternativa usando intersección de sets:**
```python
def check_drinks(nombre_bebida, ingredientes):
    if set(ingredientes) & ALCOHOLS:
        return f"{nombre_bebida} Cocktail"
    return f"{nombre_bebida} Mocktail"
```

---

### Ejercicio 10 — `unique_chars`

**Objetivo:** Obtener los caracteres únicos de un string.

**Solución:**
```python
def unique_chars(texto):
    return set(texto)
```

**Conceptos:**
- `set(string)` itera el string y agrega cada carácter al set, eliminando duplicados.
- Funciona también con string vacío (retorna `set()`).

---

### Ejercicio 11 — `sum_set`

**Objetivo:** Sumar los elementos de un set recorriéndolo.

**Solución:**
```python
def sum_set(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total
```

**Conceptos:**
- Iterar un set funciona igual que una tupla/lista, aunque **sin orden garantizado**.
- Para sumar no importa el orden: el resultado es el mismo.

**Nota sobre `while` con sets:**
Los sets **no soportan indexación** (`set[0]` da error). Para iterarlos con `while`
hay que usar `iter()` + `next()`, pero es más idiomático usar `for`.

---

### Ejercicio 12 — `common_elements`

**Objetivo:** Intersección de sets recorriendo manualmente.

**Solución:**
```python
def common_elements(set_a, set_b):
    resultado = set()
    for elem in set_a:
        if elem in set_b:
            resultado.add(elem)
    return resultado
```

**Conceptos:**
- Recorremos un set y verificamos pertenencia en el otro con `in`.
- `set.add(elemento)` agrega sin duplicar.
- `in` sobre set es **O(1)**, así que el total queda O(n).

**Consejo:** iterar el set más chico hace el algoritmo más eficiente:
```python
def common_elements(set_a, set_b):
    if len(set_b) < len(set_a):
        set_a, set_b = set_b, set_a
    resultado = set()
    for elem in set_a:
        if elem in set_b:
            resultado.add(elem)
    return resultado
```

---

## Parte 3 — Diccionarios (`exercise_dicts.py`)

### Ejercicio 13 — `create_inventory`

**Objetivo:** Construir un diccionario con el conteo de cada item.

**Solución:**
```python
def create_inventory(items):
    inventario = {}
    for item in items:
        if item in inventario:
            inventario[item] += 1
        else:
            inventario[item] = 1
    return inventario
```

**Alternativa con `.get()`:**
```python
def create_inventory(items):
    inventario = {}
    for item in items:
        inventario[item] = inventario.get(item, 0) + 1
    return inventario
```

**Alternativa con `collections.Counter`:**
```python
from collections import Counter

def create_inventory(items):
    return dict(Counter(items))
```

---

### Ejercicio 14 — `add_items`

**Objetivo:** Agregar items a un inventario existente.

**Solución:**
```python
def add_items(inventario, items):
    for item in items:
        if item in inventario:
            inventario[item] += 1
        else:
            inventario[item] = 1
    return inventario
```

**Conceptos:**
- Operador `in` para verificar presencia de clave.
- `+= 1` para incrementar.
- `create_inventory` se puede implementar reutilizando `add_items({}, items)` (están en el mismo archivo).

---

### Ejercicio 15 — `decrement_items`

**Objetivo:** Restar items sin dejar valores negativos.

**Solución:**
```python
def decrement_items(inventario, items):
    for item in items:
        if item in inventario and inventario[item] > 0:
            inventario[item] -= 1
    return inventario
```

**Conceptos:**
- Doble condición: el item debe existir Y tener cantidad > 0.
- El operador `and` cortocircuita (no se evalúa la segunda si la primera es False).
- Items que no están en el inventario se ignoran.

**¿Por qué no usar `max(0, ...)`?**
```python
# Esta solución también funciona para lógica de no-negativos, pero
# solo si el item existe en el inventario:
if item in inventario:
    inventario[item] = max(0, inventario[item] - 1)
```

---

### Ejercicio 16 — `remove_item`

**Objetivo:** Eliminar un item del inventario.

**Solución:**
```python
def remove_item(inventario, item):
    if item in inventario:
        del inventario[item]
    return inventario
```

**Conceptos:**
- `del dict[clave]` elimina la entrada.
- Validar con `in` para evitar `KeyError`.

**Alternativa con `.pop()`:**
```python
def remove_item(inventario, item):
    inventario.pop(item, None)  # None como default si no existe
    return inventario
```

---

### Ejercicio 17 — `list_inventory`

**Objetivo:** Retornar pares (item, cantidad) con cantidad > 0.

**Solución:**
```python
def list_inventory(inventario):
    return [(item, cantidad)
            for item, cantidad in inventario.items()
            if cantidad > 0]
```

**Conceptos:**
- `.items()` devuelve pares (clave, valor).
- List comprehension con filtro.
- Cada tupla es directamente `(item, cantidad)`.

**Alternativa con loop explícito:**
```python
def list_inventory(inventario):
    resultado = []
    for item, cantidad in inventario.items():
        if cantidad > 0:
            resultado.append((item, cantidad))
    return resultado
```

---

### Ejercicio 18 — `find_max_value`

**Objetivo:** Encontrar la clave con el mayor valor.

**Solución:**
```python
def find_max_value(diccionario):
    if not diccionario:
        return ""
    return max(diccionario, key=diccionario.get)
```

**Conceptos:**
- `max(dict, key=dict.get)` itera las claves y usa el valor como criterio.
- Validar `if not diccionario` cubre el caso vacío (evita `ValueError` de `max`).

**Alternativa con loop explícito:**
```python
def find_max_value(diccionario):
    if not diccionario:
        return ""
    mejor_clave = None
    for clave, valor in diccionario.items():
        if mejor_clave is None or valor > diccionario[mejor_clave]:
            mejor_clave = clave
    return mejor_clave
```

---

### Ejercicio 19 — `reverse_dict`

**Objetivo:** Invertir el diccionario concatenando claves duplicadas.

**Solución:**
```python
def reverse_dict(diccionario):
    resultado = {}
    for clave, valor in diccionario.items():
        if valor in resultado:
            resultado[valor] += clave
        else:
            resultado[valor] = clave
    return resultado
```

**Conceptos:**
- Al recorrer `.items()` en orden, la concatenación respeta el orden de inserción.
- `resultado[valor] += clave` solo funciona si `clave` es un string.

---

### Ejercicio 20 — `word_frequency`

**Objetivo:** Contar la frecuencia de cada palabra.

**Solución:**
```python
def word_frequency(palabras):
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia
```

**Alternativa con `Counter`:**
```python
from collections import Counter

def word_frequency(palabras):
    return dict(Counter(palabras))
```

**Nota:** iterar un string vacío (`""`) tampoco recorre nada, por eso retorna `{}` sin condición especial.

---

### Ejercicio 21 — `find_biggest_expense`

**Objetivo:** Categoría con el promedio de gastos más alto.

**Solución:**
```python
def find_biggest_expense(gastos):
    if not gastos:
        return ""
    return max(gastos, key=lambda cat: sum(gastos[cat]) / len(gastos[cat]))
```

**Conceptos:**
- `max(dict, key=lambda)` permite usar el promedio como criterio.
- Validar el caso vacío antes de `max` evita errores.

**Alternativa con loop explícito:**
```python
def find_biggest_expense(gastos):
    if not gastos:
        return ""
    mejor_cat = None
    mejor_prom = -float("inf")
    for cat, montos in gastos.items():
        prom = sum(montos) / len(montos)
        if prom > mejor_prom:
            mejor_prom = prom
            mejor_cat = cat
    return mejor_cat
```

---

### Ejercicio 22 — `sum_expenses`

**Objetivo:** Sumar los gastos de cada categoría.

**Solución:**
```python
def sum_expenses(gastos):
    return {categoria: sum(montos) for categoria, montos in gastos.items()}
```

**Conceptos:**
- Dict comprehension sobre `.items()`.
- `sum([])` devuelve 0, así que listas vacías no rompen nada.

---

### Ejercicio 23 — `sum_expenses_by_type`

**Objetivo:** Agrupar por tipo (ignorando la categoría) y sumar.

**Solución:**
```python
def sum_expenses_by_type(gastos):
    resultado = {}
    for montos in gastos.values():
        for tipo, monto in montos:
            resultado[tipo] = resultado.get(tipo, 0) + monto
    return resultado
```

**Conceptos:**
- `.values()` descarta las categorías, que en este caso son solo contenedores.
- Desempaquetado `for tipo, monto in montos` directo sobre la tupla.
- `resultado.get(tipo, 0)` inicializa en 0 si el tipo es nuevo.

**Alternativa con `defaultdict`:**
```python
from collections import defaultdict

def sum_expenses_by_type(gastos):
    resultado = defaultdict(int)
    for montos in gastos.values():
        for tipo, monto in montos:
            resultado[tipo] += monto
    return dict(resultado)
```

---

## Tabla Resumen de Operaciones

### Tuplas
| Operación           | Ejemplo                      | Resultado          |
| ------------------- | ---------------------------- | ------------------ |
| Acceso por índice   | `t[0]`                       | Primer elemento    |
| Concatenación       | `(1, 2) + (3, 4)`            | `(1, 2, 3, 4)`     |
| Construcción        | `tuple("ab")`                | `('a', 'b')`       |
| Desempaquetado      | `a, b = (1, 2)`              | `a=1, b=2`         |

### Sets
| Operación           | Ejemplo                      | Resultado          |
| ------------------- | ---------------------------- | ------------------ |
| Crear desde lista   | `set([1, 1, 2])`             | `{1, 2}`           |
| Pertenencia         | `2 in {1, 2, 3}`             | `True`             |
| Intersección        | `{1, 2} & {2, 3}`            | `{2}`              |
| Unión               | `{1, 2} \| {2, 3}`           | `{1, 2, 3}`        |
| Diferencia          | `{1, 2, 3} - {2}`            | `{1, 3}`           |

### Diccionarios
| Operación           | Ejemplo                      | Resultado          |
| ------------------- | ---------------------------- | ------------------ |
| Acceso por clave    | `d["k"]`                     | Valor de "k"       |
| Con default         | `d.get("k", 0)`              | Valor o 0          |
| Pertenencia         | `"k" in d`                   | `True` / `False`   |
| Agregar / actualizar| `d["k"] = v`                 | Modifica el dict   |
| Eliminar            | `del d["k"]` / `d.pop("k")`  | Elimina entrada    |
| Iterar pares        | `for k, v in d.items():`     | Clave y valor      |

---

## Tips y Buenas Prácticas

1. **Tuplas vs listas:**
    - Tuplas: inmutables, ideales para registros o retornar múltiples valores.
    - Listas: mutables, ideales para colecciones que cambian.

2. **Sets para eliminar duplicados:**
   ```python
   # Simple y eficiente
   unicos = set(lista_con_duplicados)

   # Para mantener orden:
   unicos = list(dict.fromkeys(lista_con_duplicados))
   ```

3. **Pertenencia con `in`:**
   ```python
   # O(1) — muy rápido
   if elemento in mi_set:
       ...

   # O(n) — lento en listas grandes
   if elemento in mi_lista:
       ...
   ```

4. **Validar antes de acceder a un diccionario:**
   ```python
   # Correcto
   if clave in d:
       valor = d[clave]

   # Correcto con default
   valor = d.get(clave, valor_por_defecto)

   # Puede fallar con KeyError
   valor = d[clave]
   ```

5. **Evitar negativos al decrementar:**
   ```python
   # Validar antes
   if inventario[item] > 0:
       inventario[item] -= 1

   # Con max()
   inventario[item] = max(0, inventario[item] - 1)
   ```

---
