class Phone:
    """
    Objeto que representa un número telefónico.
    Contiene el número y el tipo de teléfono que es en forma de entero.
    Tipos de número: 0:celular, 1:casa, 2:trabajo
    """

    # Constructor que crea un Phone con el tipo (int) y el número (int)
    def __init__(self, type, number):
        self.type = type  # phone type (0:cell phone, 1:home, 2:work)
        self.number = number

    # Retorna el tipo de teléfono que es
    # Tipos de número: 0:celular, 1:casa, 2:trabajo
    def get_type(self):
        return self.type

    # Retorna el número de teléfono
    def get_number(self):
        return self.number


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

    # Retorna el nombre del contacto
    def get_name(self):
        return self.name

    # Retorna el dni del contacto
    def get_dni(self):
        return self.dni

    # Retorna todos los teléfonos del contacto
    def get_phones(self):
        return self.phones

    # Busca y retorna el primer teléfono de determinado tipo, si no lo encuentra devuelve -1
    # Tipos de teléfono: 0:celular, 1:casa, 2:trabajo
    def get_phone(self, type):
        for phone in self.phones:
            if phone.type == type:
                return phone
        return -1

    # Agrega un teléfono nuevo (de tipo Phone)
    def add_phone(self, phone):
        self.phones.append(phone)


class Agenda:
    """
    Objeto que representa una agenda de contactos. La agenda está compuesta por una lista de contactos y dicha lista está restringida en tamaño por el valor de number_of_contacts. Es decir, la agenda es finita. El tamaño de la lista contacts no puede pasar el valor de number_of_contacts.
    """

    # Constructor que crea la agenda para una cantidad fija de contactos (number_of_contacts).
    # Crea una lista de objetos tipo Contact vacía.
    def __init__(self, number_of_contacts):
        self.contacts = []
        self.number_of_contacts = number_of_contacts

    # Busca y retorna un contacto por su nombre, retorna -1 si no lo encuentra.
    def find_contact_by_name(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return -1

    # Busca y retorna un contacto por su dni, retorna -1 si no lo encuentra.
    def find_contact_by_dni(self, dni):
        for contact in self.contacts:
            if contact.dni == dni:
                return contact
        return -1

    # Intenta agregar un contacto a la agenda.
    # Retorna True si hay lugar para un nuevo contacto y pudo agregarlo.
    # Retorna False si ya no había lugar.
    def add_contact(self, contact):
        if len(self.contacts) >= self.number_of_contacts:
            return False
        else:
            self.contacts.remove(contact)
            return True

    # Intenta borrar un contacto de la agenda.
    # Retorna True si lo encontró y lo borro. False si no lo encontró.
    def delete_contact(self, contact):
        for i, c in enumerate(self.contacts):
            if c.phone == contact.phones and c.name == contact.name and c.dni == contact.dni:
                del self.contacts[i]
                return True
        return False

    # Retorna True si la agenda ya está llena y no entra ningún contacto nuevo. Devuelve False si la lista no está llena.
    def is_full(self):
        return len(self.contacts) == self.number_of_contacts

    # Retorna la cantidad de espacios libres en la agenda
    def count_free_slots(self):
        return self.number_of_contacts - len(self.contacts)
