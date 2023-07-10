from lista import Lista
from casa import Casa
from departamentos import Departamentos

if __name__ == "__main__":
    lista = Lista()

    while True:
        print("------MENU DE OPCIONES-------")
        print("-Opcion 1-")
        print("-Opcion 2-")
        print("-Opcion 3-")
        print("--------------------------------")
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            casa1 = Casa("sanjuan", "libertador", 500, 23)
            depto1 = Departamentos("sanjuan", "central", 700, 4, 6, 8, 2)
            lista.agregarInmueble(casa1)
            lista.agregarInmueble(depto1)
        elif opcion == "2":
            pass
        elif opcion == "3":
            cant = int(input("Ingrese un numero de dormitorios: "))
            if cant != 0:
                for i in lista:
                    if isinstance(i, Departamentos):
                        if i.getDormitorios() < cant:
                            print(i.mostrarDatos())

        elif opcion == "4":
            for inmueble in lista:
                if isinstance(inmueble, Departamentos):
                    inmueble.mostrarD()
