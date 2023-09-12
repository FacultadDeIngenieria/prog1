def calcular_area(base, altura):
    return base * altura


def calcular_perimetro(base, altura):
    return 2 * (base + altura)


def informacion_rectangulo(base, altura):
    area = calcular_area(base, altura)
    perimetro = calcular_perimetro(base, altura)
    print(f"Rectángulo con base {base} y altura {altura}:")
    print(f"Área: {area}")
    print(f"Perímetro: {perimetro}")

def es_par(numero):
    return numero % 2 == 0


def es_palindromo(cadena):
    return cadena == cadena[::-1]

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


def verificar_numero(numero):
    if numero > 0:
        return f"El número {numero} es positivo."
    elif numero < 0:
        return f"El número {numero} es negativo."
    else:
        return "El número es cero."
