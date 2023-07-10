from constructora import Inmueble


class Departamentos(Inmueble):
    __dormitorios = " "
    __nmonoblok = " "
    __numdepartamento = " "
    __numpiso = " "

    def __init__(
        self,
        localidad,
        direccion,
        supcubierta,
        dormitorios,
        nmonoblok,
        numdepartamento,
        numpiso,
    ):
        super().__init__(
            localidad,
            direccion,
            supcubierta,
        )
        self.__dormitorios = dormitorios
        self.__nmonoblok = nmonoblok
        self.__numdepartamento = numdepartamento
        self.__numpiso = numpiso

    def getDormitorios(self):
        return self.__dormitorios

    def getNmonoblok(self):
        return self.__nmonoblok

    def getNumdepartamento(self):
        return self.__numdepartamento

    def getNumpiso(self):
        return self.__numpiso

    def mostrarD(self):
        print(self.__dormitorios)
        print(self.__nmonoblok)
        print(self.__numdepartamento)
