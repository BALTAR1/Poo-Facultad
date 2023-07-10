from claseCarrera import Carrera


class Facultad:
    __codigo = " "
    __nombreF = " "
    __direccion = " "
    __localidad = " "
    __telefono = " "
    __carrera = []

    def __init__(self, codigo, nombreF, direccion, localidad, telefono):
        self.__codigo = codigo
        self.__nombreF = nombreF
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carrera = []

    def agregarCarrera(self, unaCarrera):
        if isinstance(unaCarrera, Carrera):
            self.__carrera.append(unaCarrera)
        else:
            print("Tipo de carga incorrecta")

    def getCarrera(self):
        return self.__carrera

    def getCodigoF(self):
        return self.__codigo

    def getNombreF(self):
        return self.__nombreF

    def getDireccion(self):
        return self.__direccion

    def getLocalidad(self):
        return self.__localidad

    def getTelefono(self):
        return self.__telefono

    def mostrarDatosF(self):
        print(self.__codigo)
        print(self.__nombreF)
        print(self.__direccion)
        print(self.__localidad)
        print(self.__telefono)
