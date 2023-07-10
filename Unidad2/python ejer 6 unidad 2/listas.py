from clases import viajeroFrecuente2
import csv


class manejadorViajeros:
    __listaviajeros = []

    def __init__(self):
        self.__listaviajeros = []

    def agregarViajero(self, unViajero):
        self.__listaviajeros.append(unViajero)

    def testViajero(self):
        archivo = open("ViajeroFrecuente.csv")
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
            numeroviajero = int(fila[0])
            dni = fila[1]
            nombre = fila[2]
            apellido = fila[3]
            millasacum = int(fila[4])
            unViajero = viajeroFrecuente2(
                numeroviajero, dni, nombre, apellido, millasacum
            )
            self.agregarViajero(unViajero)
        archivo.close()

        i = 0
        while i < len(self.__listaviajeros):
            lista = self.__listaviajeros[i].mostrarDatos()
            i += 1

    def mayorMillas(self):
        viajero_mayor_millas = max(self.__listaviajeros)
        print(viajero_mayor_millas.datosMayorMillas())
