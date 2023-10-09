def remove_elements(lista):
    del lista[5]
    del lista[4]
    del lista[0]
    return lista

def add_elements(lista):
    lista.append("Yellow")
    lista.insert("Pink",0)
    return lista

def is_empty(lista):
    return len(lista)== 0

def check_lists(lista_1, lista_2):
    return lista_1[2] == lista_2[2]

def list_of_lists(lista_de_lista):
    return [
        lista_de_lista[0][:2],
        lista_de_lista[1][1:4],
        lista_de_lista[2][-2:]
    ]

print(list_of_lists([[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]))