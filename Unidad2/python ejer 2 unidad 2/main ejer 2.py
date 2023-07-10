import csv
from clase import viajerofrecuente

if __name__ == "__main__":
    listas_viajeros = []  # LA LISTA
    with open("datos_viajeros.csv") as archivo:
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
            unviajero = viajerofrecuente(
                fila[0], fila[1], fila[2], fila[3], int(fila[4])
            )
            listas_viajeros.append(unviajero)  # El append agrega al final de la lista
        # unviajero.acumularMillas()

        print(f"--- MENU: ---")
        print(f"[1]. Consultar cantidad de millas")
        print(f"[2]. Acumluar millas")
        print(f"[3]. Canjear millas")
        print(f"[0]. Salir")
        opcion = int(input("Ingrese el numero de opción que desea: "))

        while opcion != 0:
            if opcion == 1:
                print(
                    f"La cantidad de personas cargadas en la lista es de:{len(listas_viajeros)}"
                )
                for viajero in listas_viajeros:  # CON ESTE FOR RECORRO LA LISTAS
                    print(
                        f"La cantidad de millas son: {viajero.cantidadTotaldeMillas()}"
                    )
            elif opcion == 2:
                millasRecorridas = int(input("Ingrese cantidad de millas recorridas: "))
                unviajero.acumularMillas(millasRecorridas)
                acumuladas = int(unviajero.acumularMillas(millasRecorridas))
            elif opcion == 3:
                millasACanjear = int(
                    input("Ingrese la cantidad de millas que desea canjear: ")
                )
                unviajero.canjearMillas(millasACanjear, acumuladas)
            opcion = int(input("Ingrese el numero de opción que desea: "))
