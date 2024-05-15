---
title: Práctica 7
layout: practice
permalink: /practice/7
---

# Trabajo Práctico 7

## Completar el trabajo práctico en GitHub Classroom
[Link al TP 7](https://classroom.github.com/a/P4awoBvK)

## Ejercicio 1 - Loops and prints

Dada la siguiente consigna, implementar y lograr imprimir en pantalla el output esperado.

Para la primera parte, hacer una función llamada **enumerate_list** que dada una lista de Strings, retorne una nueva lista y en cada elemento agregar su número de índice, un punto, un espacio y el valor String. Si el arreglo tiene strings vacíos no debe mostrar nada, ni el elemento correspondiente en la lista.

```python
colors = ["Red", "Green", "", "White", "Black"]
enumerate_list(colors)
#retorna la lista:
# ["0. Red", "1. Green", "2. White", "3. Black"]
```

Para la segunda parte, hacer un método llamado **enumerate_backwards** que dado una lista de Strings, returne una nueva lista, al igual que en enumerate_list, pero cada palabra deberia estas escrita a la inversa. Si el arreglo tiene Strings vacíos se deben saltear esos elementos de la nueva lista.

```python
colors = ["Red", "Green", "", "White", "Black"]
enumerate_backwards(colors)
#retorna la lista:
# ["0. deR", "1. neerG", "2. etihW", "3. kcalB"]  
```


## Ejercicio 2

Dado la siguiente consigna, implementar las siguientes funciones:
* Método **index_of** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings. En caso 
  de no encontrarse ninguna retorna el valor -1.

```python
colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(index_of("Black", colors))
#imprime: 3
print(index_of("Blue", colors))
#imprime: -1
```
  
* Método **index_of_by_index** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings, a partir 
  de un índice dado, incluido en la búsqueda. En caso de no encontrarse ninguna coincidencia retorna el valor -1.

```python
colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(index_of_by_index("Black", colors, 1))
#imprime: 3
print(index_of_by_index("Black", colors, 4))
#imprime: 6
print(index_of_by_index("Green", colors, 2))
#imprime: -1
```
  
* Método **index_of_empty** que retorne el índice del primer lugar “vacío” (igual a "") en una lista de Strings. De no encontrar ninguno que retorne -1.

```python
colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(index_of_empty(colors))
#imprime: -1

colors = ["Red", "Green", "", "", "Pink", "", "Black"]
print(index_of_empty(colors))
#imprime: 2
```

* Método **put**, que dado un String y una lista de Strings lo coloque en el primer lugar vacío (igual a "") que encuentre y retorne 
  el índice en donde lo colocó. De no haber ningún lugar vacío debe retornar -1.

```python
colors = ["Red", "Green", "", "", "Pink", "", "Black"]
print(put("Blue", colors))
#imprime: 2

colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(put("Blue", colors))
#imprime: -1
```

* Método **remove** que dado un String y una lista de Strings, busque el string, lo elimine si lo encuentra (lo cambia a "") y 
  retorne el número de eliminaciones que ha hecho.


```python
colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(remove("Black", colors))
#imprime: 2
print(remove("Blue", colors))
#imprime: 0
```
