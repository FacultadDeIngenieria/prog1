---
marp: true
theme: default
paginate: true
---

# Introducción a la Programación I
## Clase 2: Strings e Input

---

## ¿Qué es un String?

Un **string** es una secuencia de caracteres.

En Python se puede escribir con comillas simples o dobles — el resultado es el mismo:

```python
nombre = 'Ada Lovelace'
nombre = "Ada Lovelace"
```

Podés usar comillas dobles dentro de un string con comillas simples, y viceversa:

```python
mensaje = "Le dijo 'hola' al pasar."
```

---

## Concatenación de Strings

Con el operador `+` podés unir (concatenar) strings:

```python
nombre = "Ada"
apellido = "Lovelace"
nombre_completo = nombre + " " + apellido
print(nombre_completo)
```

```
Ada Lovelace
```

---

## Longitud de un String: `len()`

La función `len()` devuelve la cantidad de caracteres de un string:

```python
nombre = "Python"
print(len(nombre))
```

```
6
```

Incluye espacios y caracteres especiales:

```python
print(len("hola mundo"))  # 10
```

---

## Métodos de String: `title()`, `upper()`, `lower()`

Los **métodos** son funciones asociadas a un objeto. Se llaman con un punto.

```python
nombre = "ada lovelace"

print(nombre.title())   # Ada Lovelace
print(nombre.upper())   # ADA LOVELACE
print(nombre.lower())   # ada lovelace
```

> `lower()` es muy útil para comparar strings sin importar mayúsculas.

---

## Comparar Strings

Podés usar operadores de comparación con strings:

| Operador | Significado      |
|----------|-----------------|
| `==`     | igual a         |
| `!=`     | distinto de     |
| `<`      | menor que       |
| `>`      | mayor que       |
| `<=`     | menor o igual   |
| `>=`     | mayor o igual   |

```python
print("gato" == "gato")   # True
print("gato" != "perro")  # True
print("abc" < "abd")      # True  (orden alfabético)
```

---

## Eliminar Espacios en Blanco

Los espacios al principio o al final de un string suelen ser un problema.

```python
lenguaje = "  python  "

print(lenguaje.rstrip())   # "  python"
print(lenguaje.lstrip())   # "python  "
print(lenguaje.strip())    # "python"
```

> Muy útil al procesar input del usuario.

---

## f-strings: Formatear Strings con Variables

Los **f-strings** permiten insertar variables directamente dentro de un string:

```python
nombre = "Ada"
apellido = "Lovelace"

mensaje = f"Hola, {nombre} {apellido}!"
print(mensaje)
```

```
Hola, Ada Lovelace!
```

También podés poner expresiones:

```python
print(f"2 + 2 = {2 + 2}")  # 2 + 2 = 4
```

---

## Caracteres Especiales: `\n` y `\t`

`\n` agrega un **salto de línea**, `\t` agrega una **tabulación**:

```python
print("Lenguajes:\n\tPython\n\tJavaScript\n\tRuby")
```

```
Lenguajes:
    Python
    JavaScript
    Ruby
```

---

## Buscar en un String: `find()`

`find(sub)` devuelve el **índice más bajo** donde se encuentra el substring.
Si no lo encuentra, devuelve `-1`.

```python
mensaje = "hola mundo"

print(mensaje.find("mundo"))  # 5
print(mensaje.find("xyz"))    # -1
```

Los índices empiezan en `0`.

---

## Strings Multilínea

Con **triple comillas** (`"""` o `'''`) podés crear strings que abarcan varias líneas:

```python
poema = """Había una vez
un programador
que amaba Python."""

print(poema)
```

```
Había una vez
un programador
que amaba Python.
```

---

## Verificar si un Substring Está Presente

Usá `in` y `not in` para buscar substrings:

```python
frase = "me gusta Python"

print("Python" in frase)       # True
print("JavaScript" in frase)   # False
print("Java" not in frase)     # True
```

---

## Slicing: Acceder a Caracteres Individuales

Podés acceder a un carácter por su **índice** (empieza en `0`):

```python
lenguaje = "Python"

print(lenguaje[0])   # P
print(lenguaje[1])   # y
print(lenguaje[-1])  # n  (último carácter)
print(lenguaje[-2])  # o  (anteúltimo)
```

Los **índices negativos** cuentan desde el final.

---

## Slicing: Rango de Caracteres

Podés extraer una porción de un string con `[start:end]`:

- El índice de inicio está **incluido**
- El índice de fin está **excluido**

```python
lenguaje = "Python"

print(lenguaje[0:3])   # Pyt
print(lenguaje[2:5])   # tho
```

---

## Slicing: Omitir Índices

Si omitís el inicio, arranca desde el principio.
Si omitís el fin, llega hasta el final.

```python
lenguaje = "Python"

print(lenguaje[:3])   # Pyt   (desde el inicio hasta índice 2)
print(lenguaje[3:])   # hon   (desde índice 3 hasta el final)
print(lenguaje[:])    # Python (copia completa)
```

---

## Slicing: Saltar Caracteres y Orden Inverso

Con `[start:end:step]` podés saltar de a `step` caracteres:

```python
texto = "abcdefgh"

print(texto[::2])    # aceg  (de a dos)
print(texto[1::2])   # bdfh
```

Para invertir un string usá `[::-1]`:

```python
print("Python"[::-1])   # nohtyP
```

---

## Los Strings son Inmutables

No podés modificar un string cambiando uno de sus caracteres directamente:

```python
lenguaje = "Python"
lenguaje[0] = "J"   # ❌ TypeError!
```

Para "modificar" un string hay que crear uno nuevo:

```python
lenguaje = "J" + lenguaje[1:]
print(lenguaje)   # Jython
```

---

## Métodos: `replace()` y `count()`

**`replace(old, new)`** — reemplaza todas las apariciones de un substring:

```python
frase = "me gusta Java, Java es genial"
nueva = frase.replace("Java", "Python")
print(nueva)   # me gusta Python, Python es genial
```

**`count(substring)`** — cuenta cuántas veces aparece un substring:

```python
print(frase.count("Java"))   # 2
```

---

## Input del Usuario: `input()`

La función `input()` muestra un mensaje y espera que el usuario escriba algo.
Siempre devuelve un **string**.

```python
nombre = input("¿Cómo te llamás? ")
print(f"Hola, {nombre}!")
```

```
¿Cómo te llamás? Ada
Hola, Ada!
```

---

## Parsear Input como Número

Como `input()` devuelve un string, hay que convertirlo para hacer operaciones matemáticas:

```python
edad_str = input("¿Cuántos años tenés? ")
edad = int(edad_str)
print(f"El año que viene tenés {edad + 1} años.")
```

Para números decimales usá `float()`:

```python
altura = float(input("¿Cuánto medís (en metros)? "))
```

---

## Combinando `input()` con Métodos de String

```python
nombre = input("Ingresá tu nombre: ").strip().title()
print(f"Bienvenido/a, {nombre}!")
```

Se pueden encadenar métodos: primero se ejecuta `strip()`, después `title()`.

---

## Documentación de Python

Python tiene documentación oficial con todos los métodos de string disponibles:

🔗 [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

Algunos métodos útiles además de los vistos:

| Método          | Qué hace                              |
|-----------------|---------------------------------------|
| `startswith(s)` | True si empieza con `s`               |
| `endswith(s)`   | True si termina con `s`               |
| `isdigit()`     | True si todos los caracteres son dígitos |
| `split(sep)`    | Divide el string en una lista         |

---

## Resumen de la Clase

| Concepto            | Ejemplo                         |
|---------------------|---------------------------------|
| Concatenación       | `"hola" + " " + "mundo"`        |
| `len()`             | `len("Python")` → `6`           |
| Métodos             | `"ada".title()` → `"Ada"`       |
| f-strings           | `f"Hola {nombre}"`              |
| Slicing             | `"Python"[0:3]` → `"Pyt"`       |
| `in` / `not in`     | `"py" in "python"` → `True`     |
| `input()`           | `nombre = input("Nombre: ")`    |
| `int()` / `float()` | `edad = int(input("Edad: "))`   |
