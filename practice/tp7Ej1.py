# 1 a.
def last_name_first_letter(apellido, letra):
    primera_letra = apellido[0]
    if primera_letra.lower() < letra.lower():
        return f"El apellido {apellido} comienza con una letra que está antes de la {letra.upper()}"
    elif primera_letra.lower() > letra.lower():
        return f"El apellido {apellido.title()} comienza con una letra que está después de la {letra.upper()}"
    else:
        return f"El apellido {apellido.title()} comienza con la letra {letra.upper()}"

resultado = last_name_first_letter("Longo", "M")
print(resultado) # Imprime: "El apellido Longo comienza con una letra que está antes de la M"
resultado2 = last_name_first_letter("Ponce", "C")
print(resultado2) # Imprime: "El apellido Ponce comienza con una letra que está después de la C"
resultado3 = last_name_first_letter("Gadea", "G")
print(resultado3) # Imprime: "El apellido Gadea comienza con la letra G"


# 1 b
def name_key(apellido, nombre):
    return apellido[0:3] + nombre[:-1]

last_name = 'Longo'
first_name = 'Juan'
resultado = name_key(last_name, first_name)
print(resultado) #Imprime: La clave generada es: LonJua