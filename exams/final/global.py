# Introducción a la Programación I
# Recuperatorio Global
#
#
# ¿Cuál de los siguientes es Verdadero cuando el valor de a es igual al valor de b o cuando a es igual a 5?
b = 5
a = 5

print( a == b == 5)
# print("a = b or a = 5 " + a = b or a = 5)
print(a == b or a == 5)
print("2")
# D. a = b and a = 5
# E. a == b and a = 5

# A. a == b == 5
# B. a = b or a = 5
# => C. a == b or a == 5
# D. a = b and a = 5
# E. a == b and a = 5
#

# Escribir un programa que pida un input al usuario, lo convierta a float e imprima si ese número es negativo, positivo o cero. Resultado esperado siendo X el número que ingresa el usuario (usar los mensajes):
# Si el número es positivo, imprimir: “El número X es positivo”.
# Si el número es negativo, imprimir: “El número X es negativo”.
# Si el número es cero, imprimir: “El número X es cero”.
#

def positividad():
    number = int(input("Ingrese un número"))
    if number > 0:
        print(f"El número {number} es positivo")
    elif number <0:
        print(f"El número {number} es negativo")
    else:
        print(f"El número {number} es positivo")

# Escribir la función palindrome que devuelve un Boolean indicando si el String que recibe como argumento contiene los mismos caracteres de adelante para atrás que de atrás para adelante.
#
# Ejemplo:
# palindrome("neuquen")  # devuelve True
# palindrome("agustin")  # devuelve False
#

def palindrome(word):
    half = len(word) // 2
    count = 0
    last = len(word)
    while count <= half:
        if word[count] != word[last - count -1]:
            return False
        count += 1
    return True

print(palindrome("neuquen"))
print(palindrome("neuquen2"))
print(palindrome("agustin"))


# Escribir la función power que reciba dos parámetros ‘a’ y ‘b’ de tipo integer y retorne el resultado de ‘a’ elevado a la ‘b’. El ejercicio debe realizarse usando recursión (no se puede usar ** ni ninguna función que realice la cuenta directamente sin usar recursividad).
#
# Por ejemplo: dado un ‘a’ con valor 2 y un ‘b’ con valor 3, la función debe retornar 8 como resultado.
#
# power(2, 3) # devuelve 8
#


def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp -1)
#
# Escribir una función print_xo_count que dada una lista de listas de Strings, cuente la cantidad de ‘X’ y de ‘O’ y las imprima en pantalla. Cualquier otro valor debería ser ignorado.
#
# Ejemplo:
#
# multi_strings = [["X","O","O"],["O","X","O"],["O","O","X"]]
# print_xo_count(multi_strings)    # muestra lo siguiente en pantalla

def print_xo_count(list):
    x = 0
    o = 0
    i = 0
    while i < len(list):
        j = 0
        while j < len(list[i]):
            v = list[i][j]
            if v == "X":
                x +=1
            elif v == "O":
                o +=1
            j+=1
        i+=1
    print(f"Cantidad de X: {x}\nCantidad de O: {o}")

multi_strings = [["X","O","O"],["O","X","O"],["O","O","X"]]
print_xo_count(multi_strings)    # muestra lo siguiente en pantalla
#
# Cantidad de X: 3
# Cantidad de O: 6
#
# Dado el siguiente código, escriba la clase Televisor.
#
#    samsung = Televisor(“Samsung Q60R”)
#    samsung.on()
#    samsung.channel(20)
#    print(samsung.to_string())
#    # El televisor Samsung Q60R está en el canal 20.
#
#    lg = Televisor(“LG 4K”)
#    lg.channel(17)
#    print(lg.to_string())
#    # El televisor LG 4K está apagado.
#
#
class Televisor:
    def __init__(self, model):
        self.model = model
        self.is_on = False
        self.current_channel = 0

    def on(self):
        self.is_on = True

    def channel(self, ch):
        self.current_channel = ch

    def to_string(self):
        if self.is_on:
            return f"El televisor {self.model} está en el canal {self.current_channel}"
        else:
            return f"El televisor {self.model} está apagado"

samsung = Televisor("Samsung Q60R")
samsung.on()
samsung.channel(20)
print(samsung.to_string())
# El televisor Samsung Q60R está en el canal 20.

lg = Televisor("LG 4K")
lg.channel(17)
print(lg.to_string())
# El televisor LG 4K está apagado.

class Contact:
    """
    Objeto que representa un contacto.
    Contiene el nombre de la persona (string), el número de dni (int), y sus teléfonos (lista de Phone).
    Un contacto puede tener más de un tipo de teléfono. Por ejemplo, una persona tiene 2 celulares, uno laboral y otro personal.
    """

    # Constructor que crea un contacto con el nombre y el dni de la persona
    def __init__(self, name, dni):
        self.name = name
        self.dni = dni
        self.phones = []

c1 = Contact("a",1)
c2 = Contact("b",2)
c3 = Contact("c",3)

class Agenda:
    """
    Objeto que representa una agenda de contactos. La agenda está compuesta por una lista de contactos y dicha lista está restringida en tamaño por el valor de number_of_contacts. Es decir, la agenda es finita. El tamaño de la lista contacts no puede pasar el valor de number_of_contacts.
    """

    # Constructor que crea la agenda para una cantidad fija de contactos (number_of_contacts).
    # Crea una lista de objetos tipo Contact vacía.
    def __init__(self, number_of_contacts):
        self.contacts = []
        self.number_of_contacts = number_of_contacts

    def add_contact(self, contact):
        if len(self.contacts) >= self.number_of_contacts:
            return False
        else:
            self.contacts.append(contact)
            return True

    def delete_contact(self, contact):
        for i, c in enumerate(self.contacts):
            if c == contact:
                self.contacts.remove(c)
                return True
        return False

agenda = Agenda(20)
agenda.add_contact(c1)
agenda.add_contact(c2)
agenda.add_contact(c3)


agenda.delete_contact(c3)
