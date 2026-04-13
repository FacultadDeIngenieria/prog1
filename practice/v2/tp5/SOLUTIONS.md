# Soluciones TP5 - Listas

Este archivo contiene las soluciones de referencia para todos los ejercicios del TP5.

---

## Ejercicio 1 - `exercise_list_length.py`

**Objetivo:** Obtener la longitud de una lista.

**Solución:**
```python
def list_length(lista):
    return len(lista)
```

**Conceptos:**
- Función `len()` built-in de Python
- Funciona con cualquier tipo de lista

---

## Ejercicio 2 - `exercise_get_element.py`

**Objetivo:** Obtener elemento en posición específica con validación.

**Solución:**
```python
def get_element(lista, indice):
    # Validar que el índice esté dentro del rango válido
    # Para índices positivos: 0 <= indice < len(lista)
    # Para índices negativos: -len(lista) <= indice < 0
    if len(lista) > 0 and -len(lista) <= indice < len(lista):
        return lista[indice]
    return None
```

**Conceptos:**
- Validación de índices positivos y negativos
- Operadores de comparación encadenados
- Retorno de `None` para casos inválidos

**Alternativa con try/except (más avanzada):**
```python
def get_element(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return None
```

---

## Ejercicio 3 - `exercise_add_elements.py`

**Objetivo:** Agregar elementos al principio y final.

**Solución:**
```python
def add_elements(lista):
    lista.insert(0, 'Pink')
    lista.append('Yellow')
    return lista
```

**Conceptos:**
- `insert(posicion, elemento)` - Inserta en posición específica
- `append(elemento)` - Agrega al final
- Modifica la lista original

---

## Ejercicio 4 - `exercise_remove_elements.py`

**Objetivo:** Remover elementos en posiciones específicas (1º, 5º, 6º).

**Solución:**
```python
def remove_elements(lista):
    # Remover en orden inverso para no afectar los índices
    # Primero el sexto (índice 5), luego el quinto (índice 4), finalmente el primero (índice 0)
    if len(lista) > 5:
        lista.pop(5)
    if len(lista) > 4:
        lista.pop(4)
    if len(lista) > 0:
        lista.pop(0)
    return lista
```

**Conceptos:**
- `pop(indice)` - Remueve y retorna elemento en posición
- **Importante:** Remover en orden inverso para mantener índices válidos
- Validar longitud antes de cada operación

**¿Por qué orden inverso?**
```
Lista inicial: ['A', 'B', 'C', 'D', 'E', 'F']
                 0    1    2    3    4    5

Si removemos el primero (0) primero:
['B', 'C', 'D', 'E', 'F']  <- Ahora el índice 5 ya no existe!
  0    1    2    3    4

Por eso removemos del final hacia el inicio:
1. Remover índice 5: ['A', 'B', 'C', 'D', 'E']
2. Remover índice 4: ['A', 'B', 'C', 'D']
3. Remover índice 0: ['B', 'C', 'D']
```

---

## Ejercicio 5 - `exercise_find_max.py`

**Objetivo:** Encontrar el valor máximo en una lista.

**Solución:**
```python
def find_max(lista):
    if len(lista) == 0:
        return None
    return max(lista)
```

**Conceptos:**
- `max(lista)` - Función built-in para encontrar máximo
- Validar lista vacía antes de usar `max()`
- `max()` genera error si la lista está vacía

---

## Ejercicio 6 - `exercise_find_min.py`

**Objetivo:** Encontrar el valor mínimo en una lista.

**Solución:**
```python
def find_min(lista):
    if len(lista) == 0:
        return None
    return min(lista)
```

**Conceptos:**
- `min(lista)` - Función built-in para encontrar mínimo
- Validar lista vacía antes de usar `min()`
- Mismo patrón que `find_max`

---

## Ejercicio 7 - `exercise_count_occurrences.py`

**Objetivo:** Contar cuántas veces aparece un elemento.

**Solución:**
```python
def count_occurrences(lista, elemento):
    return lista.count(elemento)
```

**Conceptos:**
- `.count(elemento)` - Método de lista que cuenta ocurrencias
- Retorna 0 si el elemento no está presente
- Funciona con cualquier tipo de elemento

---

## Ejercicio 8 - `exercise_reverse_list.py`

**Objetivo:** Invertir una lista sin modificar la original.

**Solución:**
```python
def reverse_list(lista):
    return lista[::-1]
```

**Conceptos:**
- Slicing con paso negativo `[::-1]`
- Crea una nueva lista (no modifica la original)
- Forma pythonica y eficiente

**Alternativas:**
```python
# Alternativa 1: con reversed()
def reverse_list(lista):
    return list(reversed(lista))

# Alternativa 2: con .reverse() (modifica original)
def reverse_list(lista):
    lista_copia = lista.copy()
    lista_copia.reverse()
    return lista_copia
```

---

## Ejercicio 9 - `exercise_is_empty.py`

**Objetivo:** Verificar si una lista está vacía.

**Solución:**
```python
def is_empty(lista):
    return len(lista) == 0
```

**Conceptos:**
- Comparación de longitud con 0
- Retorna booleano
- Simple y directo

**Alternativa pythonica:**
```python
def is_empty(lista):
    return not lista  # Lista vacía es False en contexto booleano
```

---

## Ejercicio 10 - `exercise_concatenate_lists.py`

**Objetivo:** Concatenar dos listas en una sola.

**Solución:**
```python
def concatenate_lists(lista1, lista2):
    return lista1 + lista2
```

**Conceptos:**
- Operador `+` para concatenar listas
- Crea una nueva lista
- No modifica las listas originales

**Alternativa con extend:**
```python
def concatenate_lists(lista1, lista2):
    resultado = lista1.copy()
    resultado.extend(lista2)
    return resultado
```

---

## Ejercicio 11 - `exercise_check_lists.py`

**Objetivo:** Comparar el tercer elemento de dos listas.

**Solución:**
```python
def check_lists(lista1, lista2):
    if len(lista1) < 3 or len(lista2) < 3:
        return False
    return lista1[2] == lista2[2]
```

**Conceptos:**
- Validación de longitud antes de acceder
- Acceso por índice `[2]` para el tercer elemento
- Operador lógico `or`
- Comparación de elementos

---

## Ejercicio 12 - `exercise_list_of_lists.py`

**Objetivo:** Manipular listas anidadas con slicing.

**Solución:**
```python
def list_of_lists(lista_de_listas):
    # Primera lista: primeros 2 elementos (índices 0 y 1)
    lista_de_listas[0] = lista_de_listas[0][:2]

    # Segunda lista: elementos del índice 1 al 3 (inclusive)
    lista_de_listas[1] = lista_de_listas[1][1:4]

    # Tercera lista: últimos 2 elementos
    lista_de_listas[2] = lista_de_listas[2][-2:]

    return lista_de_listas
```

**Conceptos:**
- Slicing con inicio y fin `[inicio:fin]`
- Índices negativos `[-2:]` para últimos elementos
- Modificación de listas anidadas
- El slicing funciona bien con listas más cortas (no genera error)

**Explicación del slicing:**
```python
lista = [1, 2, 3, 4, 5]

# Primeros 2 elementos
lista[:2]   # [1, 2]

# Del índice 1 al 3 (inclusive)
lista[1:4]  # [2, 3, 4]

# Últimos 2 elementos
lista[-2:]  # [4, 5]
```


---

## Tips y Buenas Prácticas

1. **Validar antes de acceder:**
   ```python
   # ✓ Correcto
   if len(lista) > 0:
       elemento = lista[0]

   # ✗ Puede fallar
   elemento = lista[0]  # IndexError si está vacía
   ```

2. **Remover en orden inverso:**
   ```python
   # ✓ Correcto - de mayor a menor índice
   lista.pop(5)
   lista.pop(4)
   lista.pop(0)

   # ✗ Incorrecto - los índices cambian
   lista.pop(0)
   lista.pop(4)  # Este índice ya no es el mismo!
   lista.pop(5)
   ```

3. **Slicing es seguro con listas cortas:**
   ```python
   lista = [1, 2]
   lista[:5]   # [1, 2] - No genera error
   lista[5]    # IndexError!
   ```

4. **Índices negativos:**
   ```python
   lista = [1, 2, 3, 4, 5]
   lista[-1]   # 5 (último)
   lista[-2]   # 4 (penúltimo)
   lista[-2:]  # [4, 5] (últimos 2)
   ```

5. **Modificar vs Crear nueva:**
   ```python
   # Modificar original
   lista.append(4)
   lista.reverse()

   # Crear nueva
   nueva = lista + [4]
   nueva = lista[::-1]
   ```
