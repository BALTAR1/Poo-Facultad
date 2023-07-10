from Clases import PlanAhorro
import csv
from generalist import ManejadorPlanes

if __name__ == "__main__":
    lista = ManejadorPlanes()
    while True:
        print("\n(a)MENU DE OPCIONES:")
        print("\n(b)Valores cargados en la lista")
        print("\n(c)Datos cuyo valor de la cuota sea inferior al valor dado--")
        print("\n(d)Importe que se debe haber pagado para licitar--")
        print("\n(e)Modificar la cantidad de cuotas pagas para licitar--")
        print("\n(f)SALIR DEL MENU\n")
        opcion = input("\nIngrese la opcion que desee:")

        if opcion == "a":
            print("--DATOS DE LA LISTA--")
            lista.testPlanes()
        else:
            if opcion == "b":
                lista.iniciarValor()
            else:
                if opcion == "c":
                    cuotas = input("Ingrese la cantidad de cuotas: ")
                    lista.CCuotas
                else:
                    if opcion == "d":
                        lista.importe
                    else:
                        if opcion == "e":
                            lista.modificarCuotas
                        else:
                            if opcion == "f":
                                break
                            else:
                                print("opcion no valida")
