---
title: Práctica Scopes
layout: practice
permalink: /practice/scopes
---

# Trabajo Práctico Scopes


## Ejercicio 1

```python
def mi_funcion():
    x = 10
    print(x)

x = 5
mi_funcion()
print(x)
```
Responder:
¿Cuál será la salida de este código? ¿ Por qué ?

## Ejercicio 2

```python
def mi_funcion():
    global x
    x = 10
    print(x)

x = 5
mi_funcion()
print(x)
```
Responder:
¿Cuál será la salida de este código? ¿ Por qué ?

## Ejercicio 3

```python
def incrementar():
    global contador
    contador += 1

contador = 0
incrementar()
incrementar()
incrementar()
print(contador)
```
Responder:
¿Cuál será la salida de este código? ¿ Por qué ?

## Ejercicio 4

```python
def mi_funcion():
    x = 10
    print(x)

x = 5
mi_funcion()
print(x)
```
Responder:
¿Qué sucede si intentas imprimir x fuera de la función mi_funcion? ¿ Por qué ?

## Ejercicio 5

```python
def mi_funcion():
    global x
    x = 10
    print(x)

x = 5
mi_funcion()
print(x)
```
Responder:
¿Qué sucede si eliminas la línea global x de la función mi_funcion? ¿ Por qué ?

## Ejercicio 6

```python
def exterior():
    x = 10
    def interior():
        print(x)
    interior()

exterior()
```
Responder:
¿Cuál será la salida de este código? ¿ Por qué ?

## Ejercicio 7

```python
def mi_funcion():
    print(y)

y = 10
mi_funcion()
```
Responder:
¿Cuál será la salida de este código? ¿ Por qué ?

## Ejercicio 8

```python
def mi_funcion():
    global y
    print(y)

y = 10
mi_funcion()
```
Responder:
¿Cuál será la salida de este código? ¿ Por qué ?

## Ejercicio 9

```python
def exterior():
    x = 10
    def interior():
        x = 20
        print(x)
    interior()
    print(x)

exterior()
```
Responder:
¿Cuál será la salida de este código? ¿ Por qué ?
