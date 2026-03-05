---
title: Práctica 1
layout: practice
permalink: /practice/1
---

# TP1 - Trabajo Práctico 1
## Completar el trabajo práctico en GitHub Classroom

[Link al TP 1](https://classroom.github.com/a/c6oH9MFz)

## Temas evaluados

Variables, asignación, operaciones matemáticas, tipos de datos, operadores aritméticos y funciones básicas.

## Cómo ejecutar los tests

Para verificar todos los ejercicios en el directorio actual:

```bash
python3 -m unittest discover
```

Para verificar un ejercicio en particular:

```bash
python3 -m unittest test_tp1_math
```

O ejecutar directamente:

```bash
python3 test_tp1_math.py
```

---

## Ejercicios

## Ejercicio 0

Para este ejercicio el objetivo es leer el código, anotar lo que piensen que los prints vayan a decir y luego correr el código para ver si les dio igual o no.

```python
i1 = 3
i2 = 5
i3 = i2 + i1
print("valor de i1:")
print(i1)
print("valor de i2:")
print(i2)
print("valor de i3:")
print(i3)
print(i1 + i2 + i3)

s1, s2, s3 = "Python", " is ", 'awesome'
print(s1 + s2 + s3)

x = y = z = "Naranja"
print("valor de x: " + x + ", valor de y: " + y + ", valor de z: " + z)

z1 = i3 / i2
print(z1)
z2 = i3 % i2
print(z2)
f1 = -.5
f2 = 10
f3 = f1 + f2
i3 = int(f3)
print("entero i3:")
print(i3)
print("variable f3:")
print(f3)
f2 += i1
print("el valor de")
print(f2)
print("más")
print(f1)
print("es:")
print(f2 + f1)

```


### Ejercicio 1 — `exercise_math.py`

**Archivo de test:** `test_tp1_math.py`

**Conceptos:** Operadores aritméticos (`+`, `-`, `*`, `/`, `//`, `%`).

**Consigna:** Dado dos números enteros `a` y `b`, imprimir en pantalla:
1. La suma
2. La diferencia
3. El producto
4. El promedio
5. El cociente entero
6. El resto de la división entera
7. El valor real de la división

**Ejemplo:** Para `a = 57` y `b = 7` la salida esperada es:

```
64
50
399
32.0
8
1
8.142857142857142
```

---

### Ejercicio 2 — `exercise_rectangle.py`

**Archivo de test:** `test_tp1_rectangle.py`

**Conceptos:** Fórmulas geométricas, operaciones con variables.

**Consigna:** Dado un rectángulo con `base` y `altura`, calcular e imprimir:
1. El área del rectángulo
2. El perímetro del rectángulo

**Ejemplo:** Para `base = 10` y `altura = 5` la salida esperada es:

```
50
30
```

---

### Ejercicio 3 — `exercise_temperature.py`

**Archivo de test:** `test_tp1_temperature.py`

**Conceptos:** Conversiones con fórmulas, manejo de decimales.

**Consigna:** Dada una temperatura en grados Celsius, imprimir:
1. La temperatura convertida a Fahrenheit en número decimal usando: `F = C × 9/5 + 32`
2. La temperatura original en Celsius en número entero

**Ejemplo:** Para `celsius = 25` la salida esperada es:

```
77.0
25
```

---

### Ejercicio 4 — `exercise_time.py`

**Archivo de test:** `test_tp1_time.py`

**Conceptos:** División entera, módulo, conversiones de unidades.

**Consigna:** Dado un número total de segundos, calcular e imprimir:
1. Cuántas horas completas hay
2. Cuántos minutos completos quedan después de sacar las horas
3. Cuántos segundos quedan después de sacar horas y minutos

**Ejemplo:** Para `total_segundos = 3665` la salida esperada es:

```
1
1
5
```

---

### Ejercicio 5 — `exercise_statistics.py`

**Archivo de test:** `test_tp1_statistics.py`

**Conceptos:** Funciones integradas (`max()`, `min()`), cálculo de promedio.

**Consigna:** Dados cuatro números, calcular e imprimir:
1. El promedio de los cuatro números
2. El máximo de los cuatro números
3. El mínimo de los cuatro números
4. El rango (diferencia entre el máximo y el mínimo)

**Ejemplo:** Para `num1 = 15`, `num2 = 8`, `num3 = 23`, `num4 = 12` la salida esperada es:

```
14.5
23
8
15
```

---

### Ejercicio 6 — `exercise_circle.py`

**Archivo de test:** `test_tp1_circle.py`

**Conceptos:** Constantes, biblioteca `math`, potenciación.

**Consigna:** Dado el radio de un círculo, calcular e imprimir:
1. El área del círculo: `π × radio²`
2. La circunferencia: `2 × π × radio`

**Ejemplo:** Para `radio = 5` la salida esperada es:

```
78.53981633974483
31.41592653589793
```

---

### Ejercicio 7 — `exercise_length.py`

**Archivo de test:** `test_tp1_length.py`

**Conceptos:** Conversiones con múltiples unidades.

**Consigna:** Dada una distancia en metros, convertir e imprimir:
1. La distancia en kilómetros (1 km = 1000 m)
2. La distancia en millas (1 milla ≈ 1609.34 m)
3. La distancia en pies (1 pie ≈ 0.3048 m)
4. La distancia en pulgadas (1 pulgada ≈ 0.0254 m)

**Ejemplo:** Para `metros = 1000` la salida esperada es:

```
1.0
0.6213727366498067
3280.839895013123
39370.078740157485
```

---

### Ejercicio 8 — `exercise_price.py`

**Archivo de test:** `test_tp1_price.py`

**Conceptos:** Aplicación de múltiples porcentajes en secuencia.

**Consigna:** Dado un precio base, calcular e imprimir:
1. El monto del impuesto (21% del precio base)
2. El subtotal (precio base + impuesto)
3. El monto de la propina (10% del subtotal)
4. El precio final (subtotal + propina)

**Ejemplo:** Para `precio_base = 100` la salida esperada es:

```
21.0
121.0
12.1
133.1
```

---

### Ejercicio 9 — `exercise_swap.py`

**Archivo de test:** `test_tp1_swap.py`

**Conceptos:** Asignación múltiple, intercambio de variables.

**Consigna:** Dados dos valores `x` e `y`, intercambiar sus valores e imprimir:
1. Los valores originales de x e y
2. Los valores después del intercambio

**Ejemplo:** Para `x = 10` y `y = 20` la salida esperada es:

```
10
20
20
10
```

---

### Ejercicio 10 — `exercise_age.py`

**Archivo de test:** `test_tp1_age.py`

**Conceptos:** Múltiples conversiones de unidades de tiempo.

**Consigna:** Dada una edad en años, calcular e imprimir:
1. La edad en meses (aproximado: 1 año = 12 meses)
2. La edad en días (aproximado: 1 año = 365 días)
3. La edad en horas (1 día = 24 horas)
4. La edad en minutos (1 hora = 60 minutos)

**Ejemplo:** Para `edad_anos = 25` la salida esperada es:

```
300
9125
219000
13140000
```

---

### Ejercicio 11 — `exercise_grades.py`

**Archivo de test:** `test_tp1_grades.py`

**Conceptos:** Promedios, funciones `max()` y `min()`, diferencias.

**Consigna:** Dadas tres calificaciones (notas), calcular e imprimir:
1. El promedio de las tres notas
2. La nota máxima
3. La nota mínima
4. Cuántos puntos le faltan al promedio para llegar a 10

**Ejemplo:** Para `nota1 = 8`, `nota2 = 7`, `nota3 = 9` la salida esperada es:

```
8.0
9
7
2.0
```

---

### Ejercicio 12 — `exercise_triangle.py`

**Archivo de test:** `test_tp1_triangle.py`

**Conceptos:** Fórmulas geométricas.

**Consigna:** Dados la base y la altura de un triángulo, calcular e imprimir:
1. El área del triángulo

**Ejemplo:** Para `base = 10` y `altura = 6` la salida esperada es:

```
30.0
```

---

### Ejercicio 13 — `exercise_currency.py`

**Archivo de test:** `test_tp1_currency.py`

**Conceptos:** Conversiones con tasas de cambio.

**Consigna:** Dado un monto en pesos argentinos, convertir e imprimir:
1. El monto en dólares (usando una tasa de cambio)
2. El monto en euros (usando una tasa de cambio)
3. El monto en reales brasileños (usando una tasa de cambio)

**Ejemplo:** Para `pesos = 10000`, `tasa_dolar = 1500`, `tasa_euro = 1600`, `tasa_real = 250` la salida esperada es:

```
6.666666666666667
6.25
40.0
```

---
