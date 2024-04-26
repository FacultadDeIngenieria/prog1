---
title: Ejercicios adicionales 1.er parcial
layout: practice
permalink: /additional-practice/1
---

# Práctica adicional 1.er parcial

## 1 - Strings

## Ejercicio 1.1 - Uso del "not in"

Ingresar una oración usando input y verificar que no contenga ninguna letra con tilde
Considerar que la letra puede ser mayuscula o minuscula.

Ayuda: los caracteres de las letras con tilde son distintos que los caracteres de las letras sin tildes
( por ejemplo, la letra `á` es un carácter distinto que la letra `a`)

Ejemplo: 
```
> La contraseña no es válida
No contiene á: False
No contiene é: True
No contiene í: True
No contiene ó: True
No contiene ú: True

> A la grande le puse cuca
No contiene á: True
No contiene é: True
No contiene í: True
No contiene ó: True
No contiene ú: True
```

**************************************************


## Ejercicio 1.2 - Uso del "slice" con un carácter

Obtener los siguientes datos del texto de ejemplo:
* Primera letra ( usando índices positivos )
* Última  ( usando índices positivos )
* Anteúltima letra ( usando índices negativos )
* Primera letra ( usando índices negativos )

Es necesario que todos los caracteres se impriman en minúscula

Ejemplo: 
```
> texto = "Hello, World!"
>  * código a implementar *
h
!
d
h
```

************************************************** 
## Ejercicio 1.3 - Uso del "slice" con orden inverso
Imprimir la palabra completa en orden inverso, es decir, dada vuelta.

Ejemplo: 
```
> texto = "Hello, World!"
>  * código a implementar *
!dlroW ,olleH
```

************************************************** 
# Ejercicio 1.4 - Uso del "slice" cada n caracteres.
Imprimir el resultado de obtener los valores de la palabra saltando de a 3 caracteres

Ejemplo: 
```
> texto = "Hello, World!"
>  * código a implementar *
Hl r!

> texto2 = "12345678910"
>  * código a implementar *
1471
```


************************************************** 
## Ejercicio 1.5 - Uso del "slice" validando que la palabra obtenida está contenida en otro string
Se debe obtener del texto dado sus primeros 2 caracteres y concatenarlos con lo últimos 3.
Con este string obtenido se debe validar que el mismo se encuentre o no dentro de la lista de gases nobles.

Considerar que las palabras pueden tener algunos caracteres en mayúscula.
Al momento de realizar la validación se debe utilizar todo en minúscula

Ejemplo: 
```
> gases_nobles = "Helio, Neón, Argón, Kriptón, Xenón, Radón, Oganesón"
> texto = "Hello, Aurelio"
>  * código a implementar *
La palabra se encuentra dentro de los gases nobles: True

> gases_nobles = "Helio, Neón, Argón, Kriptón, Xenón, Radón, Oganesón"
> texto2 = "Hello, Matías"
>  * código a implementar *
La palabra se encuentra dentro de los gases nobles: False
```

************************************************** 
## Ejercicio 1.6 - Modificaciones de los strings
Cambiar el nombre de la persona que aparece en la oración por tu nombre

Ejemplo: 
```
> texto = "Hello, Gastón!"
>  * código a implementar *
Hello, Matías!

```

************************************************** 
## Ejercicio 1.7 - Modificaciones de los strings.
Modificar el string para que se le sume un año a la edad. 
Considerar que la edad va a tener siempre 2 caracteres. 

Ejemplo: 
```
> texto = "Carlos tiene 19 años"
>  * código a implementar *
Carlos tiene 20 años!

> texto2 = "Felipe tiene 22 años"
>  * código a implementar *
Felipe tiene 23 años!

```
************************************************** 

## 2 - Condicionales


## Ejercicio 2.1 - Comparación de booleans

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

## Ejercicio 2.2 - Comparación de números

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

## Ejercicio 2.3 - Costo de entradas del parque

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

## Ejercicio 2.4 - Comparación de strings

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

## 3 - Funciones


## Ejercicio 3.1 - Dias a horas

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
## Ejercicio 3.2 - Dias a horas con fracciones 

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


## Ejercicio 3.3 - Dias a horas con reutilización 

Implementar la función dias_a_horas_reutilizable, la cual tiene como parámetro un valor que puede ser entero o decimal ( recomandamos de llamarlo `días`) y va a retornar el valor de horas correspondiente.
En caso de ser una cantidad de horas negativa, se debe retornar un string con un mensaje de error

En este caso es requerido que dentro de la funcion `dias_a_horas_reutilizable` se haga uso de por lo menos una de las funciones de este trabajo práctico para obtener el resultado.

Ejemplo: 
```python
horas_1 = dias_a_horas_reutilizable(5)
horas_2 = dias_a_horas_reutilizable(2.5)
horas_3 = dias_a_horas_reutilizable(0)
horas_4 = dias_a_horas_reutilizable(-4)

print(horas_1) # Imprime: 120 horas
print(horas_2) # Imprime: 60 horas
print(horas_3) # Imprime: 0 horas
print(horas_4) # Imprime: Número erróneo de días ingresados
```



## Ejercicio 3.4 - Concatenar strings
Para este ejercicio se debe implementar la función `concatenar_strings` la cuál debe recibir como parámetros dos strings ( recomendamos llamarlos `string_1` y `string_2`)  
Y debe retornar la concatenación de ambos strings separados por un espacio

## Ejercicio 3.5- Área rectángulo 
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

## Ejercicio 3.6 - Perímetro rectángulo 
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


## Ejercicio 3.7 - Información del rectángulo 
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

## Ejercicio 3.8 - Invertir la oración 
Para este ejercicio se debe implementar la función `invertir_string` la cuál recibe como parámetro un string y el cual se debe retornar de la función pero con todos sus caracteres de atrás hacía adelente.

## Ejercicio 3.9 - Es par 

Para este ejercicio se debe implementar la función `es_par` que tome un número como argumento y devuelva True si el número es par y False si no lo es.
Ejemplo: 
```python
par_1 = es_par(4)
par_2 = es_par(5)
print(par_1) # Imprime: True
print(par_2) # Imprime: False
```

## Ejercicio 3.10 - Es palindromo 
Para este ejercicio se debe implementar la función `es_palindromo` que tome un string como argumento y retorne True si el string es un palíndromo y False si no lo es.


Ejemplo:
```python
print(es_palindromo("radar"))    # Imprime: True
print(es_palindromo("python"))   # Imprime: False
print(es_palindromo("reconocer")) # Imprime: True
```

## Ejercicio 3.11 - Calificar estudiante
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

## Ejercicio 3.12 - Verificar positividad 
Para este ejercicio se debe implementar la función `verificar_positividad` que recibe como parámetro un número y retorna información sobre si este número es positivo, negativo o cero.

Ejemplo:
```python
print(verificar_numero(5))   # Imprime: El número 5 es positivo.
print(verificar_numero(-3))  # Imprime: El número -3 es negativo.
print(verificar_numero(0))   # Imprime: El número es cero.
```
