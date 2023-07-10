class Taller:
    __id = " "
    __nombre = " "
    __vacantes = " "
    __monto = " "
    __listIns = list

    def __init__(self, id, nombre, vacantes, monto):
        self.__id = id
        self.__nombre = nombre
        self.__vacantes = vacantes
        self.__monto = monto

    def listTaller(self, listIns):
        self.__listIns.append(listIns)

    def getId(self):
        return self.__id

    def getNombreT(self):
        return self.__nombre

    def vacante(self):
        self.__vacantes -= 1

    def getMonto(self):
        return self.__monto

    def mostrarT(self):
        print("Id: ", self.__id)
        print("Nombre: ", self.__nombre)
        print("Vacantes: ", self.__vacantes)
        print("Monto: ", self.__monto)
        print("---------------")
