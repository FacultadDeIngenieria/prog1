---
title: Práctica 6
layout: practice
permalink: /practice/6
---

# TP6 - Trabajo Práctico 6
## Completar el trabajo práctico en GitHub Classroom

[Link al TP 6](https://classroom.github.com/a/c4hUW7DF)

# TP6 - Trabajo Práctico 6

## Temas evaluados

Bucles `for` y `while`, `range()`, `enumerate()`, bucles anidados, `break`, recorrido e iteración de listas, acumuladores, búsqueda lineal, modificación de listas, composición de funciones con bucles.

---

## Ejercicios

### Ejercicio 1 — `sum_range.py`

**Archivo de test:** `test_tp6_sum_range.py`

**Conceptos:** Bucle `for`, `range()`, acumuladores.

**Consigna:** Implementar tres funciones que usen bucles `for` con `range()` para realizar cálculos con acumuladores.

```python
def sum_to_n(n):
    """Retorna la suma de todos los enteros desde 1 hasta n (inclusive). Si n <= 0, retorna 0."""

def sum_evens(n):
    """Retorna la suma de todos los números pares desde 1 hasta n (inclusive). Si n <= 0, retorna 0."""

def factorial(n):
    """Retorna el factorial de n (n!). Si n <= 0, retorna 1."""
```

**Ejemplos:**
- `sum_to_n(5)` → `15`
- `sum_to_n(100)` → `5050`
- `sum_to_n(0)` → `0`
- `sum_evens(10)` → `30` (2+4+6+8+10)
- `sum_evens(7)` → `12` (2+4+6)
- `sum_evens(1)` → `0`
- `factorial(5)` → `120`
- `factorial(1)` → `1`
- `factorial(0)` → `1`

---

### Ejercicio 2 — `powers.py`

**Archivo de test:** `test_tp6_powers.py`

**Conceptos:** Bucle `for`, `range()`, acumulador multiplicativo, composición de funciones.

**Consigna:** Implementar una función que calcule la potencia usando un bucle, y otra que use la primera para sumar potencias.

```python
def power(base, exp):
    """Retorna base elevado a exp usando un bucle for. exp >= 0."""

def sum_of_powers(base, max_exp):
    """Retorna base^0 + base^1 + ... + base^max_exp. Debe USAR power."""
```

**Ejemplos:**
- `power(2, 3)` → `8`
- `power(5, 0)` → `1`
- `power(3, 4)` → `81`
- `sum_of_powers(2, 3)` → `15` (1+2+4+8)
- `sum_of_powers(3, 2)` → `13` (1+3+9)
- `sum_of_powers(5, 0)` → `1`

---

### Ejercicio 3 — `enumerate_list.py`

**Archivo de test:** `test_tp6_enumerate_list.py`

**Conceptos:** Bucle `for`, iteración de listas, strings, listas nuevas, índices consecutivos.

**Consigna:** Implementar dos funciones que recorran una lista de strings y generen una nueva lista enumerada. Los strings vacíos deben saltearse y el índice debe ser consecutivo (no el original).

```python
def enumerate_list(lst):
    """Dada una lista de strings, retorna una nueva lista con formato "indice. valor". Saltea strings vacíos."""

def enumerate_backwards(lst):
    """Igual que enumerate_list pero cada palabra está escrita al revés. Saltea strings vacíos."""
```

**Ejemplos:**
- `enumerate_list(["Red", "Green", "", "White", "Black"])` → `["0. Red", "1. Green", "2. White", "3. Black"]`
- `enumerate_list(["", "", ""])` → `[]`
- `enumerate_backwards(["Red", "Green", "", "White", "Black"])` → `["0. deR", "1. neerG", "2. etihW", "3. kcalB"]`
- `enumerate_backwards(["Hello", "World"])` → `["0. olleH", "1. dlroW"]`

---

### Ejercicio 4 — `search.py`

**Archivo de test:** `test_tp6_search.py`

**Conceptos:** Bucle `for`, búsqueda lineal, `range()`, retorno temprano.

**Consigna:** Implementar tres funciones de búsqueda sobre listas de strings. Todas deben retornar `-1` si no encuentran lo buscado.

```python
def index_of(target, lst):
    """Retorna el índice de la primera ocurrencia de target en lst, o -1."""

def index_of_by_index(target, lst, start):
    """Retorna el índice de la primera ocurrencia de target a partir de start (inclusive), o -1."""

def index_of_empty(lst):
    """Retorna el índice del primer string vacío en lst, o -1."""
```

**Ejemplos:**
- `index_of("Black", ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"])` → `3`
- `index_of("Blue", ["Red", "Green"])` → `-1`
- `index_of_by_index("Black", ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"], 4)` → `6`
- `index_of_by_index("Green", ["Red", "Green", "White"], 2)` → `-1`
- `index_of_empty(["Red", "Green", "", "", "Pink"])` → `2`
- `index_of_empty(["Red", "Green", "White"])` → `-1`

---

### Ejercicio 5 — `list_modify.py`

**Archivo de test:** `test_tp6_list_modify.py`

**Conceptos:** Bucle `for`, modificación de listas, búsqueda lineal.

**Consigna:** Implementar dos funciones que modifiquen una lista de strings. Las funciones **modifican la lista original** (no crean una nueva).

```python
def put(value, lst):
    """Coloca value en el primer lugar vacío ("") de lst. Retorna el índice o -1."""

def remove(value, lst):
    """Reemplaza todas las ocurrencias de value por "". Retorna cantidad de eliminaciones."""
```

**Ejemplos:**
- `put("Blue", ["Red", "", "Green"])` → `1` (la lista queda `["Red", "Blue", "Green"]`)
- `put("Blue", ["Red", "Green", "White"])` → `-1`
- `remove("Black", ["Red", "Black", "Green", "Black"])` → `2` (la lista queda `["Red", "", "Green", ""]`)
- `remove("Blue", ["Red", "Green"])` → `0`

---

### Ejercicio 6 — `while_basics.py`

**Archivo de test:** `test_tp6_while_basics.py`

**Conceptos:** Bucle `while`, listas, condición de terminación.

**Consigna:** Implementar dos funciones que usen bucles `while` para generar secuencias de números.

```python
def countdown(n):
    """Retorna una lista con la cuenta regresiva desde n hasta 0. Si n < 0, retorna []."""

def double_until(limit):
    """Comenzando desde 1, duplica el valor y lo agrega a una lista mientras sea <= limit. Si limit < 1, retorna []."""
```

**Ejemplos:**
- `countdown(5)` → `[5, 4, 3, 2, 1, 0]`
- `countdown(0)` → `[0]`
- `countdown(-1)` → `[]`
- `double_until(10)` → `[1, 2, 4, 8]`
- `double_until(1)` → `[1]`
- `double_until(16)` → `[1, 2, 4, 8, 16]`
- `double_until(0)` → `[]`

---

### Ejercicio 7 — `collatz.py`

**Archivo de test:** `test_tp6_collatz.py`

**Conceptos:** Bucle `while`, condición de terminación desconocida, listas.

**Consigna:** La conjetura de Collatz dice que para cualquier número entero positivo, si aplicamos repetidamente las reglas: si es par dividir por 2, si es impar multiplicar por 3 y sumar 1, eventualmente llegamos a 1.

```python
def collatz_steps(n):
    """Retorna la cantidad de pasos para llegar de n a 1. Si n es 1, retorna 0."""

def collatz_sequence(n):
    """Retorna la secuencia completa de Collatz como lista, desde n hasta 1."""
```

**Ejemplos:**
- `collatz_steps(1)` → `0`
- `collatz_steps(6)` → `8` (6→3→10→5→16→8→4→2→1)
- `collatz_steps(10)` → `6`
- `collatz_sequence(1)` → `[1]`
- `collatz_sequence(6)` → `[6, 3, 10, 5, 16, 8, 4, 2, 1]`
- `collatz_sequence(10)` → `[10, 5, 16, 8, 4, 2, 1]`

---

### Ejercicio 8 — `nested_loops.py`

**Archivo de test:** `test_tp6_nested_loops.py`

**Conceptos:** Bucles `for` anidados, listas de listas (matrices), `range()`.

**Consigna:** Implementar tres funciones que operen sobre matrices (listas de listas de números) usando bucles anidados.

```python
def flatten(matrix):
    """Dada una lista de listas, retorna una única lista con todos los elementos."""

def row_sums(matrix):
    """Retorna una lista con la suma de cada fila."""

def col_sums(matrix):
    """Retorna una lista con la suma de cada columna. Todas las filas tienen la misma longitud."""
```

**Ejemplos:**
- `flatten([[1, 2], [3, 4], [5, 6]])` → `[1, 2, 3, 4, 5, 6]`
- `flatten([[1], [2, 3], [4, 5]])` → `[1, 2, 3, 4, 5]`
- `row_sums([[1, 2, 3], [4, 5, 6]])` → `[6, 15]`
- `row_sums([[1, 2, 3], [4, 5, 6], [7, 8, 9]])` → `[6, 15, 24]`
- `col_sums([[1, 2, 3], [4, 5, 6]])` → `[5, 7, 9]`
- `col_sums([[1, 2, 3], [4, 5, 6], [7, 8, 9]])` → `[12, 15, 18]`

---

### Ejercicio 9 — `find_extremes.py`

**Archivo de test:** `test_tp6_find_extremes.py`

**Conceptos:** Bucle `for`, recorrido de listas, acumuladores, comparación.

**Consigna:** Implementar tres funciones que recorran una lista de números para encontrar valores extremos y contar elementos.

```python
def find_min(numbers):
    """Dada una lista de números (no vacía), retorna el menor valor."""

def find_max(numbers):
    """Dada una lista de números (no vacía), retorna el mayor valor."""

def count_negatives(numbers):
    """Retorna la cantidad de números negativos en la lista. Si está vacía, retorna 0."""
```

**Ejemplos:**
- `find_min([3, 1, 7, 2])` → `1`
- `find_min([-3, -1, -7])` → `-7`
- `find_max([3, 1, 7, 2])` → `7`
- `find_max([-3, -1, -7])` → `-1`
- `count_negatives([3, -1, -7, 2])` → `2`
- `count_negatives([1, 2, 3])` → `0`
- `count_negatives([])` → `0`

---

### Ejercicio 10 — `list_stats.py`

**Archivo de test:** `test_tp6_list_stats.py`

**Conceptos:** Composición de funciones, bucles `for`, acumuladores, funciones provistas.

**Consigna:** Se proveen dos funciones ya implementadas: `find_min(numbers)` y `find_max(numbers)`. El alumno debe **usar** estas funciones (no reimplementar la lógica) para implementar `range_of`, `average` y `describe`.

Las funciones provistas son:
```python
def find_min(numbers):
    """Dada una lista de números, retorna el menor valor."""

def find_max(numbers):
    """Dada una lista de números, retorna el mayor valor."""
```

Las funciones a implementar:
```python
def range_of(numbers):
    """Retorna max - min. Debe USAR find_min y find_max."""

def average(numbers):
    """Retorna el promedio redondeado a 1 decimal. Si la lista está vacía, retorna 0.0."""

def describe(numbers):
    """Retorna "Min:{min} Max:{max} Range:{range} Avg:{avg}". Si la lista está vacía, retorna "Empty list"."""
```

**Ejemplos:**
- `range_of([3, 1, 7, 2])` → `6`
- `range_of([5, 5, 5])` → `0`
- `average([10, 20, 30])` → `20.0`
- `average([])` → `0.0`
- `average([1, 2, 7])` → `3.3`
- `describe([3, 1, 7, 2])` → `"Min:1 Max:7 Range:6 Avg:3.2"`
- `describe([])` → `"Empty list"`

---
