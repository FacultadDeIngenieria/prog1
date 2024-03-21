# WIP
# Trabajo Práctico 3 - Ejercicios adicionales

## Ejercicio 2 - Uso del "not in"

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
Carlos tiene 20 años!

> texto2 = "Felipe tiene 22 años"
>  * código a implementar *
Felipe tiene 23 años!

```