---
title: Práctica 7
layout: practice
permalink: /practice/7
---

# Trabajo Práctico 7

Dado la siguiente consigna, implementar las siguientes funciones TODAS USANDO RECURSIVIDAD (Eso significa, sin usar for o while):

* Método **indexOf** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings. En caso 
  de no encontrarse ninguna retorna el valor -1.

```python
colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(indexOf("Black", colors))
#imprime: 3
print(indexOf("Blue", colors))
#imprime: -1
```
  
* Método **indexOfByIndex** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings, a partir 
  de un índice dado, incluido en la búsqueda. En caso de no encontrarse ninguna coincidencia retorna el valor -1.

```python
colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(indexOfByIndex("Black", colors, 1))
#imprime: 3
print(indexOfByIndex("Black", colors, 4))
#imprime: 6
print(indexOfByIndex("Green", colors, 2))
#imprime: -1
```
  
* Método **indexOfEmpty** que retorne el índice del primer lugar “vacío” (igual a "") en una lista de Strings. De no encontrar ninguno que retorne -1.

```python
colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(indexOfEmpty(colors))
#imprime: -1

colors = ["Red", "Green", "", "", "Pink", "", "Black"]
print(indexOfEmpty(colors))
#imprime: 2
```

* Método **put**, que dado un String y una lista de Strings lo coloque en el primer lugar vacío que encuentre y retorne 
  el índice en donde lo colocó. De no haber ningún lugar vacío debe retornar -1.

```python
colors = ["Red", "Green", "", "", "Pink", "", "Black"]
print(put("Blue", colors))
#imprime: 2

colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(put("Blue", colors))
#imprime: -1
```

* Método **remove** que dado un String y una lista de Strings, busque el string, lo elimine si lo encuentra y 
  retorne el número de eliminaciones que ha hecho.


```python
colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(remove("Black", colors))
#imprime: 2
print(remove("Blue", colors))
#imprime: 0
```
