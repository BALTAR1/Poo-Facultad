import csv
import numpy as np
from claseIns import Insripcion
from clasePersona import Persona
from manejadorTaller import manejadorT
from manejadorPersona import manejadorP


class manejadorIns:
    __arreglo = []
    __cantidad: int
    __dimension: int

    def __init__(self):
        self.__dimension = 1
        self.__cantidad = 0
        self.__arreglo = np.empty(self.__dimension, dtype=Insripcion)

    def agregaIns(self, unInscripto, mt, mp):
        if self.__cantidad == self.__dimension:
            self.__dimension += 1
            self.__arreglo.resize(self.__dimension)
        else:
            nombre = input("Ingrese un nombre: ")
            direccion = input("Ingrese una direccion: ")
            dni = input("Ingrese un dni: ")
            persona = Persona(nombre, direccion, dni)
            idd = input("Ingrese un id: ")
            idtaller = mt.getid(idd - 1)
            mt.actualizarvacante(idd - 1)
            fecha = input("Ingrese una fecha: ")
            unInscripto = Insripcion(fecha, persona, idtaller)
            mp.agregar(persona)
            self.__arreglo[self.__cantidad] = unInscripto
            self.__cantidad += 1
