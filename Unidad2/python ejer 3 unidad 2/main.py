from clases import Registro
from claseRegistro import Meteorologia

if __name__ == "__main__":
    while True:
        print("Menu de opciones:")
        print("1. Mostrar mínimo y máximo de cada variable.")
        print("2. Mostrar promedio diario de cada variable.")
        print("3. Mostrar promedio horario de cada variable.")
        print("4. Salir.")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            Meteorologia.min_max()
        elif opcion == "2":
            Meteorologia.promedio_dia()
        elif opcion == "3":
            Meteorologia.promedio_hora()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    while True:
        print("Menu de opciones:")
        print("1. Mostrar mínimo y máximo de cada variable.")
        print("2. Mostrar promedio diario de cada variable.")
        print("3. Mostrar promedio horario de cada variable.")
        print("4. Salir.")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            Meteorologia.min_max()
        elif opcion == "2":
            Meteorologia.promedio_dia()
        elif opcion == "3":
            Meteorologia.promedio_hora()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
