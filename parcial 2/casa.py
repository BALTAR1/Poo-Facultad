from constructora import Inmueble


class Casa(Inmueble):
    __metros = " "

    def __init__(self, localidad, direccion, supcubierta, metros):
        super().__init__(localidad, direccion, supcubierta)
        self.__metros = metros

    def getMetros(self):
        return self.__metros
