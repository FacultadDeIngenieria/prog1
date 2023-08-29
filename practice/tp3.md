---
title: Práctica 3
layout: practice
permalink: /practice/3
---

# Trabajo Práctico 3

## Ejercicio 1 - Uso del "in"

Ingresar un nombre usando input y verificar que contenga las cada una de las vocales.
No considerar el uso de vocales con tilde, pero si considerar que la letra puede ser mayúscula o minúscula.

Ejemplo: 
```
> Matias
Contiene a: True
Contiene e: False
Contiene i: True
Contiene o: False
Contiene u: False

> Augusto
Contiene a: True
Contiene e: False
Contiene i: False
Contiene o: True
Contiene u: True
```
************************************************** 

## Ejercicio 2 - Uso del "not in"

Ingresar una oración usando input y verificar que no contenga ninguna letra con tilde
Considerar que la letra puede ser mayuscula o minuscula.

Ayuda: los caracteres de las letras con tilde son distintos que los caracteres de las letras sin tildes
( por ejemplo, la letra `á` es un carácter distinto que la letra `a`)

Ejemplo: 
```
> La contraseña no es válida
Contiene á: True
Contiene é: False
Contiene í: False
Contiene ó: False
Contiene ú: False

> A la grande le puse cuca
Contiene á: False
Contiene é: False
Contiene í: False
Contiene ó: False
Contiene ú: False
```
************************************************** 

## Ejercicio 3 - Uso del "slice" con un carácter

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

## Ejercicio 4 - Uso del "slice" con múltiples caracteres. 
Obtener los siguientes datos del texto de ejemplo:
* Primeras 3 letras del texto ( usando índices positivos )
* Las 3 letras en medio del texto ( usando índices positivos )
* De la primera a la cuarta letra ( incluída ) y de la antepenúltima hasta la última ( incluída )

Es necesario que todos los caracteres se impriman en minúscula

Ejemplo: 
```
> texto = "Awesome"
>  * código a implementar *
awe
eso
awesome
```

************************************************** 
## Ejercicio 5 - Uso del "slice" con orden inverso
Imprimir la palabra completa en orden inverso, es decir, dada vuelta.

Ejemplo: 
```
> texto = "Hello, World!"
>  * código a implementar *
!dlroW ,olleH
```

************************************************** 
# Ejercicio 6 - Uso del "slice" cada n caracteres.
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
## Ejercicio 7 - Uso del "slice" cada N caracteres con condiciones extra.
Imprimir el resultado de obtener los valores de la palabra saltando de a 2 caracteres, pero sólo a partir del quinto carácter ( incluído )

Ejemplo: 
```
> texto = "Hello, World!"
>  * código a implementar *
o ol!

> texto2 = "12345678910"
>  * código a implementar *
5790
```

************************************************** 
## Ejercicio 8 - Uso del "slice" validando que la palabra obtenida está contenida en otro string
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
## Ejercicio 9 - Modificaciones de los strings
Cambiar el nombre de la persona que aparece en la oración por tu nombre

Ejemplo: 
```
> texto = "Hello, Gastón!"
>  * código a implementar *
Hello, Matías!

```

************************************************** 
## Ejercicio 10 - Modificaciones de los strings.
Modificar el string para que se le sume un año a la edad. 
Considerar que la edad va a tener siempre 2 caracteres. 

Ejemplo: 
```
> texto = "Carlos tiene 19 años"
>  * código a implementar *
Augusto tiene 20 años!

> texto2 = "Felipe tiene 22 años"
>  * código a implementar *
Felipe tiene 23 años!

```