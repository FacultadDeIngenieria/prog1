---
title: Práctica 5
layout: practice
permalink: /practice/5
---

# Trabajo Práctico 5

Debe entregarse en 15 días, luego del parcial.

## Ejercicio 1

En este ejercicio deberán usar las variables que vienen dadas:
```
lastName = 'Longo'
name = 'Juan'
```

Y con ellas lograr imprimir el siguiente output:
```
El apellido Longo comienza con una letra que esta antes de la M
La clave generada es: LonJua
```
## Ejercicio 2

En este ejercicio deberán implementar todos los métodos descritos a continuación:

Escribir un método llamado **removeElements** que dado una lista retorne una lista después de haber removido el primer, el quinto y el sexto elemento.

```
Sample Input : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
```

Escribir un método llamado **addElements** que dado una lista retorne una lista después de 
haber agregado el elemento 'Pink' al principio de la lista y el elemento 'Yellow' al final de la lista.

```
Sample Input : ['Red', 'Green', 'White', 'Black']
Expected Output : ['Pink', 'Red', 'Green', 'White', 'Black', 'Yellow']
```

Escribir un método llamado **isEmpty** que diga si una lista esta vacía o no.

Escribir un método llamado **checkLists** que dado dos listas retorne True si ambas listas contienen el mismo 3er elemento.

```
Sample List1 : ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
Sample List2 : ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
Expected Output : True

Sample List1 : ['Black', 'Pink', 'Green', 'White']
Sample List2 : ['Red', 'Green', 'Yellow', 'Black', 'Pink']
Expected Output : False
```

Escribir un método llamado **listOfLists** que dado una lista de listas, la modifique en la siguiente manera y la retorne:

De la primera lista solo se quede con los primeros 2 elementos.
De la segunda lista solo se quede con los elementos entre el segundo y cuarto elemento.
De la tercera lista solo se quede con los últimos 2 elementos.

```
Sample List: [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
Sample Output: [[1, 2], [5, 6, 7], [11, 12]]
```
