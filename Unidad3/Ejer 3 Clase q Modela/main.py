# from manejadorIns import manejadorIns
from manejadorPersona import manejadorP
from manejadorTaller import manejadorT
from clasePersona import Persona
from manejadorIns import manejadorIns

if __name__ == "__main__":
    mt = manejadorT()
    mp = manejadorP()
    mt.testTaller()
    mi = manejadorIns()

    while True:
        print("---MENU DE OPCIONES---")
        print("(1)Cargar los datos de los talleres")
        print("(2)Inscribir una persona en un taller")
        print("(3)Consultar inscriptos")
        print("(4)OPCINO 4")
        print("(5)Registrar pago")
        print("(6)Guardar inscripciones")
        print("(7)SALIR DEL MENU")
        opcion = input("\nIngrese una opcion: ")

        if opcion == "1":
            mi.agregaIns(mt, mp)

            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            pass
        elif opcion == "7":
            break
