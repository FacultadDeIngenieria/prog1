---
title: Ejercicios adicionales 2.do parcial
layout: practice
permalink: /additional-practice/2
---

# Práctica adicional 2.do parcial

## 6 - Lists

### Ejercicio 6.1
Definir la función `last_name_first_letter`, que debe recibir un apellido y una letra. Y debe retornar si el apellido comienza con una letra anterior, posterior o igual a la letra recibida

Ejemplo:
```python
resultado = last_name_first_letter("Longo", "M")
print(resultado) # Imprime: "El apellido Longo comienza con una letra que está antes de la M"
resultado2 = last_name_first_letter("Ponce", "C")
print(resultado2) # Imprime: "El apellido Ponce comienza con una letra que está después de la C"
resultado3 = last_name_first_letter("Gadea", "G")
print(resultado3) # Imprime: "El apellido Gadea comienza con la letra G"
```

### Ejercicio 6.2
Definir la función `name_key`, que debe recibir un nombre y un apellido, y retornar una clave compuesta por las 3 primeras letras del apellido seguido del nombre sin la última letra

Ejemplo:
```python
last_name = 'Longo'
first_name = 'Juan'
resultado = name_key(last_name, first_name)
print(resultado) #Imprime: La clave generada es: LonJua
```

Recordar que las funciones deben funcionar también para otros valores que no sean los dados como ejemplo.


### Ejercicio 6.3
Definir la funcion **agregar_fruta** que reciba una lista de frutas y una nueva fruta y la inserte al final de la lista. Consideramos las frutas como un string con su nombre

Ejemplo:
```python
frutas = ["naranja", "banana", "uva", "pera"]
nueva_lista = agregar_fruta(frutas,"manzana")
print(nueva_lista) # Imprime ["naranja", "banana", "uva", "pera","manzana"]

```

### Ejercicio 6.4
Definir la funcion **agregar_color** que reciba una lista de colores y un nuevo color y un numero que indica la posición y la inserte en la posición indicada. Consideramos los colores como un string con su nombre

Ejemplo:
```python
colores = ["rojo", "verde", "amarillo", "morado"]
nueva_lista = agregar_color(colores,"azul", 3)
print(nueva_lista) # Imprime ["rojo", "verde", "amarillo", "azul", "morado"]

```

### Ejercicio 6.5
Definir la funcion **agregar_lista** que reciba una lista de listas de strings y una nueva lista de strings, se debe retornar la lista, con la nueva lista agregada al final

Ejemplo:
```python
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nueva_lista = agregar_lista(listas,["x", "y", "z"])
print(nueva_lista) # Imprime [[1, 2, 3], [4, 5, 6], [7, 8, 9],["x", "y", "z"]]

```

### Ejercicio 6.6
Definir la funcion **eliminar_elementos** que reciba una lista y se retorne la lista eliminando las posiciones 2,3 y 4

Ejemplo:
```python
numeros = [1, 2, 3, 4, 5, 6, 7]
nueva_lista = eliminar_elementos(numeros)
print(nueva_lista) # Imprime [1,2,6,7]

```

### Ejercicio 6.7
Definir la funcion **eliminar_elementos_por_valor** que reciba una lista y un string o numero y se retorne la lista eliminando la primer ocurrencia de ese valor en la lista

Ejemplo:
```python
frutas = ["naranja", "banana", "uva", "manzana", "pera", "manzana"]
nueva_lista = eliminar_elementos_por_valor(frutas,"manzana")
print(nueva_lista) # Imprime ["naranja", "banana", "uva", "pera", "manzana"]

```
## Loops

## Ejercicio 1
Escribir la función find_min que dada una lista de números, retorna el elemento con el menor valor de la lista. Se debe recorrer la lista para encontrarlo, no se pueden usar funciones provistas por python para encontrarlo.
Ejemplo de valor a pasar a la función: [2, 5, 3, 7, 1]
Valor que se espera que retorne la función: 1

## Ejercicio 2
Escribir la función find_key_min_map que dado un dictionario cuya clave son strings y cuyo valor es un numero, retorna la clave con el menor valor. Se debe recorrer el dictionario para encontrarlo, no se pueden usar funciones provistas por python para encontrarlo.
Ejemplo de valor a pasar a la función: {"ingenieria": 100, "abogacia": 50, "medicina": 70, "administracion": 10}
Valor que se espera que retorne la función: "administracion"

## Ejercicio 3
Programe la función llamada suma_de_digitos que reciba un string que representa un numero positivo como argumento. La función deberá retornar la suma de sus digitos cómo un número entero. No se pueden utilizar librerías externas, cómo por ejemplo numpy o math.

```python
suma_de_digitos("12345")  # retorna 15
suma_de_digitos("1000001")  # retorna 2
```

## Ejercicio 4

Escribir la función categorize_words_by_length que, dado un diccionario cuyas claves son strings y cuyos valores son listas de palabras, retorna un nuevo diccionario donde las claves son longitudes de palabras y los valores son listas de palabras que tienen esa longitud. No usar funciones provistas por Python que puedan simplificar la tarea.

Ejemplo:
```python
# Dado el dict
{
    "frutas": ["manzana", "pera", "mango"],
    "animales": ["perro", "gato", "elefante"],
    "colores": ["rojo", "azul", "verde"]
}
La función retorna
{
    8: ["elefante"],
    7: ["manzana"],
    4: ["pera", "gato", "rojo", "azul"],
    5: ["perro", "verde", "mango"]
}
```

## Ejercicio 5

Escribir la función find_highest_score que, dada una lista de tuplas donde cada tupla contiene un nombre de estudiante (string) y su puntaje (entero), retorna el nombre del estudiante con el puntaje más alto. La función debe recorrer la lista para encontrar el puntaje más alto, sin usar funciones provistas por Python que puedan simplificar la tarea.

```python
Dado: [("Juan", 85), ("Ana", 92), ("Pedro", 88), ("Claudia", 95)]
Retorna: "Claudia"
```


