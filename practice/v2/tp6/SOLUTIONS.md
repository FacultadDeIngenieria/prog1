# Soluciones TP6 - Bucles for y while

Este archivo contiene las soluciones de referencia para todos los ejercicios del TP6.

---

## Ejercicio 1 - `sum_range.py`

**Objetivo:** Usar bucles `for` con `range()` y acumuladores.

**Solución:**
```python
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_evens(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

**Conceptos:**
- `range(1, n + 1)` genera números de 1 a n inclusive
- `range(2, n + 1, 2)` genera pares: 2, 4, 6, ...
- Acumulador aditivo (`+=`) y multiplicativo (`*=`)
- Si `n <= 0`, los `range()` generan secuencias vacías, retornando el valor inicial

---

## Ejercicio 2 - `powers.py`

**Objetivo:** Calcular potencias con bucle y componer funciones.

**Solución:**
```python
def power(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

def sum_of_powers(base, max_exp):
    total = 0
    for i in range(max_exp + 1):
        total += power(base, i)
    return total
```

**Conceptos:**
- Acumulador multiplicativo para calcular potencia
- `range(exp)` repite la multiplicación `exp` veces
- `sum_of_powers` **usa** `power` (composición de funciones)
- `power(base, 0)` retorna 1 porque el bucle no ejecuta

---

## Ejercicio 3 - `enumerate_list.py`

**Objetivo:** Recorrer listas, generar nuevas listas enumeradas, saltear vacíos.

**Solución:**
```python
def enumerate_list(lst):
    result = []
    index = 0
    for item in lst:
        if item != "":
            result.append(str(index) + ". " + item)
            index += 1
    return result

def enumerate_backwards(lst):
    result = []
    index = 0
    for item in lst:
        if item != "":
            result.append(str(index) + ". " + item[::-1])
            index += 1
    return result
```

**Conceptos:**
- Índice manual separado del recorrido (se incrementa solo cuando no se saltea)
- `item[::-1]` invierte el string
- Filtrado de strings vacíos con `if item != ""`

---

## Ejercicio 4 - `search.py`

**Objetivo:** Búsqueda lineal con retorno temprano.

**Solución:**
```python
def index_of(target, lst):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

def index_of_by_index(target, lst, start):
    for i in range(start, len(lst)):
        if lst[i] == target:
            return i
    return -1

def index_of_empty(lst):
    for i in range(len(lst)):
        if lst[i] == "":
            return i
    return -1
```

**Conceptos:**
- `range(len(lst))` para recorrer por índice
- `range(start, len(lst))` para comenzar desde una posición
- Retorno temprano: `return i` cuando se encuentra el elemento
- Retorno `-1` al final si no se encontró

---

## Ejercicio 5 - `list_modify.py`

**Objetivo:** Modificar listas in-place con búsqueda lineal.

**Solución:**
```python
def put(value, lst):
    for i in range(len(lst)):
        if lst[i] == "":
            lst[i] = value
            return i
    return -1

def remove(value, lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] == value:
            lst[i] = ""
            count += 1
    return count
```

**Conceptos:**
- `put` busca el primer vacío y coloca el valor (retorno temprano)
- `remove` recorre toda la lista reemplazando ocurrencias
- Ambas funciones **modifican la lista original**
- Acumulador `count` para contar eliminaciones

---

## Ejercicio 6 - `while_basics.py`

**Objetivo:** Usar bucles `while` para generar secuencias.

**Solución:**
```python
def countdown(n):
    result = []
    while n >= 0:
        result.append(n)
        n -= 1
    return result

def double_until(limit):
    result = []
    value = 1
    while value <= limit:
        result.append(value)
        value *= 2
    return result
```

**Conceptos:**
- `while n >= 0` termina cuando n es negativo
- `while value <= limit` termina cuando el valor supera el límite
- Si `n < 0` o `limit < 1`, el bucle no ejecuta y retorna `[]`
- `value *= 2` duplica el valor en cada iteración

---

## Ejercicio 7 - `collatz.py`

**Objetivo:** Implementar la conjetura de Collatz con `while`.

**Solución:**
```python
def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        steps += 1
    return steps

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        sequence.append(n)
    return sequence
```

**Conceptos:**
- Condición de terminación desconocida: no sabemos cuántas iteraciones
- `n % 2 == 0` para verificar si es par
- `//` para división entera
- `collatz_sequence` guarda cada valor en la lista

---

## Ejercicio 8 - `nested_loops.py`

**Objetivo:** Operar sobre matrices con bucles anidados.

**Solución:**
```python
def flatten(matrix):
    result = []
    for row in matrix:
        for element in row:
            result.append(element)
    return result

def row_sums(matrix):
    result = []
    for row in matrix:
        total = 0
        for element in row:
            total += element
        result.append(total)
    return result

def col_sums(matrix):
    if len(matrix) == 0:
        return []
    num_cols = len(matrix[0])
    result = []
    for col in range(num_cols):
        total = 0
        for row in matrix:
            total += row[col]
        result.append(total)
    return result
```

**Conceptos:**
- Bucle externo recorre filas, interno recorre elementos
- `flatten` agrega todos los elementos a una única lista
- `row_sums` acumula por fila
- `col_sums` recorre por columna usando `range(num_cols)` y acceso por índice

---

## Ejercicio 9 - `find_extremes.py`

**Objetivo:** Encontrar valores extremos recorriendo listas.

**Solución:**
```python
def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

def count_negatives(numbers):
    count = 0
    for num in numbers:
        if num < 0:
            count += 1
    return count
```

**Conceptos:**
- Inicializar el mínimo/máximo con el primer elemento
- Recorrer comparando cada elemento
- Acumulador `count` para contar negativos
- Lista vacía retorna 0 en `count_negatives`

---

## Ejercicio 10 - `list_stats.py`

**Objetivo:** Componer funciones usando `find_min` y `find_max` provistas.

**Solución:**
```python
def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

def range_of(numbers):
    return find_max(numbers) - find_min(numbers)

def average(numbers):
    if len(numbers) == 0:
        return 0.0
    total = 0
    for num in numbers:
        total += num
    return round(total / len(numbers), 1)

def describe(numbers):
    if len(numbers) == 0:
        return "Empty list"
    mn = find_min(numbers)
    mx = find_max(numbers)
    rng = range_of(numbers)
    avg = average(numbers)
    return "Min:" + str(mn) + " Max:" + str(mx) + " Range:" + str(rng) + " Avg:" + str(avg)
```

**Conceptos:**
- `range_of` **usa** `find_max` y `find_min` (no reimplementa)
- `average` usa acumulador y `round(valor, 1)` para 1 decimal
- `describe` compone todas las funciones en un string formateado
- Validar lista vacía en `average` y `describe`

---

## Tips y Buenas Prácticas

1. **Acumuladores - inicializar correctamente:**
   ```python
   # Suma → inicializar en 0
   total = 0
   for x in lista:
       total += x

   # Producto → inicializar en 1
   result = 1
   for x in lista:
       result *= x
   ```

2. **`range()` con diferentes argumentos:**
   ```python
   range(5)        # 0, 1, 2, 3, 4
   range(1, 6)     # 1, 2, 3, 4, 5
   range(2, 11, 2) # 2, 4, 6, 8, 10
   ```

3. **Búsqueda lineal con retorno temprano:**
   ```python
   # ✓ Eficiente - retorna al encontrar
   for i in range(len(lst)):
       if lst[i] == target:
           return i
   return -1

   # ✗ Ineficiente - recorre toda la lista
   found = -1
   for i in range(len(lst)):
       if lst[i] == target:
           found = i
   return found
   ```

4. **`while` vs `for`:**
   ```python
   # Usar for cuando sabemos cuántas iteraciones
   for i in range(10):
       ...

   # Usar while cuando NO sabemos cuántas iteraciones
   while n != 1:
       ...
   ```

5. **Modificar lista vs crear nueva:**
   ```python
   # Modificar in-place (cambia la original)
   lst[i] = new_value

   # Crear nueva (la original no cambia)
   new_list = []
   for item in lst:
       new_list.append(transform(item))
   ```
