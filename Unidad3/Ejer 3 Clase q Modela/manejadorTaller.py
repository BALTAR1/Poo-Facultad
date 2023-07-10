import numpy as np
from claseTaller import Taller
import csv


class manejadorT:
    __arre = []
    __dimension: int
    __cantidad: int

    def __init__(self):
        self.__dimension = 1
        self.__cantidad = 0
        self.__arre = np.empty(1, dtype=Taller)

    def agregaContrato(self, unTaller):
        if self.__cantidad == self.__dimension:
            self.__dimension += 1
            self.__arre.resize(self.__dimension)
        self.__arre[self.__cantidad] = unTaller
        self.__cantidad += 1

    def testTaller(self):
        archivo = open("Talleres.csv")
        reader = csv.reader(archivo, delimiter=";")

        for linea in reader:
            id = linea[0]
            nombre = linea[1]
            vacantes = linea[2]
            monto = linea[3]
            unTaller = Taller(id, nombre, vacantes, monto)
            self.agregaContrato(unTaller)
        archivo.close()
        i = 0
        while i < len(self.__arre):
            self.__arre[i].mostrarT()
            i += 1

    def getId(self, idd):
        return self.__arre[idd]

    def Actualizarvacante(self, idd):
        self.__arre[idd].vacante()
