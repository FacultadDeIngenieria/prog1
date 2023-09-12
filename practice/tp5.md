---
title: Práctica 5
layout: practice
permalink: /practice/5
---

# Trabajo Práctico 5

## Ejercicio 1 - Dias a horas

Implementar la función dias_a_horas, la cual tiene como parámetro un valor entero ( recomandamos de llamarlo `días`) y va a retornar el valor de horas correspondiente.
En caso de ser una cantidad de horas negativa, se debe retornar un string con un mensaje de error

Ejemplo: 
```python
horas_1 = dias_a_horas(5)
horas_2 = dias_a_horas(0)
horas_3 = dias_a_horas(-4)

print(horas_1) # Imprime: 120 horas
print(horas_2) # Imprime: 0 horas
print(horas_3) # Imprime: Número erróneo de días ingresados
```
## Ejercicio 2 - Dias a horas con fracciones 

Implementar la función dias_a_horas_con_fracciones, la cual tiene como parámetro un valor decimal ( es decir, float, recomandamos de llamarlo `días` al igual que en `dias_a_horas`) y va a retornar el valor de horas correspondiente.
En caso de ser una cantidad de horas negativa, se debe retornar un string con un mensaje de error

Ejemplo: 
```python
horas_1 = dias_a_horas_con_fracciones(5)
horas_2 = dias_a_horas_con_fracciones(2,5)
horas_3 = dias_a_horas_con_fracciones(0)
horas_4 = dias_a_horas_con_fracciones(-4)

print(horas_1) # Imprime: 120 horas
print(horas_2) # Imprime: 60 horas
print(horas_3) # Imprime: 0 horas
print(horas_4) # Imprime: Número erróneo de días ingresados
```


## Ejercicio 3 - Dias a horas con reutilización 

Implementar la función dias_a_horas_reutilizable, la cual tiene como parámetro un valor que puede ser entero o decimal ( recomandamos de llamarlo `días`) y va a retornar el valor de horas correspondiente.
En caso de ser una cantidad de horas negativa, se debe retornar un string con un mensaje de error

En este caso es requerido que dentro de la funcion `dias_a_horas_reutilizable` se haga uso de por lo menos una de las funciones de este trabajo práctico para obtener el resultado.

Ejemplo: 
```python
horas_1 = dias_a_horas_reutilizable(5)
horas_2 = dias_a_horas_reutilizable(2,5)
horas_3 = dias_a_horas_reutilizable(0)
horas_4 = dias_a_horas_reutilizable(-4)

print(horas_1) # Imprime: 120 horas
print(horas_2) # Imprime: 60 horas
print(horas_3) # Imprime: 0 horas
print(horas_4) # Imprime: Número erróneo de días ingresados
```


## Ejercicio 4 - Cálculo de los máximos

Para este ejercicio deberan implementar las funciones dadas para que cumplan con su objetivo. Para saber como implementar cada metodo, deberan leer el python-doc.

```python
def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    return "ANSWER HERE" # Remove this line and implement

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    return "ANSWER HERE" # Remove this line and implement
```

Ejemplo: 
```python
max_1 = max_of_two(5,4)
max_2 = max_of_two(-2,-3)
max_3 = max_of_two(0,0)

print(max_1) # Imprime: 5
print(max_2) # Imprime: -2
print(max_3) # Imprime: 0

max_4 = max_of_three(5,4,7)
max_5 = max_of_three(-2,-3,-1)
max_6 = max_of_three(0,0,0)

print(max_4) # Imprime: 7
print(max_5) # Imprime: -1
print(max_6) # Imprime: 0
```

## Ejercicio 5 - Concatenar strings
Para este ejercicio se debe implementar la función `concatenar_strings` la cuál debe recibir como parámetros dos strings ( recomendamos llamarlos `string_1` y `string_2`)  
Y debe retornar la concatenación de ambos strings separados por un espacio

## Ejercicio 6- Área rectángulo 
Para este ejercicio se debe implementar la función `calcular_area` la cuál debe recibir como parámetros dos valores numéricos que pueden ser int o float, el primero indicando la medida de la base del rectángulo y el segundo representando la medida de la altura del rectángulo. Se debe retornar el cálculo del área del rectángulo que representan. 
Ejemplo: 
```python
area_1 = calcular_area(5,4)
area_2 = calcular_area(3,-3)
area_3 = calcular_area(0,20)

print(area_1) # Imprime: 20
print(area_2) # Imprime: El área del rectángulo no puede ser negativa
print(area_3) # Imprime: 0
```

## Ejercicio 7 - Perímetro rectángulo 
Para este ejercicio se debe implementar la función `calcular_perimetro` la cuál debe recibir como parámetros dos valores numéricos que pueden ser int o float, el primero indicando la medida de la base del rectángulo y el segundo representando la medida de la altura del rectángulo. Se debe retornar el cálculo del perímetro del rectángulo que representan. 
Ejemplo: 
```python
permietro_1 = calcular_perimetro(5,4)
permietro_2 = calcular_perimetro(3,-3)
permietro_3 = calcular_perimetro(0,20)

print(permietro_1) # Imprime: 18
print(permietro_2) # Imprime: El perímetro del rectángulo no puede ser negativo
print(permietro_3) # Imprime: 0
```


## Ejercicio 8 - Información del rectángulo 
Para este ejercicio se debe implementar la función `informancion_del_rectangulo` la cual debe imprimir en pantalla la información del área y el perímetro del rectaculo.
Para lograr eso es necesario reutilizar las funciones creadas en los ejercicios anteriores

Ejemplo: 
```python
informacion_rectangulo(5,4)
# Imprime:
Rectángulo con base 5 y altura 4:
Área: 20
Perímetro: 18
```

## Ejercicio 9 - Invertir la oración 
Para este ejercicio se debe implementar la función `invertir_string` la cuál recibe como parámetro un string y el cual se debe retornar de la función pero con todos sus caracteres de atrás hacía adelente.

## Ejercicio  10 - Es par 

Para este ejercicio se debe implementar la función `es_par` que tome un número como argumento y devuelva True si el número es par y False si no lo es.
Ejemplo: 
```python
par_1 = es_par(4)
par_2 = es_par(5)
print(par_1) # Imprime: True
print(par_2) # Imprime: False
```

## Ejercicio  11 - Es palindromo 
Para este ejercicio se debe implementar la función `es_palindromo` que tome un string como argumento y retorne True si el string es un palíndromo y False si no lo es.


Ejemplo:
```python
print(es_palindromo("radar"))    # Imprime: True
print(es_palindromo("python"))   # Imprime: False
print(es_palindromo("reconocer")) # Imprime: True
```

## Ejercicio 12 - Calificar estudiante
Para este ejercicio se debe implementar la función `calificar_estudiante` que tome la puntuación de un estudiante en un examen (un valor entre 0 y 100) como argumento y devuelva la calificación correspondiente en forma de letra según la siguiente escala:

Puntuación de 90 o más: "A"
Puntuación de 80 a 89: "B"
Puntuación de 70 a 79: "C"
Puntuación de 60 a 69: "D"
Puntuación por debajo de 60: "F"


Ejemplo:
```python
print(calificar_estudiante(95))  # Imprime: A
print(calificar_estudiante(82))  # Imprime: B
print(calificar_estudiante(70))  # Imprime: C
print(calificar_estudiante(65))  # Imprime: D
print(calificar_estudiante(45))  # Imprime: F
```

## Ejercicio  13 - Verificar positividad 
Para este ejercicio se debe implementar la función `verificar_positividad` que recibe como parámetro un número y retorna información sobre si este número es positivo, negativo o cero.

Ejemplo:
```python
print(verificar_numero(5))   # Imprime: El número 5 es positivo.
print(verificar_numero(-3))  # Imprime: El número -3 es negativo.
print(verificar_numero(0))   # Imprime: El número es cero.
```

## Ejercicio 14 - Months

Para este ejercicio se debe implementar la función `number_to_month` que dado un numero entre el 1 y el 12, retorne el nombre del mes que representa en el calendario.
Si el numero no esta entre el rango 1 y 12, se debera retornar la palabra "error".

```python
def number_to_month(month):
    return "ANSWER HERE" # Remove this line and implement
```

Todos los meses deberan ser en minuscula.

Ejemplo:
```python
print(number_to_month(1)) # Imprime: "enero"
print(number_to_month(99)) # Imprime: "error"
```

## Ejercicio 15 - Quadratic

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
![cuadratic]({{site.baseurl}}/practice/tp5.png)
