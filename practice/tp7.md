---
title: Práctica 7
layout: practice
permalink: /practice/7
---

# Trabajo Práctico 7

## Ejercicio 1


En este ejercicio deberán usar las variables que vienen dadas:
```
last_name = 'Longo'
first_name = 'Juan'
```

Y con ellas lograr retornar los siguientes datos para las funciones dadas:

Para la función `last_name_first_letter` retornar si el apellido comienza con una letra anterior, posterior o igual a la M
```
El apellido Longo comienza con una letra que está antes de la M
```
Para la función `name_key` retornar una clave compuesta por las 3 primeras letras del apellido seguido del nombre sin la última letra
```
La clave generada es: LonJua
```


Recordar que las funciones deben funcionar también para otros valores que no sean los del ejemplo. 
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
