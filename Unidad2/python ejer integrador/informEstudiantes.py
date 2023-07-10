from InformarPromedio import informarPromedio
from informarEstudiantes import InformarAprobados
from ListaOrdenada import MostrarLisOrdenado


def menu(arre, list):
    print("************Menu de Opciones**************")
    print("a - Informar Promedio de Alumno")
    print("b - Informar Estudiantes que aprobaron una Materia")
    print("c - Mostrar Ordenado Listado de alumnos")
    print("0 - Finalizar Operancion")
    print("**************************************")
    op = str(input("Ingrese una opcion--->"))
    while op != "0":
        if op == "a":
            informarPromedio(arre, list)
        elif op == "b":
            InformarAprobados(arre, list)
        elif op == "c":
            MostrarLisOrdenado(arre, list)
        else:
            print("Opcion Incorrecta")
        if op != "0":
            print()
            print("************Menu de Opciones**************")
            print("a - Informar Promedio de Alumno")
            print("b - Informar Estudiantes que aprobaron una Materia")
            print("c - Mostrar Ordenado Listado de alumnos")
            print("0 - Finalizar Operancion")
            print("**************************************")
            op = str(input("Ingrese una opcion--->"))
    print("Finalizando...")
