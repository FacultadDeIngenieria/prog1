# 2 a
def agregar_fruta(lista, nueva):
    return lista.append(nueva)

# 2 b
def agregar_color(lista,nuevo, posicion):
    return lista.inser(nuevo,posicion)

# 2 c
def agregar_lista(lista, nueva):
    return lista.append(nueva)

# 2 d
def eliminar_elementos(lista):
    list = lista[:]
    del list[4]
    del list[3]
    del list[2]
    return list

# numeros = [1, 2, 3, 4, 5, 6, 7]
# nueva_lista = eliminar_elementos(numeros)
# print(nueva_lista) # Imprime [1,2,6,7]

# 2 e
def eliminar_elementos_por_valor(lista, palabra):
    indice = lista.index(palabra)
    if indice != -1:
        del lista[indice]
    return lista


# frutas = ["naranja", "banana", "uva", "manzana", "pera", "manzana"]
# nueva_lista = eliminar_elementos_por_valor(frutas,"manzana")
# print(nueva_lista) # Imprime ["naranja", "banana", "uva", "pera", "manzana"]