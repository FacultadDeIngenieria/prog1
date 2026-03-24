# Soluciones TP3 - Condicionales

## Ejercicio 1 - exercise_positive.py

```python
def positive():
    numero = int(input())

    if numero > 0:
        print("El numero es positivo")
    elif numero < 0:
        print("El numero es negativo")
    else:
        print("El numero es cero")
```

---

## Ejercicio 2 - exercise_even_odd.py

```python
def even_odd():
    numero = int(input())

    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
```

---

## Ejercicio 3 - exercise_age_check.py

```python
def age_check():
    edad = int(input())
    limite = int(input())

    if edad <= 0 or limite <= 0:
        print("Entrada invalida")
    elif edad >= limite:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
```

---

## Ejercicio 4 - exercise_compare.py

```python
def compare():
    num1 = int(input())
    num2 = int(input())

    if num1 > num2:
        print(f"{num1} es mayor que {num2}")
    elif num1 < num2:
        print(f"{num1} es menor que {num2}")
    else:
        print(f"{num1} es igual a {num2}")
```

---

## Ejercicio 5 - exercise_grades.py

```python
def grades():
    nota = int(input())

    if nota >= 9:
        print("Excelente")
    elif nota >= 7:
        print("Bueno")
    elif nota >= 5:
        print("Regular")
    else:
        print("Insuficiente")
```

---

## Ejercicio 6 - exercise_weekday.py

```python
def weekday():
    dia = input()

    if not (dia == "sabado" or dia == "domingo"):
        print("Dia habil")
    else:
        print("Fin de semana")
```

---

## Ejercicio 7 - exercise_calculator.py

```python
def calculator():
    num1 = float(input())
    num2 = float(input())
    operacion = input()

    if operacion == "+":
        resultado = num1 + num2
        print(f"Resultado: {resultado}")
    elif operacion == "-":
        resultado = num1 - num2
        print(f"Resultado: {resultado}")
    elif operacion == "*":
        resultado = num1 * num2
        print(f"Resultado: {resultado}")
    elif operacion == "/":
        if num2 == 0:
            print("Error: division por cero")
        else:
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
    else:
        print("Operacion invalida")
```

---

## Ejercicio 8 - exercise_triangle.py

```python
def triangle():
    lado1 = float(input())
    lado2 = float(input())
    lado3 = float(input())

    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        print("Los lados forman un triangulo valido")
    else:
        print("Los lados no forman un triangulo valido")
```

---

## Ejercicio 9 (Integrador) - exercise_discount.py

```python
def discount():
    precio = float(input())
    cantidad = int(input())

    subtotal = precio * cantidad

    if cantidad >= 10:
        porcentaje = 20
    elif cantidad >= 5:
        porcentaje = 10
    else:
        porcentaje = 0

    monto_descuento = subtotal * porcentaje / 100
    total_final = subtotal - monto_descuento

    print(f"Subtotal: {subtotal}")
    print(f"Descuento aplicado: {porcentaje}%")
    print(f"Monto de descuento: {monto_descuento}")
    print(f"Total final: {total_final}")
```

---

## Ejercicio 10 - exercise_password.py

```python
def password():
    contraseña = input()

    # Variables booleanas para cada requisito
    es_larga = len(contraseña) >= 8

    # Verificar si contiene algún número usando el operador in y or
    tiene_numero = ("0" in contraseña or "1" in contraseña or "2" in contraseña or
                    "3" in contraseña or "4" in contraseña or "5" in contraseña or
                    "6" in contraseña or "7" in contraseña or "8" in contraseña or
                    "9" in contraseña)

    # Si cumple ambos requisitos
    if es_larga and tiene_numero:
        print("Contraseña valida")
    else:
        # IFS INDEPENDIENTES (no elif!) para que pueda imprimir ambos errores
        if not es_larga:
            print("Contraseña muy corta")
        if not tiene_numero:
            print("Debe contener un numero")
```

---

## Ejercicio 11 (Desafío) - exercise_leap_year.py

```python
def leap_year():
    año = int(input())

    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")
```

---

## Notas importantes:

1. **Ejercicio 1 (positive)**: Usa `if-elif-else` para tres casos mutuamente excluyentes
2. **Ejercicio 3 (age_check)**: Valida entradas antes de procesar
3. **Ejercicio 6 (weekday)**: Practica el operador `not`
4. **Ejercicio 7 (calculator)**: Usa if anidado para validar división por cero
5. **Ejercicio 8 (triangle)**: Todas las condiciones se deben cumplir simultáneamente (usa `and`)
6. **Ejercicio 10 (password)**: Usa múltiples ifs independientes (no `elif`) para mostrar ambos errores
7. **Ejercicio 11 (leap_year)**: Condición lógica compleja con `and` y `or`
