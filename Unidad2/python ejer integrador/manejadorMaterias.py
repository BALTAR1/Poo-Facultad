from ClaseMateria import MateriasAprobadas
import csv


class manejadorMaterias:
    __listaMaterias = []

    def __init__(self):
        self.__listaMaterias = []

    def agregarMaterias(self, unaMateria):
        self.__listaMaterias.append(unaMateria)

    def testMaterias(self):
        archivo = open("materiasAprobadas.csv")
        reader = csv.reader(archivo, delimiter=";")
        for i in reader:
            dni = i[0]
            nombre = i[1]
            fecha = i[2]
            nota = i[3]
            aprobacion = i[4]
            unaMateria = manejadorMaterias(dni, nombre, fecha, nota, aprobacion)
            self.__listaMaterias.append(unaMateria)
        archivo.close()

    def buscarNotas(self, dni):
        acum = 0
        contador = 0
        for i in range(len(self.__listaMaterias)):
            if dni == self.__listaMaterias[i].getDni():
                acum += self.__listaMaterias[i].getNota()
                print("Nota: ", self.__listaMaterias[i].getNota())
                contador += 1
        print("Promedio Total: ", acum / contador)

    def buscarMaterias(self, materia):
        listadeDni = []
        for i in range(len(self.__lista)):
            if self.__listaMaterias[i].getNombre() == materia:
                listadeDni.append(self.__listaMaterias[i].getDni())
        return listadeDni

    def tamaño(self):
        return int(len(self.__listaMaterias))

    def getAprobacion(self, indice):
        return self.__listaMaterias[indice].getAprobacion()

    def getDni(self, indice):
        return self.__listaMaterias[indice].getDni()

    def getFecha(self, indice):
        return self.__listaMaterias[indice].getFecha()

    def getNota(self, indice):
        return self.__listaMaterias[indice].getNota()

    def getMateria(self, indice):
        return self.__listaMaterias[indice].getNombre()
