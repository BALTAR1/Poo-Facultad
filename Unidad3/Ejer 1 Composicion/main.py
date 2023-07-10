from manejadorFaculltades import manejadorFacultades

if __name__ == "__main__":
    mf = manejadorFacultades()
    mf.test()
    mf.mostrarDatos()
    while True:
        print("-------------------------")
        print("MENU DE OPCIONES")
        print("(1)Inciso A")
        print("(2)Inciso B")
        print("(3)SALIR DEL MENU")
        print("------------------------")
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            codFac = input("Ingrese un codigo de una facultad: ")
            print("---------------------")
            mf.BuscarCod(codFac)
        elif opcion == "2":
            nomCarre = input("Ingrese el nombre de una carrera: ")
            print("----------------------")
            mf.BuscaNom(nomCarre)
        elif opcion == "3":
            break
