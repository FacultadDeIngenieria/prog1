# Ejercicio 1
text = input()
contains_a = "a" in text
contains_e = "e" in text
contains_i = "i" in text
contains_o = "o" in text
contains_u = "u" in text
print(f"Contiene a: {contains_a}")
print(f"Contiene e: {contains_e}")
print(f"Contiene i: {contains_i}")
print(f"Contiene o: {contains_o}")
print(f"Contiene u: {contains_u}")


# Ejercicio 2
text = input()
contains_a = "á" not in text
contains_e = "é" not in text
contains_i = "í" not in text
contains_o = "ó" not in text
contains_u = "ú" not in text
print(f"No contiene á: {contains_a}")
print(f"No contiene é: {contains_e}")
print(f"No contiene í: {contains_i}")
print(f"No contiene ó: {contains_o}")
print(f"No contiene ú: {contains_u}")


# Ejercicio 3
texto = "Hello, World!"
print(texto[0].lower())
ultima_letra = len(texto) - 1
print(texto[ultima_letra].lower())
print(texto[-2].lower())
print(texto[-ultima_letra-1].lower())

# Ejercicio 4
texto = "Awesome"
print(texto[0:3].lower())
mitad = int(len(texto) / 2)
anterior = mitad - 1
print(texto[mitad - 1:mitad + 2].lower())
print(texto[0:4].lower() + texto[4:].lower())

# Ejercicio 5
texto = "Hello, World!"
print(texto[::-1])

# Ejercicio 6
texto = "Hello, World!"
texto2 = "12345678910"
print(texto[::3])
print(texto2[::3])

# Ejercicio 7
texto = "Hello, World!"
texto2 = "12345678910"

print(texto[4::2])
print(texto2[4::2])

# Ejercicio 8
gases_nobles = "Helio, Neón, Argón, Kriptón, Xenón, Radón, Oganesón"

texto = "Hello, Aurelio"
substring = texto[:2] + texto[-3:]
contains_text = substring in gases_nobles
print(f"La palabra se encuentra dentro de los gases nobles: {contains_text}")

texto2 = "Hello, Matías"
substring2 = texto2[:2] + texto2[-3:]
contains_text2 = substring2 in gases_nobles
print(f"La palabra se encuentra dentro de los gases nobles: {contains_text2}")

# Ejercicio 9
texto = "Hello, Gastón!"
texto_cambiado = texto[:-7] + "Matías" + texto[-1]
print(texto_cambiado)

# Ejercicio 10

texto = "Carlos tiene 19 años"
edad = int(texto[-7:-5])
print(edad)
texto_cambiado = texto[:-7] + str(edad+1) + texto[-5:]
print(texto_cambiado)

texto2 = "Felipe tiene 22 años"
edad2 = int(texto2[-7:-5])
print(edad2)
texto_cambiado2 = texto2[:-7] + str(edad2+1) + texto2[-5:]
print(texto_cambiado2)