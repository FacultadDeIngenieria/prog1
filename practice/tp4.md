---
title: Práctica 4
layout: practice
permalink: /practice/4
---

# Trabajo Práctico 4

Debe entregarse a la semana siguiente de ser entregado.

## Ejercicio 1

Para este ejercicio deberan implementar las funciones dadas para que cumplan con su objetivo. Para saber como implementar cada metodo, deberan leer el python-doc.

```python
def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    return "ANSWER HERE" # Remove this line and implement

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    return "ANSWER HERE" # Remove this line and implement
```

## Ejercicio 2 - Months

Hacer un metodo llamado *numberToMonth* que dado un numero entre el 1 y el 12, devuelva el nombre del mes que representa en el calendario. Si el numero no esta entre el rango 1 y 12, se debera retornar la palabra "error".

```python
def numberToMonth(month):
    return "ANSWER HERE" # Remove this line and implement
```

Ejemplo:

Dado el input 1 el resultado debera ser "enero"
Dado el input 99 el resultado debera ser "error"
Todos los meses deberan ser en minuscula.

## Ejercicio 3 - Quadratic

Completar, definir e implementar los métodos necesarios para resolver una ecuación cuadrática de 2º grado. Para ello, lo que deberan hacer es crear todos los siguentes métodos:

* Dado los parámetros (a, b, c) el método roots devolverá un String de la forma (r1, r2) o (r12) o ( ) según sea el caso de que tenga dos raíces, una raíz o ninguna.
* Dado los parámetros (a, b, c, x) el método valueY devolverá el valor de Y para un valor de X que se le pasa como parámetro.
* Dado los parámetros (a, b, c) el método toString que devolverá un String mostrando la ecuación como figura en el primer párrafo (Y = A * X2 + B * X + C).
* Dado los parámetros (a, b) el método derivation que devolverá un String mostrando la función lineal derivada.

```python
# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    return "ANSWER HERE"

def valueY(a, b, c, x):
    return "ANSWER HERE"

def toString(a, b, c):
    return "ANSWER HERE"

def derivation(a, b):
    return "ANSWER HERE"
```

HINT: Para resolver una cuadrática:
![cuadratic]({{site.baseurl}}/practice/tp4.png)