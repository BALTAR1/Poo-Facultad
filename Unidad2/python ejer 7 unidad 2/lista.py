from clases import viajeroFrecuente2
import csv


class manejadorC:
    __lviajero = []

    def __init__(self):
        self.__lviajero = []

    def agregarV(self, unV):
        self.__lviajero.append(unV)

    def testV(self):
        archi = open("ViajeroFrecuente.csv")
        reader = csv.reader(archi, delimiter=",")
        for fila in reader:
            numeroviajero = int(fila[0])
            dni = fila[1]
            nombre = fila[2]
            apellido = fila[3]
            millasacum = int(fila[4])
            unV = viajeroFrecuente2(numeroviajero, dni, nombre, apellido, millasacum)
            self.__lviajero.append(unV)
        archi.close()

        i = 0

        while i < len(self.__lviajero):
            V = self.__lviajero[i].mostrarDatos()
            i += 1

    def mayorM(self):
        viajero_mayor = max(self.__lviajero)
        print(viajero_mayor.datosMayorMillas())
