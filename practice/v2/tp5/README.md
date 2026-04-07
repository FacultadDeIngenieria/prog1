---
title: Práctica 5
layout: practice
permalink: /practice/5
---

# TP5 - Trabajo Práctico 5
## Completar el trabajo práctico en GitHub Classroom

[Link al TP 5](https://classroom.github.com/a/olaKydob)

# TP5 - Trabajo Práctico 5

## Temas evaluados

Listas, operaciones con listas, acceso por índices, manipulación de elementos, iteración, funciones de listas, listas anidadas.

---

## Ejercicios

### Ejercicio 1 — `exercise_list_length.py`

**Archivo de test:** `test_tp5_list_length.py`

**Conceptos:** Función `len`, listas básicas.

**Consigna:** Crear una función que retorne la cantidad de elementos en una lista.

**Ejemplo:** Para `lista = [1, 2, 3, 4, 5]` la salida esperada es:

```
5
```

Para `lista = []` la salida esperada es:

```
0
```

---

### Ejercicio 2 — `exercise_get_element.py`

**Archivo de test:** `test_tp5_get_element.py`

**Conceptos:** Acceso por índice, validación de rangos.

**Consigna:** Crear una función que retorne el elemento en la posición indicada por el índice. Si el índice está fuera de rango (positivo o negativo), la función debe retornar `None` en lugar de generar un error.

**Ejemplo:** Para `lista = [10, 20, 30]` e `indice = 1` la salida esperada es:

```
20
```

Para `lista = [10, 20, 30]` e `indice = 10` la salida esperada es:

```
None
```

Para `lista = [10, 20, 30]` e `indice = -1` la salida esperada es:

```
30
```

---

### Ejercicio 3 — `exercise_add_elements.py`

**Archivo de test:** `test_tp5_add_elements.py`

**Conceptos:** `insert`, `append`, modificación de listas.

**Consigna:** Crear una función que agregue el elemento `'Pink'` al principio de la lista y el elemento `'Yellow'` al final de la lista. La función debe retornar la lista modificada.

**Ejemplo:** Para `lista = ['Red', 'Green', 'White', 'Black']` la salida esperada es:

```
['Pink', 'Red', 'Green', 'White', 'Black', 'Yellow']
```

Para `lista = []` la salida esperada es:

```
['Pink', 'Yellow']
```

---

### Ejercicio 4 — `exercise_remove_elements.py`

**Archivo de test:** `test_tp5_remove_elements.py`

**Conceptos:** `pop`, `del`, índices, manejo de listas de diferentes tamaños.

**Consigna:** Crear una función que remueva el primer elemento, el quinto elemento y el sexto elemento de la lista. La función debe funcionar correctamente con listas de cualquier tamaño, incluyendo listas más cortas que los índices indicados.

**Importante:** Tener en cuenta que al remover un elemento, los índices de los elementos posteriores cambian.

**Ejemplo:** Para `lista = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']` la salida esperada es:

```
['Green', 'White', 'Black']
```

Para `lista = ['Audi', 'BMW', 'Porsche', 'Aston Martin']` la salida esperada es:

```
['BMW', 'Porsche', 'Aston Martin']
```

Para `lista = []` la salida esperada es:

```
[]
```

---

### Ejercicio 5 — `exercise_find_max.py`

**Archivo de test:** `test_tp5_find_max.py`

**Conceptos:** búsqueda de elementos, manejo de listas vacías.

**Consigna:** Crear una función que encuentre y retorne el valor máximo en una lista de números. Si la lista está vacía, retornar `None`.

**Ejemplo:** Para `lista = [3, 7, 2, 9, 1]` la salida esperada es:

```
9
```

Para `lista = [-5, -2, -8, -1, -10]` la salida esperada es:

```
-1
```

Para `lista = []` la salida esperada es:

```
None
```

---

### Ejercicio 6 — `exercise_find_min.py`

**Archivo de test:** `test_tp5_find_min.py`

**Conceptos:** búsqueda de elementos, manejo de listas vacías.

**Consigna:** Crear una función que encuentre y retorne el valor mínimo en una lista de números. Si la lista está vacía, retornar `None`.

**Ejemplo:** Para `lista = [3, 7, 2, 9, 1]` la salida esperada es:

```
1
```

Para `lista = [-5, -2, -8, -1, -10]` la salida esperada es:

```
-10
```

Para `lista = []` la salida esperada es:

```
None
```

---

### Ejercicio 7 — `exercise_count_occurrences.py`

**Archivo de test:** `test_tp5_count_occurrences.py`

**Conceptos:** `count`, búsqueda de elementos.

**Consigna:** Crear una función que cuente cuántas veces aparece un elemento específico en la lista.

**Ejemplo:** Para `lista = [1, 2, 2, 3, 2, 4]` y `elemento = 2` la salida esperada es:

```
3
```

Para `lista = [1, 2, 3, 4, 5]` y `elemento = 10` la salida esperada es:

```
0
```

Para `lista = ['red', 'blue', 'red', 'green', 'red']` y `elemento = 'red'` la salida esperada es:

```
3
```

---

### Ejercicio 8 — `exercise_reverse_list.py`

**Archivo de test:** `test_tp5_reverse_list.py`

**Conceptos:** slicing, creación de nuevas listas.

**Consigna:** Crear una función que retorne una nueva lista con los elementos en orden inverso. La lista original no debe ser modificada.

**Ejemplo:** Para `lista = [1, 2, 3, 4, 5]` la salida esperada es:

```
[5, 4, 3, 2, 1]
```

Para `lista = ['a', 'b', 'c', 'd']` la salida esperada es:

```
['d', 'c', 'b', 'a']
```

Para `lista = []` la salida esperada es:

```
[]
```

---

### Ejercicio 9 — `exercise_is_empty.py`

**Archivo de test:** `test_tp5_is_empty.py`

**Conceptos:** Verificación de listas vacías, expresiones booleanas.

**Consigna:** Crear una función que determine si una lista está vacía. Debe retornar `True` si la lista está vacía y `False` en caso contrario.

**Ejemplo:** Para `lista = []` la salida esperada es:

```
True
```

Para `lista = [1]` la salida esperada es:

```
False
```

Para `lista = ['Red', 'Green', 'White', 'Black']` la salida esperada es:

```
False
```

---

### Ejercicio 10 — `exercise_concatenate_lists.py`

**Archivo de test:** `test_tp5_concatenate_lists.py`

**Conceptos:** concatenación de listas.

**Consigna:** Crear una función que concatene dos listas en una sola. La función debe retornar una nueva lista con todos los elementos de la primera lista seguidos de todos los elementos de la segunda lista.

**Ejemplo:** Para `lista1 = [1, 2, 3]` y `lista2 = [4, 5, 6]` la salida esperada es:

```
[1, 2, 3, 4, 5, 6]
```

Para `lista1 = []` y `lista2 = [1, 2, 3]` la salida esperada es:

```
[1, 2, 3]
```

Para `lista1 = [1, 2]` y `lista2 = ['a', 'b']` la salida esperada es:

```
[1, 2, 'a', 'b']
```

---

### Ejercicio 11 — `exercise_check_lists.py`

**Archivo de test:** `test_tp5_check_lists.py`

**Conceptos:** Acceso por índice, comparación, validación de longitud.

**Consigna:** Crear una función que verifique si ambas listas tienen el mismo elemento en la tercera posición (índice 2). Si alguna de las listas no tiene un tercer elemento, la función debe retornar `False`.

**Ejemplo:** Para `lista1 = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']` y `lista2 = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']` la salida esperada es:

```
True
```

Para `lista1 = ['Black', 'Pink', 'Green', 'White']` y `lista2 = ['Red', 'Green', 'Yellow', 'Black', 'Pink']` la salida esperada es:

```
False
```

Para `lista1 = ['Black', 'Pink']` y `lista2 = ['Red', 'Green', 'Yellow', 'Black', 'Pink']` la salida esperada es:

```
False
```

---

### Ejercicio 12 — `exercise_list_of_lists.py`

**Archivo de test:** `test_tp5_list_of_lists.py`

**Conceptos:** Listas anidadas, slicing avanzado, manipulación de múltiples dimensiones.

**Consigna:** Crear una función que reciba una lista que contiene exactamente 3 listas internas y modifique cada una de ellas según las siguientes reglas:

- **Primera lista:** Conservar solo los primeros 2 elementos (índices 0 y 1)
- **Segunda lista:** Conservar solo los elementos entre el segundo y cuarto elemento inclusive (índices 1 a 3)
- **Tercera lista:** Conservar solo los últimos 2 elementos

La función debe funcionar correctamente incluso si alguna de las listas internas tiene menos elementos de los esperados.

**Ejemplo:** Para `lista = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]` la salida esperada es:

```
[[1, 2], [5, 6, 7], [11, 12]]
```

Para `lista = [[], [4, 5, 6], [10, 11, 12]]` la salida esperada es:

```
[[], [5, 6], [11, 12]]
```

Para `lista = [[1, 2], [], [12]]` la salida esperada es:

```
[[1, 2], [], [12]]
```

---
