from ClaseSabor import sabor
import csv


class manejadorSabor:
    __listasabores = []

    def __init__(self):
        self.__listasabores = []

    def cargarSabores(self):
        archivo = open("sabores.csv", encoding="utf-8")
        reader = csv.reader(archivo, delimiter=";")
        for i in reader:
            unSabor = sabor(int(i[0]), i[1], i[2])
            self.__listasabores.append(unSabor)
        print("Sabores cargados con exito!")
        print("-------------------------------------")
        archivo.close()

        i = 0

        while i < len(self.__listasabores):
            self.__listasabores[i].mostrarDatos()
            i += 1

    def agregarSabor(self, sabor):
        self.__listasabores.append(sabor)

    def obtenerSabor(self, idSabores):
        i = 0
        band = False
        while i < len(self.__listasabores):
            if self.__listasabores[i].getIdSabor() == idSabores:
                aux = self.__listasabores.getIdSabor()
                band = True
                print("Sabor: ", sabor.getNombreSabor())
                print("Ingredientes: ", sabor.getIngredientes())
            else:
                print("El id es incorrecto")
            i += 1
