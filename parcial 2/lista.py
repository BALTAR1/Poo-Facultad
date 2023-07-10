from nodo import Nodo
from casa import Casa
from departamentos import Departamentos
from constructora import Inmueble


class Lista:
    __comienzo: Nodo
    __actual = Nodo
    __tope = int
    __indice = int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getInmueble()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def agregarInmueble(self, inmueble):
        nodo = Nodo(inmueble)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
