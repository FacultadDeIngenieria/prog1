class: center, middle, inverse

# **Ejercicio 4 - Sistema de Gimnasio**

---

## Enunciado

Implementar `gym_membership` que calcule el costo mensual segun:

- **Plan "basico":** $2000 | **Plan "premium":** $3500
- **Menores de 18:** 15% descuento
- **60 o mas:** 25% descuento
- **Fin de semana:** +$500 (despues de descuentos)
- Edad negativa o plan invalido → `"Datos de entrada no validos"`

---

## Estructura del problema

```
1. Pedir datos (edad, plan, fin de semana)
2. Validar datos
3. Determinar costo base segun plan
4. Aplicar descuento por edad
5. Sumar recargo por fin de semana
6. Imprimir resultado
```

---

## Solucion - Parte 1: Entrada y validacion

```python
def gym_membership():
    edad = int(input("Ingrese la edad del socio: "))
    plan = input("Ingrese el plan (basico/premium): ")
    fds = input("¿Acceso fin de semana? (si/no): ")

    if edad < 0 or (plan != "basico" and plan != "premium"):
        print("Datos de entrada no validos")
        return
```

---

## Solucion - Parte 2: Costo base

```python
    if plan == "basico":
        costo = 2000
    else:
        costo = 3500
```

El plan solo puede ser `"basico"` o `"premium"` (ya validamos arriba).

---

## Solucion - Parte 3: Descuentos por edad

```python
    if edad < 18:
        costo = costo * 0.85
    elif edad >= 60:
        costo = costo * 0.75
```

- Menor de 18 → 15% descuento → multiplicar por 0.85
- 60 o mas → 25% descuento → multiplicar por 0.75
- Entre 18 y 59 → sin descuento

---

## Solucion - Parte 4: Recargo y resultado

```python
    if fds == "si":
        costo = costo + 500

    print("El costo final de la membresia es: $" + str(costo))
```

El recargo se aplica **despues** de los descuentos.

---

## Solucion completa

```python
def gym_membership():
    edad = int(input("Ingrese la edad del socio: "))
    plan = input("Ingrese el plan (basico/premium): ")
    fds = input("¿Acceso fin de semana? (si/no): ")

    if edad < 0 or (plan != "basico" and plan != "premium"):
        print("Datos de entrada no validos")
        return

    if plan == "basico":
        costo = 2000
    else:
        costo = 3500

    if edad < 18:
        costo = costo * 0.85
    elif edad >= 60:
        costo = costo * 0.75

    if fds == "si":
        costo = costo + 500

    print("El costo final de la membresia es: $" + str(costo))
```

---

## Ejemplo 1

Edad: 70, Plan: "premium", Fin de semana: "no"

```
costo = 3500           (premium)
costo = 3500 * 0.75    (60 o mas → 25% descuento)
costo = 2625.0
```

**Imprime:** `El costo final de la membresia es: $2625.0`

---

## Ejemplo 2

Edad: 25, Plan: "basico", Fin de semana: "si"

```
costo = 2000           (basico)
                       (sin descuento por edad)
costo = 2000 + 500     (fin de semana)
costo = 2500
```

**Imprime:** `El costo final de la membresia es: $2500`

---

## Ejemplo 3

Edad: 15, Plan: "premium", Fin de semana: "si"

```
costo = 3500           (premium)
costo = 3500 * 0.85    (menor de 18 → 15% descuento)
costo = 2975.0
costo = 2975.0 + 500   (fin de semana)
costo = 3475.0
```

**Imprime:** `El costo final de la membresia es: $3475.0`

---

## Caso invalido

Edad: -5, Plan: "basico"

```
edad < 0 → True
```

**Imprime:** `Datos de entrada no validos`

---

class: center, middle, inverse

[Volver a las respuestas](/prog1/simulacrum-answers#2)
