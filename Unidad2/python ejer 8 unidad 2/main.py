from clases import conjunto
import numpy as np


if __name__ == "__main__":
    conjunto1 = [1, 2, 3]
    conjunto2 = [3, 4, 5, 6]
    while True:
        print("Seleccione una opción:")
        print("1. Unión de conjuntos")
        print("2. Diferencia de conjuntos")
        print("3. Verificar igualdad de conjuntos")
        print("4. Salir del menu")
        opcion = input("Opción: ")

        if opcion == "1":
            union = conjunto1 + conjunto2
            print("Unión de conjuntos: ", union)

        else:
            if opcion == "2":
                conjunto1 = set([1, 2, 3])
                conjunto2 = set([3, 4, 5, 6])
                diferencia = conjunto1 - conjunto2
                print("Diferencia de conjuntos: ", diferencia)
            else:
                if opcion == "3":
                    if conjunto1 == conjunto2:
                        print("Los conjuntos son iguales")
                    else:
                        print("No son iguales")
                        if opcion == "4":
                            break
