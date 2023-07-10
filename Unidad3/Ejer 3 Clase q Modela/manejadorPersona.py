from claseIns import Insripcion
from clasePersona import Persona
from claseTaller import Taller


class manejadorP:
    __listaP = []

    def __init__(self):
        self.__listaP = []

    def agregar(self, persona):
        self.__listaP.append(persona)

    def testPer(self):
        i = 0
        while i < len(self.__listaP):
            print("--------------------------")
            print("Nombre:", self.__listaP[i].getNombreP())
            print("Direccion:", self.__listaP[i].getDireccion())
            print("Dni:", self.__listaP[i].getDniP())
            print("--------------------------")
            i += 1
