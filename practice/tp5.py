import math


# 1
def dias_a_horas(dias):
    if dias < 0:
        return "Número erróneo de días ingresados"
    else:
        return int(dias) * 24

# 2


def dias_a_horas_con_fracciones(dias):
    if dias < 0:
        return "Número erróneo de días ingresados"
    else:
        return dias * 24

# 3


def dias_a_horas_reutilizable(dias):
    return dias_a_horas_con_fracciones(dias)

# 4


def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x >= y:
        biggest = x
    else:
        biggest = y
    return biggest


def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if x >= y and x >= z:
        biggest = x
    elif y >= x and y >= z:
        biggest = y
    else:
        biggest = z
    return biggest


# 5

def concatenar_strings(string_1, string_2):
    return f"{string_1} {string_2}"


# 6


def calcular_area(base, altura):
    resultado = base * altura
    if resultado < 0:
        return "El área del rectángulo no puede ser negativa"
    else:
        return resultado

# 7


def calcular_perimetro(base, altura):
    resultado = 2 * (base + altura)
    if resultado < 0:
        return "El perímetro del rectángulo no puede ser negativo"
    else:
        return resultado

# 8


def informacion_rectangulo(base, altura):
    area = calcular_area(base, altura)
    perimetro = calcular_perimetro(base, altura)
    print(f"Rectángulo con base {base} y altura {altura}:")
    print(f"Área: {area}")
    print(f"Perímetro: {perimetro}")

# 9


def invertir_string(string):
    return string[::-1]

# 10


def es_par(numero):
    return numero % 2 == 0

 # 11


def es_palindromo(cadena):
    return cadena == cadena[::-1]

# 12


def calificar_estudiante(puntuacion):
    if puntuacion >= 90:
        return "A"
    elif puntuacion >= 80:
        return "B"
    elif puntuacion >= 70:
        return "C"
    elif puntuacion >= 60:
        return "D"
    else:
        return "F"

# 13


def verificar_numero(numero):
    if numero > 0:
        return f"El número {numero} es positivo."
    elif numero < 0:
        return f"El número {numero} es negativo."
    else:
        return "El número es cero."


# 14


def number_to_month(month):
    if (month == 1): return "Jan"
    elif (month == 2): return "Feb"
    elif (month == 3): return "Mar"
    elif (month == 4): return "Apr"
    elif (month == 5): return "May"
    elif (month == 6): return "Jun"
    elif (month == 7): return "Jul"
    elif (month == 8): return "Aug"
    elif (month == 9): return "Sep"
    elif (month == 10): return "Oct"
    elif (month == 11): return "Nov"
    elif (month == 12): return "Dec"
    else:
        return "Error"


 # 15

def roots(a, b, c):
    radicando = math.pow(b, 2) - 4 * a * c
    if radicando > 0:
        x1 = (-b + math.sqrt(radicando)) / (2 * a)
        x2 = (-b - math.sqrt(radicando)) / (2 * a)
        return f"({x1},{x2})"
    if radicando == 0:
        # Tiene 1 raiz doble
        x = (-b + math.sqrt(radicando)) / (2 * a)
        return f"({x})"
    else:
        # No tiene raices
        return "()"


def valueY(a, b, c, x):
    return (a * math.pow(x, 2)) + (b * x) + c


def toString(a, b, c):
    return f"Y = {a} * X2 + {b} * X + {c}"


def derivation(a, b):
    return f"Y' = 2*{a} * X + {b}"