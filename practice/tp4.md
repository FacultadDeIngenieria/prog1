---
title: Práctica 4
layout: practice
permalink: /practice/4
---

# Trabajo Práctico 4

## Ejercicio 1 - Comparación de booleans

Teniendo las 3 siguientes variables con valores booleanos se quiere realizar las comparaciones entre las mismas y saber si son iguales o no. 

Ejemplo: 
```
a = True
b = False
c = False
```
Imprime lo siguiente como resultado:
```
El valor de a es True
El valor de b es False
El valor de c es False

El valor de a y el valor de b son iguales: False
El valor de b y el valor de c son iguales: True
El valor de a y el valor de c son iguales: False

El valor de a y el valor de b son distintos: True
El valor de b y el valor de c son distintos: False
```
************************************************** 

## Ejercicio 2 - Comparación de números

Teniendo las 3 siguientes variables con valores numéricos se quiere realizar las comparaciones entre las mismas y saber cuál es el mayor y cual es el menor de los 3 números. 

Ejemplo: 
```
a = 4
b = -5
c = 2
```
Imprime lo siguiente como resultado:
```
El número mayor es: 4
El número menor es: -5
```
************************************************** 

## Ejercicio 3 - Costo de entradas del parque

Dados los siguientes costos para las entradas del parque de diversiones, se quiere saber cuanto deberá pagar un adolescente con su abuelo. 

```
Costos:
Niños hasta 4 años: $0 ( entrada gratis )
De 5 a 17 años: $50
De 18 a 50 años: $30
De 50 años en adelante: $10
```
Ejemplo: 
```
edad_adolescente = 14
edad_anciano = 66
```
Imprime lo siguiente como resultado:
```
El costo de entrada para el grupo familiar es de: $60
```
************************************************** 

## Ejercicio 4 - Comparación de strings

Dados los siguientes días de la semanana, verificar que sean dias laborables o de fin de semana  
Se debe usar por lo menos un `or` o `and` para resolverlo

Ejemplo: 
```
dia_1 = "Martes"
dia_2 = "Domingo"
dia_3 = "Octodia"
```

Imprime lo siguiente como resultado:
```
El día Martes es un día laborable
El día Domingo es un día de fin de semana
El día Octodia no es válido
```
************************************************** 

## Ejercicio 5 - Line

Queremos hacer un programa que nos calcule para una ecuación de primer grado la distancia sobre la recta entre dos 
coordenadas cualquiera del eje X y además me informe de las coordenadas del eje Y a la que corresponde.

Ejemplo: 
```
Ingrese el coeficiente A: 2.3
Ingrese el coeficiente B: -4
Ingrese el coeficiente X1: 50
Ingrese el coeficiente X2: -32.9
El coeficiente A de su ecuación de la recta es: 2.3
El coeficiente B de su ecuación de la recta es: -4.0
El coeficiente X1 de su ecuación de la recta es: 50.0
El coeficiente X2 de su ecuación de la recta es: -32.9

Para la siguiente ecuación:
	Y = 2.3X + -4.0

Dados los siguientes puntos:
	P1 (50.0, 110.99999999999999)
	P2 (-32.9, -79.66999999999999)

La distancia entre ellos es: 207.9121422620622
```
************************************************** 


HINT: [Formula de la distancia](https://es.wikipedia.org/wiki/Distancia#Distancia_de_dos_puntos_en_el_plano)

HINT: [Python Math doc](https://www.w3schools.com/python/module_math.asp)

## Ejercicio 6 - Leap Year

Un año no tiene en realidad 365 días, sino 365.242199. A fin de mantener el calendario en fase con los equinoccios y los solsticios, Julio César adoptó un sistema que añade un día adicional a cada cuatro años, que se conoce como año bisiesto. No obstante, este sistema no tenía la suficiente precisión, por lo que el Papa Gregorio XIII decretó, en 1582, un nuevo sistema calendario, según el cual un año divisible entre cuatro es bisiesto a menos que sea un año centenario, en cuyo caso sólo es bisiesto si es divisible por 400. Escribir una función que informa si un año dado es bisiesto.

Hacer un programa que dado un año me indique si es bisiesto útilizando al menos un comparador `or` o `and`. 

Ejemplos:
```
Ingrese un año: 2000
El año 2000 es bisiesto
```
```
Ingrese un año: 2001
El año 2001 no es bisiesto
```
