from lista import manejadorC
from clases import viajeroFrecuente2
import csv

if __name__ == "__main__":
    listaV = manejadorC()

    while True:
        print("----------------------")
        print("===MENU DE OPCIONES===")
        print("\na--Mostrar Datos: ")
        print("\nb--Viajero/s con mayor millas acumuladas: ")
        print("\nc--Acumular millas: ")
        print("\nd--Canjear Millas: ")
        print("\ne--Comparar millas acum: ")
        opcion = input("\nSeleccione una opcion: ")

        if opcion == "a":
            print("\n==Datos de la lista cargada==")
            listaV.testV()
        else:
            if opcion == "b":
                listaV.mayorM()
            else:
                if opcion == "c":
                    v = viajeroFrecuente2(123, "12345678A", "Juan", "Pérez", 1000)
                    v = v + 100
                    print(v)
                else:
                    if opcion == "d":
                        v2 = viajeroFrecuente2(
                            125, "12335778A", "Sofi", "Rodriguez", 500
                        )
                        v2 = v2 - 100
                        print(v2)
                    else:
                        if opcion == "e":
                            v3 = viajeroFrecuente2(
                                135, "12335778B", "Carlos", "Fuentes", 750
                            )
                            v3 = v3 == 750
                            print(v3)
                        else:
                            if opcion == "f":
                                break
