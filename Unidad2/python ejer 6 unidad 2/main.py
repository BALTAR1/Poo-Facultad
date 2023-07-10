from clases import viajeroFrecuente2
from listas import manejadorViajeros

if __name__ == "__main__":
    lista1 = manejadorViajeros()

    while True:
        print("----------------------")
        print("===MENU DE OPCIONES===")
        print("\na--Mostrar Datos: ")
        print("\nb--Viajero/s con mayor millas acumuladas: ")
        print("\nc--Acumular millas: ")
        print("\nd--Canjear Millas: ")
        print("\ne--Finalizar sesion: ")
        opcion = input("\nSeleccione una opcion: ")

        if opcion == "a":
            print("\n==Datos de la lista cargada==")
            lista1.testViajero()
        else:
            if opcion == "b":
                lista1.mayorMillas()
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
                            break
