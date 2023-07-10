from Clases import PlanAhorro
import csv


class ManejadorPlanes:
    __listaPlanes = []

    def __init__(self):
        self.__listaPlanes = []

    def agregarPlanes(self, unPlan):
        self.__listaPlanes.append(unPlan)

    def testPlanes(self):  # LISTA LOS DATOS
        archivo = open("planes.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            cod = str(fila[0])
            mod = fila[1]
            vers = fila[2]
            pre = fila[3]
            cC = fila[4]
            Clicitar = str(fila[5])
            unPlan = PlanAhorro(cod, mod, vers, pre, cC, Clicitar)
            self.agregarPlanes(unPlan)
        i = 0

        while i < len(self.__listaPlanes):
            plan = self.__listaPlanes[i].mostrarDatos()
            print("---------------------------------")
            # print(plan) no hace falta!!!
            i += 1

    def iniciarValor(self):  # OBTENGO EL NUEVO VALOR DEL PALN DEL AUTO CON NUEVO_VALOR
        i = 0
        while i < len(self.__listaPlanes):
            nuevo_valor = input(
                "\nIngrese el precio actualizado del plan: "
            )  # desde la lista mandamos el precio actualizado a la clase Plan de Ahorro
            print("---------------------------------")
            nuevoplan = self.__listaPlanes[i].actualizarValorVehiculo(
                nuevo_valor
            )  # ponemos la variable que mandamos
            print("---------------------------------")
            i += 1

    def CCuotas(self, cuotas):
        i = 0
        while i < len(self.__listaPlanes):
            mdatos = self.__listaPlanes[i].mostrarDatos2(
                cuotas
            )  # Envia el valor actulizado de cuotas
            i += 1

    def importe(self):
        i = 0
        while i < len(self.__listaPlanes):
            importexcuota = self.__listaPlanes[i].importeCuota()
            print("Importe de cuota de cada plan: ", importexcuota)
            i += 1

    def modificarCuotas(
        self, nueva_cuota
    ):  # Y por que no hago esto en el modulo clases
        self.__Cparalicitar = nueva_cuota
        print("Se modifico la cantida de cuotas: ")
