# Soluciones de Ejemplo

---

## Ejercicio 0 - Lectura de Código

Este ejercicio no requiere escribir código, solo leer y predecir el output.

**Output esperado:**

```
valor de i1:
3
valor de i2:
5
valor de i3:
8
16
Python is awesome
valor de x: Naranja, valor de y: Naranja, valor de z: Naranja
1.6
3
entero i3:
9
variable f3:
9.5
el valor de
13
más
-0.5
es:
12.5
```

**Explicación línea por línea:**

1. `i1 = 3, i2 = 5, i3 = 8` (suma de i1 + i2)
2. `print(i1 + i2 + i3)` → `3 + 5 + 8 = 16`
3. Concatenación de strings: `"Python" + " is " + "awesome"` → `"Python is awesome"`
4. Asignación múltiple: `x = y = z = "Naranja"` (todos tienen el mismo valor)
5. `z1 = 8 / 5 = 1.6` (división decimal)
6. `z2 = 8 % 5 = 3` (resto de la división)
7. `f3 = -0.5 + 10 = 9.5`, luego `i3 = int(9.5) = 9` (conversión a entero)
8. `f2 += i1` → `f2 = 10 + 3 = 13`
9. `f2 + f1` → `13 + (-0.5) = 12.5`

---

## Ejercicio 1 - Math

```python
def math():
    a = 57
    b = 7

    print(a + b)          # suma: 64
    print(a - b)          # diferencia: 50
    print(a * b)          # producto: 399
    print((a + b) / 2)    # promedio: 32.0
    print(a // b)         # cociente entero: 8
    print(a % b)          # resto: 1
    print(a / b)          # división real: 8.142857142857142
```

---

## Ejercicio 2 - Rectangle

```python
def rectangle():
    base = 10
    altura = 5

    area = base * altura
    perimetro = 2 * base + 2 * altura

    print(area)           # 50
    print(perimetro)      # 30
```

---

## Ejercicio 3 - Temperature

```python
def temperature():
    celsius = 25

    fahrenheit = celsius * 9/5 + 32

    print(fahrenheit)     # 77.0
    print(celsius)        # 25 (valor original)
```

---

## Ejercicio 4 - Time

```python
def time():
    total_segundos = 3665

    horas = total_segundos // 3600
    resto_despues_horas = total_segundos % 3600
    minutos = resto_despues_horas // 60
    segundos = resto_despues_horas % 60

    print(horas)          # 1
    print(minutos)        # 1
    print(segundos)       # 5
```

**Alternativa más compacta:**

```python
def time():
    total_segundos = 3665

    print(total_segundos // 3600)                    # horas: 1
    print((total_segundos % 3600) // 60)            # minutos: 1
    print(total_segundos % 3600 % 60)               # segundos: 5
```

---

## Ejercicio 5 - Statistics

```python
def statistics():
    num1 = 15
    num2 = 8
    num3 = 23
    num4 = 12

    promedio = (num1 + num2 + num3 + num4) / 4
    maximo = max(num1, num2, num3, num4)
    minimo = min(num1, num2, num3, num4)
    rango = maximo - minimo

    print(promedio)       # 14.5
    print(maximo)         # 23
    print(minimo)         # 8
    print(rango)          # 15
```

---

## Ejercicio 6 - Circle

```python
from math import pi

def circle():
    radio = 5

    area = pi * radio ** 2
    circunferencia = 2 * pi * radio

    print(area)              # 78.53981633974483
    print(circunferencia)    # 31.41592653589793
```

---

## Ejercicio 7 - Length

```python
def length():
    metros = 1000

    kilometros = metros / 1000
    millas = metros / 1609.34
    pies = metros / 0.3048
    pulgadas = metros / 0.0254

    print(kilometros)     # 1.0
    print(millas)         # 0.6213711922373339
    print(pies)           # 3280.839895013123
    print(pulgadas)       # 39370.07874015748
```

---

## Ejercicio 8 - Price

```python
def price():
    precio_base = 100

    impuesto = precio_base * 0.21
    subtotal = precio_base + impuesto
    propina = subtotal * 0.10
    precio_final = subtotal + propina

    print(impuesto)       # 21.0
    print(subtotal)       # 121.0
    print(propina)        # 12.1
    print(precio_final)   # 133.1
```

---

## Ejercicio 9 - Swap

```python
def swap():
    x = 10
    y = 20

    # Imprimimos valores originales
    print(x)              # 10
    print(y)              # 20

    # Intercambiamos
    x, y = y, x

    # Imprimimos valores intercambiados
    print(x)              # 20
    print(y)              # 10
```

**Nota:** La asignación múltiple `x, y = y, x` es una característica única de Python que permite intercambiar valores sin necesidad de una variable temporal.

---

## Ejercicio 10 - Age

```python
def age():
    edad_anos = 25

    meses = edad_anos * 12
    dias = edad_anos * 365
    horas = dias * 24
    minutos = horas * 60

    print(meses)          # 300
    print(dias)           # 9125
    print(horas)          # 219000
    print(minutos)        # 13140000
```

---

## Ejercicio 11 - Grades

```python
def grades():
    nota1 = 8
    nota2 = 7
    nota3 = 9

    promedio = (nota1 + nota2 + nota3) / 3
    maximo = max(nota1, nota2, nota3)
    minimo = min(nota1, nota2, nota3)
    faltan = 10 - promedio

    print(promedio)       # 8.0
    print(maximo)         # 9
    print(minimo)         # 7
    print(faltan)         # 2.0
```

---

## Ejercicio 12 - Triangle

```python
def triangle():
    base = 10
    altura = 6

    area = (base * altura) / 2

    print(area)           # 30.0
```

---

## Ejercicio 13 - Currency

```python
def currency():
    pesos = 10000
    tasa_dolar = 1500
    tasa_euro = 1600
    tasa_real = 250

    dolares = pesos / tasa_dolar
    euros = pesos / tasa_euro
    reales = pesos / tasa_real

    print(dolares)        # 6.666666666666667
    print(euros)          # 6.25
    print(reales)         # 40.0
```

---

## Errores Comunes de los Estudiantes

### 1. Confundir `/` con `//`
```python
# ❌ Incorrecto
horas = total_segundos / 3600  # Devuelve float

# ✅ Correcto
horas = total_segundos // 3600  # Devuelve int
```

### 2. Orden incorrecto de operaciones
```python
# ❌ Incorrecto
fahrenheit = celsius * 9 / 5 + 32  # Puede dar problemas de precedencia

# ✅ Correcto (más claro)
fahrenheit = (celsius * 9 / 5) + 32
# O mejor aún:
fahrenheit = celsius * 9/5 + 32  # Python lo maneja bien
```

### 3. No guardar resultados intermedios
```python
# ❌ Difícil de leer
print((total_segundos % 3600) // 60)

# ✅ Más claro
resto = total_segundos % 3600
minutos = resto // 60
print(minutos)
```

### 4. Imprimir en el orden incorrecto
```python
# ❌ Incorrecto
print(minutos)
print(horas)
print(segundos)

# ✅ Correcto (según consigna)
print(horas)
print(minutos)
print(segundos)
```

### 5. No usar paréntesis en promedios
```python
# ❌ Incorrecto
promedio = num1 + num2 + num3 + num4 / 4  # Solo divide num4

# ✅ Correcto
promedio = (num1 + num2 + num3 + num4) / 4
```

---

## Tips de Corrección

- **Automatización:** Estos ejercicios son perfectos para corrección automática con tests unitarios
- **Outputs exactos:** El output debe coincidir exactamente (incluyendo decimales)
- **Orden:** Verificar que los prints estén en el orden correcto
- **Variables no usadas:** Está bien si crean variables auxiliares, mientras el output sea correcto
- **Estilo:** No penalizar por estilo en un TP de nivel 1, solo funcionalidad

---

## Casos de Test Adicionales

Si querés probar con otros valores para asegurar que la lógica es correcta:

### Math
- `a = 100, b = 10` → `110, 90, 1000, 55.0, 10, 0, 10.0`
- `a = 17, b = 5` → `22, 12, 85, 11.0, 3, 2, 3.4`

### Rectangle
- `base = 7, altura = 3` → `21, 20`
- `base = 15, altura = 8` → `120, 46`

### Temperature
- `celsius = 0` → `32.0, 0`
- `celsius = 100` → `212.0, 100`

### Time
- `total_segundos = 7265` → `2, 1, 5`
- `total_segundos = 86400` → `24, 0, 0`

### Statistics
- `num1 = 10, num2 = 10, num3 = 10, num4 = 10` → `10.0, 10, 10, 0`
- `num1 = 1, num2 = 100, num3 = 50, num4 = 25` → `44.0, 100, 1, 99`

---

**Fecha de creación:** Marzo 2026
**Versión:** POC 1.0
