class PlanAhorro:
    __codigoplan = " "
    __modelo = " "
    __version = " "
    __valor = " "
    __cantCuotas = " "
    __clicitar = " "  # LOS ULTIMOS 2 ATRIBUTOS SON LOS MISMO PARA TODOS LOS PLANES

    def __init__(self, codigoplan, modelo, version, valor, cantCuotas, clicitar):
        self.__codigoplan = codigoplan
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor
        self.__CantCuotas = cantCuotas
        self.__clicitar = clicitar

    def mostrarDatos(self):
        print("El codigo del plan es:", self.__codigoplan)
        print("El modelo es:", self.__modelo)
        print("La version es:", self.__version)
        print("El valor es de: $", self.__valor)
        print("La cantidad de cuotas es de:", self.__cantCuotas)
        print("La cantidad de cuotas pagas para licitar es de:", self.__clicitar)

    def actulizarValorVehiculo(self, nuevoValor):
        print("Codigo del plan: ", self.__codigo)
        print("Modelo: ", self.__modelo)
        print("Version: ", self.__version)
        self.__precio = nuevoValor
        print("Nuevo precio: ", self.__precio)

    def mostrarDatos2(self, cuotas):
        if self.__cantcuotas > cuotas:
            print(
                "\nDatos de vehiculos cuyo valor de la cuota sea inferior al valor dado."
            )
            print("--------------------------------")
            print("Codigo de pla : ", self.__codigo)
            print("Modelo del auto: ", self.__modelo)
            print("Version del auto: ", self.__version)
            print("--------------------------------")

    def modificarCuotas(self, nueva_cuota):
        self.__Cparalicitar = nueva_cuota
        print("Se modifico la cantida de cuotas: ")
