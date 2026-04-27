# Soluciones TP7 - Estructuras de Datos

Este archivo contiene las soluciones de referencia para todos los ejercicios del TP7.

Los ejercicios están agrupados en 3 archivos según la estructura de datos que usan:

- `exercise_tuples.py` — ejercicios 1 a 3 (tuplas)
- `exercise_sets.py` — ejercicios 4 y 5 (sets)
- `exercise_dicts.py` — ejercicios 6 a 10 (diccionarios)

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

## Parte 2 — Sets (`exercise_sets.py`)

### Ejercicio 4 — `clean_ingredients`

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

### Ejercicio 5 — `check_drinks`

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

## Parte 3 — Diccionarios (`exercise_dicts.py`)

### Ejercicio 6 — `create_inventory`

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

### Ejercicio 7 — `add_items`

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

### Ejercicio 8 — `decrement_items`

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

### Ejercicio 9 — `remove_item`

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

### Ejercicio 10 — `list_inventory`

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
