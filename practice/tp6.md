---
title: Práctica 6
layout: practice
permalink: /practice/6
---

# Trabajo Práctico 6

## Ejercicio 1 - Loops and prints

Dada la siguiente consigna, implementar y lograr imprimir en pantalla el output esperado.

Para la primera parte, hacer una función llamada **printList** que dada una lista de Strings los muestre por pantalla uno por renglón con su número de índice, un punto, un tabulado (\t) y el valor String. Si el arreglo tiene strings vacíos no debe mostrar nada, ni el renglón correspondiente.

```python
colors = ["Red", "Green", "", "White", "Black"]
printList(colors)
#imprime:
# 0.  Red
# 1.  Green
# 2.  White
# 3.  Black
```

Para la segunda parte, hacer un método llamado **printBackwards** que dado una lista de strings lo muestre por pantalla uno por renglón al igual que en la primera parte, pero la palabra deberia ser impresa al reves. Si el arreglo tiene strings vacíos no debe mostrar nada, ni el renglón correspondiente.

```python
colors = ["Red", "Green", "", "White", "Black"]
printBackwards(colors)
#imprime:
# 0. deR
# 1. neerG
# 2. etihW
# 3. kcalB
```


## Ejercicio 2

Dado la siguiente consigna, implementar las siguientes funciones:
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