---
marp: true
theme: default
paginate: true
---

# Introducción a la Programación I
## Clase 5: Listas

---

## ¿Qué es una lista?

Una **lista** es una colección **ordenada** y **mutable** de elementos.

```python
# Lista vacía
mi_lista = []

# Lista con elementos
frutas = ["manzana", "banana", "naranja"]
numeros = [1, 2, 3, 4, 5]
mixta = ["hola", 42, 3.14, True]
```

- Se escribe con **corchetes** `[]`
- Los elementos se separan con **comas**
- Puede contener cualquier tipo de dato (¡incluso mezclarlos!)
- Es **mutable**: podemos cambiarla después de crearla

---

## Índices

Python numera los elementos de una lista empezando desde **0**:

```python
frutas = ["manzana", "banana", "naranja"]
#              0          1         2
```

También se pueden usar **índices negativos** para contar desde el final:

```python
frutas = ["manzana", "banana", "naranja"]
#             -3         -2        -1
```

| Índice positivo | Índice negativo | Elemento |
|---|---|---|
| `0` | `-3` | `"manzana"` |
| `1` | `-2` | `"banana"` |
| `2` | `-1` | `"naranja"` |

---

## Acceder a elementos

Usamos el índice entre corchetes para acceder a un elemento:

```python
frutas = ["manzana", "banana", "naranja"]

print(frutas[0])    # manzana
print(frutas[1])    # banana
print(frutas[2])    # naranja

# Índices negativos
print(frutas[-1])   # naranja (último)
print(frutas[-2])   # banana (penúltimo)
```

El elemento devuelto es un valor normal que podés usar en cualquier expresión:

```python
print(f"Mi fruta favorita es la {frutas[0].upper()}.")
# Mi fruta favorita es la MANZANA.
```

---

## len() con listas

La función `len()` devuelve la **cantidad de elementos** de una lista:

```python
frutas = ["manzana", "banana", "naranja"]
print(len(frutas))   # 3

vacia = []
print(len(vacia))    # 0

numeros = [10, 20, 30, 40, 50]
print(len(numeros))  # 5
```

Útil para obtener el **último índice válido**:

```python
ultimo_indice = len(frutas) - 1
print(frutas[ultimo_indice])   # naranja
# equivalente a frutas[-1]
```

---

## Modificar elementos

Las listas son **mutables**: podemos cambiar sus elementos:

```python
frutas = ["manzana", "banana", "naranja"]
print(frutas)   # ['manzana', 'banana', 'naranja']

frutas[1] = "pera"
print(frutas)   # ['manzana', 'pera', 'naranja']

frutas[0] = "uva"
print(frutas)   # ['uva', 'pera', 'naranja']
```

La sintaxis es simple:
```python
lista[indice] = nuevo_valor
```

---

## Agregar elementos: append()

`append()` agrega un elemento **al final** de la lista:

```python
frutas = ["manzana", "banana"]
frutas.append("naranja")
frutas.append("uva")

print(frutas)   # ['manzana', 'banana', 'naranja', 'uva']
```


---

## Agregar elementos: insert()

`insert()` agrega un elemento en **cualquier posición**:

```python
frutas = ["manzana", "banana", "naranja"]

frutas.insert(0, "uva")       # inserta al inicio
print(frutas)   # ['uva', 'manzana', 'banana', 'naranja']

frutas.insert(2, "pera")      # inserta en posición 2
print(frutas)   # ['uva', 'manzana', 'pera', 'banana', 'naranja']
```

La sintaxis es:
```python
lista.insert(indice, valor)
```

Los elementos que estaban en esa posición y después se **desplazan** una posición.

---

## Eliminar elementos: del

`del` elimina un elemento por su **índice**:

```python
frutas = ["manzana", "banana", "naranja", "uva"]

del frutas[1]
print(frutas)   # ['manzana', 'naranja', 'uva']

del frutas[0]
print(frutas)   # ['naranja', 'uva']
```

⚠️ Una vez eliminado con `del`, el elemento ya no está disponible.

```python
# También podés borrar toda la lista:
del frutas
# print(frutas)   # NameError: la variable ya no existe
```

---

## Eliminar elementos: slice vacío

Podés reemplazar una porción de la lista con una lista vacía para eliminar elementos:

```python
numeros = [1, 2, 3, 4, 5, 6]

numeros[2:4] = []    # elimina los elementos en posiciones 2 y 3
print(numeros)       # [1, 2, 5, 6]

numeros[1:3] = []    # elimina posiciones 1 y 2
print(numeros)       # [1, 6]
```

Esta técnica es útil cuando querés eliminar un rango de elementos de una vez.

---

## Slicing de listas

El **slicing** permite obtener una porción de la lista:

```python
letras = ["a", "b", "c", "d", "e"]

print(letras[1:4])   # ['b', 'c', 'd']  → desde 1, sin incluir 4
print(letras[2:])    # ['c', 'd', 'e']  → desde 2 hasta el final
print(letras[:3])    # ['a', 'b', 'c']  → desde el inicio hasta 3 (sin incluir)
print(letras[:])     # ['a', 'b', 'c', 'd', 'e']  → copia completa
```

La sintaxis es:
```python
lista[inicio:fin]    # fin no está incluido
```

---

## Slicing: más ejemplos

```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Con step (tercer parámetro)
print(numeros[::2])     # [0, 2, 4, 6, 8]  → de a 2
print(numeros[1::2])    # [1, 3, 5, 7, 9]  → impares
print(numeros[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  → invertida

# Combinando
print(numeros[2:8:2])   # [2, 4, 6]
```

El `[:]` hace una **copia** de la lista (no una referencia):

```python
original = [1, 2, 3]
copia = original[:]
copia[0] = 99
print(original)   # [1, 2, 3]  ← no cambió
print(copia)      # [99, 2, 3]
```

---

## Strings como listas

Un **String** es, en muchos sentidos, una lista de caracteres:

```python
nombre = "Python"

print(len(nombre))    # 6
print(nombre[0])      # P
print(nombre[1])      # y
print(nombre[-1])     # n

# Slicing también funciona
print(nombre[0:3])    # Pyt
print(nombre[::-1])   # nohtyP  (invertido)
```

Todo lo que aprendimos sobre índices y slicing aplica también a los strings.

---

## Strings vs Listas: diferencia clave

La gran diferencia: los strings son **inmutables**.

```python
frutas = ["manzana", "banana"]
frutas[0] = "uva"        # ✅ OK, las listas son mutables
print(frutas)            # ['uva', 'banana']

nombre = "Python"
nombre[0] = "J"          # ❌ TypeError: 'str' object does not support item assignment
```

Para "modificar" un string, hay que crear uno nuevo:

```python
nombre = "Python"
nuevo_nombre = "J" + nombre[1:]
print(nuevo_nombre)   # Jython
```

---


## Listas de listas

Una lista puede contener otras listas (**listas multidimensionales**):

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Para acceder a los elementos usamos **doble índice** `[fila][columna]`:

```python
print(matriz[0])       # [1, 2, 3]  → primera fila
print(matriz[0][0])    # 1          → fila 0, columna 0
print(matriz[1][2])    # 6          → fila 1, columna 2
print(matriz[2][1])    # 8          → fila 2, columna 1
```

---

## Resumen

| Operación | Sintaxis | Descripción |
|---|---|---|
| Crear lista | `lista = [a, b, c]` | Lista con elementos |
| Acceder | `lista[i]` | Elemento en posición i |
| Longitud | `len(lista)` | Cantidad de elementos |
| Modificar | `lista[i] = x` | Cambia elemento en posición i |
| Agregar al final | `lista.append(x)` | Agrega x al final |
| Insertar | `lista.insert(i, x)` | Inserta x en posición i |
| Eliminar | `del lista[i]` | Elimina elemento en posición i |
| Slice | `lista[a:b]` | Porción desde a hasta b (sin incluir) |
| Copia | `lista[:]` | Copia completa de la lista |
| String indexado | `string[i]` | Carácter en posición i (inmutable) |
| Lista de listas | `lista[i][j]` | Elemento fila i, columna j |
