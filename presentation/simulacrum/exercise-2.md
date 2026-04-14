class: center, middle, inverse

# **Ejercicio 2 - Manipulacion de Listas y Slicing**

---

## Enunciado

Escribir una funcion `shuffle_list` que reciba una lista de **exactamente 6 elementos** y devuelva una nueva lista:

- El primer elemento de la nueva lista debe ser el ultimo de la original.
- Los elementos en la posicion central (indices 2 y 3) deben estar invertidos.
- El resto de los elementos deben ser los mismos que en la lista original.
- Si la lista no tiene 6 elementos, debe devolver una lista vacia y mostrar: `"Lista no valida"`.

**Sin usar loops.**

---

## Analisis

Lista original de 6 elementos con indices 0 a 5:

```
Indice:    0    1    2    3    4    5
```

Reglas:
- Posicion 0 de la nueva → ultimo de la original (`lst[5]`)
- Posiciones 2 y 3 → invertidas (`lst[3]` y `lst[2]`)
- Posicion 5 de la nueva → primero de la original (`lst[0]`)
- El resto (posiciones 1 y 4) → se mantienen

---

## Mapeo de indices

```
Nueva lista:
Posicion 0 → lst[5]   (primero = ultimo de original)
Posicion 1 → lst[1]   (se mantiene)
Posicion 2 → lst[3]   (central invertido)
Posicion 3 → lst[2]   (central invertido)
Posicion 4 → lst[4]   (se mantiene)
Posicion 5 → lst[0]   (ultimo = primero de original)
```

---

## Solucion

```python
def shuffle_list(lst):
    if len(lst) != 6:
        print("Lista no valida")
        return []
    return [lst[5], lst[1], lst[3], lst[2], lst[4], lst[0]]
```

---

## Ejemplo

```python
lista = [10, 20, 30, 40, 50, 60]
print(shuffle_list(lista))
```

```
Posicion 0 → lst[5] = 60
Posicion 1 → lst[1] = 20
Posicion 2 → lst[3] = 40
Posicion 3 → lst[2] = 30
Posicion 4 → lst[4] = 50
Posicion 5 → lst[0] = 10
```

**Resultado:** `[60, 20, 40, 30, 50, 10]`

---

## Caso invalido

```python
print(shuffle_list([1, 2, 3]))
```

**Imprime:** `Lista no valida`

**Retorna:** `[]`

---

class: center, middle, inverse

[Volver a las respuestas](/simulacrum-answers)
