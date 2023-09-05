# # Ejercicio 1
# a = True
# b = False
# c = False
#
# print(f"El valor de a es {a}")
# print(f"El valor de b es {b}")
# print(f"El valor de c es {c}")
#
# print(f"El valor de a y el valor de b son iguales: {a == b}")
# print(f"El valor de b y el valor de c son iguales: {b == c}")
# print(f"El valor de a y el valor de c son iguales: {a == c}")
#
# print(f"El valor de a y el valor de b son distintos: {a != b}")
# print(f"El valor de b y el valor de c son distintos: {b != c}")


# # Ejercicio 2
#
# a = 4
# b = -5
# c = 2
#
# mayor = a
# menor = a
#
# if b > mayor:
#     mayor = b
# if c > mayor:
#     mayor = c
#
# if b < menor:
#     menor = b
# if c < menor:
#     menor = c
#
# print(f"El número mayor es: {mayor}")
# print(f"El número menor es: {menor}")
#

# # Ejercicio 3
#
# edad_adolescente = 14
# edad_abuelo = 66
#
# costo_nino = 0
# costo_adolescente = 50
# costo_adulto = 30
# costo_anciano = 10
#
# pago_total = 0
# pago_adolescente = 0
# pago_abuelo = 0
#
# edad_1 = 4
# edad_2 = 17
# edad_3 = 18
# edad_4 = 50
#
# if edad_adolescente <= edad_1:
#     pago_adolescente = costo_nino
# elif edad_adolescente <= edad_2:
#     pago_adolescente = costo_adolescente
# elif edad_adolescente <= edad_3:
#     pago_adolescente = costo_adolescente
# elif edad_adolescente > edad_4:
#     pago_adolescente = costo_anciano
#
# pago_total += pago_adolescente
#
# if edad_abuelo <= edad_1:
#     edad_abuelo = costo_nino
# elif edad_abuelo <= edad_2:
#     edad_abuelo = costo_adolescente
# elif edad_abuelo <= edad_3:
#     edad_abuelo = costo_adolescente
# elif edad_abuelo > edad_4:
#     edad_abuelo = costo_anciano
#
# pago_total += edad_abuelo
#
# print(f"El costo de entrada para el grupo familiar es de: ${pago_total}")

# # Ejercicio 4
# dia = "lunes"
#
# if dia == "lunes" or dia == "martes" or dia == "miércoles" or dia == "jueves" or dia == "viernes":
#     print(f"El día {dia} es un día laborable.")
# elif dia == "sábado" or dia == "domingo":
#     print(f"El día {dia} es un día de fin de semana.")
# else:
#     print(f"El día {dia} no es válido.")


# Ejercicio 5
# import math
#
# # coeficiente_a = 2.3
# # coeficiente_b = -4.0
# # coeficiente_x1 = 50
# # coeficiente_x2 = -32.9
# coeficiente_a = float(input("Ingrese el coeficiente A:\n"))
# coeficiente_b = float(input("Ingrese el coeficiente B:\n"))
# coeficiente_x1 = float(input("Ingrese el coeficiente X1:\n"))
# coeficiente_x2 = float(input("Ingrese el coeficiente X2:\n"))
#
# coeficiente_y1 = coeficiente_a * coeficiente_x1 + coeficiente_b
# coeficiente_y2 = coeficiente_a * coeficiente_x2 + coeficiente_b
#
# print(f"Para la siguiente ecuación: \n\tY = {coeficiente_a}X + {coeficiente_b}")
# print(f"Dados los siguientes puntos: \n\tP1 ({coeficiente_x1}, {coeficiente_y1}) \n\tP2 ({coeficiente_x2}, {coeficiente_y2})")
#
# distancia_entre_dos_puntos =  math.sqrt( ( math.pow(coeficiente_x2 - coeficiente_x1, 2) ) + ( math.pow(coeficiente_y2 - coeficiente_y1, 2) ) )
# print(f"La distancia entre ellos es: {distancia_entre_dos_puntos}")

# # Ejercicio 6
# año = int(input("Ingresar año:"))
# if año % 400 == 0 or (año % 4 == 0 and año % 100 != 0):
#     print("es bisiesto")
# else:
#     print("no es bisiesto")
#

