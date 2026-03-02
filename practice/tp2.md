---
title: Práctica 2
layout: practice
permalink: /practice/2
---

# Trabajo Práctico 2

## Completar el trabajo práctico en GitHub Classroom

[Link al TP 2](https://classroom.github.com/a/I6IpQ03T)

## Temas evaluados

Variables, asignación, operaciones matemáticas, casting, strings, input y f-strings.

## Cómo ejecutar los tests

Para verificar todos los ejercicios:

```bash
pytest
```

Para verificar un ejercicio en particular:

```bash
pytest test_tp3_casting.py
```

---

## Ejercicios

### Ejercicio 1 — `names.py`

**Archivo de test:** `test_tp3_ada_change_in_tests.py`

**Conceptos:** `input()`, concatenación de strings (`+`), `lower()`, `title()`, `upper()`, caracter de escape (`\t`).

**Consigna:** Leer un nombre y un apellido mediante `input()`. Concatenarlos en un nombre completo y luego imprimir:

1. El nombre completo en minúsculas.
2. El nombre completo con formato título (primera letra de cada palabra en mayúscula).
3. El nombre completo en mayúsculas.
4. El nombre completo en minúsculas precedido por un tabulador.

**Ejemplo:** Para la entrada `"AdA"` y `"LoVeLAce"`, la salida esperada es:

```
ada lovelace
Ada Lovelace
ADA LOVELACE
	ada lovelace
```

---

### Ejercicio 2 — `change.py`

**Archivo de test:** `test_tp3_ada_change_in_tests.py`

**Conceptos:** `input()`, `float()`, `int()`, operaciones matemáticas (`-`, `*`), `round()`.

**Consigna:** Leer un gasto (decimal) y el dinero recibido (entero) mediante `input()`. Calcular el vuelto y separarlo en pesos (parte entera) y centavos. Imprimir toda la información con el formato que se muestra a continuación.

**Ejemplo:** Para la entrada `"23.75"` y `"100"`, la salida esperada es:

```
Ingresar gasto:
23.75
Dinero recibido
100

Vuelto

Pesos:
76
Centavos:
25
```

---

### Ejercicio 3 — `casting.py`

**Archivo de test:** `test_tp3_casting.py`

**Conceptos:** `input()`, `int()`, `float()`, operaciones matemáticas (`-`, `*`), f-strings.

**Consigna:** Leer un precio (texto que representa un entero), un descuento (texto que representa un decimal) y una cantidad (texto que representa un entero) mediante `input()`. Convertir los valores al tipo numérico correspondiente, calcular el precio con descuento y el total, e imprimir los resultados.

**Ejemplo:** Para la entrada `"150"`, `"23.5"` y `"3"`, la salida esperada es:

```
Precio: 150
Descuento: 23.5
Precio con descuento: 126.5
Total: 379.5
```

---

### Ejercicio 4 — `input_calc.py`

**Archivo de test:** `test_tp3_input_calc.py`

**Conceptos:** `input()`, `int()`, operaciones matemáticas (`*`, `+`, `*`), f-strings.

**Consigna:** Leer la base y la altura de un rectángulo mediante `input()`. Convertirlos a enteros y calcular el área y el perímetro. Imprimir los resultados.

**Ejemplo:** Para la entrada `"8"` y `"5"`, la salida esperada es:

```
Base: 8
Altura: 5
Area: 40
Perimetro: 26
```

---

### Ejercicio 5 — `in_string.py`

**Archivo de test:** `test_tp3_in_string.py`

**Conceptos:** `input()`, `lower()`, operador `in`, f-strings.

**Consigna:** Leer un nombre mediante `input()`. Convertirlo a minúsculas y verificar si contiene cada una de las vocales (a, e, i, o, u). Imprimir el resultado para cada vocal.

**Ejemplo:** Para la entrada `"Matias"`, la salida esperada es:

```
Contiene a: True
Contiene e: False
Contiene i: True
Contiene o: False
Contiene u: False
```

---

### Ejercicio 6 — `slice_simple.py`

**Archivo de test:** `test_tp3_slice_simple.py`

**Conceptos:** slicing de strings (`[inicio:fin]`), `lower()`.

**Consigna:** Dada la variable `texto = "Awesome"`, imprimir:

1. Los primeros 3 caracteres en minúsculas.
2. Los caracteres desde la posición 2 hasta la 4 (inclusive).
3. El texto completo en minúsculas.

**Salida esperada:**

```
awe
eso
awesome
```

---

### Ejercicio 7 — `slice_advanced.py`

**Archivo de test:** `test_tp3_slice_advanced.py`

**Conceptos:** `input()`, slicing con paso (`[inicio::paso]`).

**Consigna:** Leer un texto mediante `input()`. Imprimir los caracteres desde la posición 4 en adelante, tomando uno de cada dos (paso 2).

**Ejemplo:** Para la entrada `"Hello, World!"`, la salida esperada es:

```
o ol!
```

---

### Ejercicio 8 — `string_info.py`

**Archivo de test:** `test_tp3_string_info.py`

**Conceptos:** `len()`, indexación (`[0]`, `[-1]`), repetición de strings (`*`), concatenación (`+`), f-strings.

**Consigna:** Dada la variable `palabra = "Programacion"`, imprimir:

1. La palabra.
2. Su longitud.
3. Su primera letra.
4. Su última letra.
5. La palabra repetida 3 veces.
6. La palabra decorada con `***` a cada lado.

**Salida esperada:**

```
Palabra: Programacion
Longitud: 12
Primera letra: P
Ultima letra: n
Repetida: ProgramacionProgramacionProgramacion
Decorada: ***Programacion***
```

---

### Ejercicio 9 — `string_methods.py`

**Archivo de test:** `test_tp3_string_methods.py`

**Conceptos:** `strip()`, `lstrip()`, `rstrip()`, `upper()`, `lower()`, `title()`, `find()`, `replace()`, `count()`, operador `in`, slicing, slicing con paso, slicing reverso (`[::-1]`), f-strings, strings multilínea.

**Consigna:** Dadas las siguientes variables:

```python
nombre = "   Grace Hopper   "
frase = "Python es un gran lenguaje de programacion"
multilinea = """Linea 1
Linea 2
Linea 3"""
```

Imprimir los resultados de aplicar las distintas operaciones de strings sobre estas variables, en el siguiente orden:

1. `nombre` sin espacios (strip), sin espacios a la izquierda (lstrip), sin espacios a la derecha (rstrip).
2. `frase` en mayúsculas, minúsculas y formato título.
3. Imprimir la posición de `"gran"` en `frase`.
4. `frase` reemplazando `"programacion"` por `"desarrollo"`.
5. Contar la cantidad de `'a'` en `frase`.
6. Verificar si `"Python"` y `"Java"` están en `frase`.
7. Extraer `"Python"` de `frase` usando slicing.
8. Caracteres no contiguos de `"Python"` con paso 2.
9. `"Python"` en orden inverso.
10. Combinar `nombre` (sin espacios) y `"Python"` en un f-string.
11. Imprimir el string multilínea.

**Salida esperada:**

```
Strip: Grace Hopper
Lstrip: Grace Hopper   
Rstrip:    Grace Hopper
Upper: PYTHON ES UN GRAN LENGUAJE DE PROGRAMACION
Lower: python es un gran lenguaje de programacion
Title: Python Es Un Gran Lenguaje De Programacion
Find: 13
Replace: Python es un gran lenguaje de desarrollo
Count: 4
Contiene Python: True
Contiene Java: False
Slice: Python
Paso: Pto
Reverso: nohtyP
Formato: Grace Hopper sabe Python
Linea 1
Linea 2
Linea 3
```

---

### Ejercicio 10 (Integrador) — `ficha.py`

**Archivo de test:** `test_tp3_ficha.py`

**Conceptos:** Todos los anteriores combinados: `input()`, `strip()`, `title()`, `lower()`, `upper()`, `int()`, `len()`, `find()`, indexación, slicing, `[::-1]`, `replace()`, `count()`, operador `in`, f-strings, strings multilínea, repetición de strings (`*`), concatenación (`+`), operaciones matemáticas (`+`, `/`, `//`).

**Consigna:** Crear un generador de ficha de alumno. Leer mediante `input()`:

1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas).
2. Email (puede tener mayúsculas).
3. Tres notas (como texto).

Con esos datos, generar e imprimir una ficha que incluya:

- Un encabezado decorativo usando un string multilínea con `"="`.
- Nombre limpio (sin espacios extra, con formato título).
- Email en minúsculas.
- Cantidad de caracteres del nombre.
- Iniciales (usar `find` para encontrar el espacio e indexar las letras).
- Usuario generado: `apellido.nombre` en minúsculas.
- Verificar si el email contiene `@`.
- Extraer el dominio del email.
- Nombre con guion bajo en vez de espacio (usar `replace`).
- Contar la cantidad de `'a'` en el nombre.
- Código secreto: nombre invertido en mayúsculas.
- Las 3 notas, su suma, promedio y promedio entero.
- Un cierre decorativo usando repetición de string (`"=" * 24`).

**Ejemplo:** Para la entrada `"   maria GARCIA   "`, `"Maria.Garcia@Universidad.EDU"`, `"8"`, `"9"`, `"7"`, la salida esperada es:

```
========================
    FICHA DEL ALUMNO
========================
Nombre: Maria Garcia
Email: maria.garcia@universidad.edu
Caracteres en nombre: 12
Iniciales: MG
Usuario: garcia.maria
Email valido: True
Dominio: universidad.edu
Nombre para archivo: Maria_Garcia
Cantidad de a: 4
Codigo secreto: AICRAG AIRAM
Nota 1: 8
Nota 2: 9
Nota 3: 7
Suma: 24
Promedio: 8.0
Promedio entero: 8
========================
```
