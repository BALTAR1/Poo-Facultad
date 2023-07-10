from clasePersona import Persona
from claseTaller import Taller


class Insripcion:
    __fecha = " "
    __pago = " "
    __persona: Persona
    __taller: Taller

    def __init__(self, fecha, Persona, Taller, pago=False):
        self.__fecha = fecha
        self.__pago = pago
        self.__persona = Persona
        self.__taller = Taller

    def getFecha(self):
        return self.__fecha

    def getPago(self):
        return self.__pago
