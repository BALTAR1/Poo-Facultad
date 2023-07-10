class Inmueble:
    __localidad = " "
    __direccion = " "
    __supcubierta = " "

    def __init__(self, localidad, direccion, supcubierta):
        self.__localidad = localidad
        self.__direccion = direccion
        self.__supcubierta = supcubierta

    def getLocalidad(self):
        return self.__localidad

    def getDireccion(self):
        return self.__direccion

    def getSupcubierta(self):
        return self.__supcubierta

    def importe():
        pass

    def mostrarDatos(self):
        print("Localidad: ", self.__localidad)
        print("Direccion ", self.__direccion)
        print("Superficie cubierta: ", self.__supcubierta)
