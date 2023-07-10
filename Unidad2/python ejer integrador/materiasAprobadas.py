import ManejadorAlumnos as mA
import ManejadorMaterias as mM


# Funcion
def InformarAprobados(arreglo, lista):
    materia = str(input("Ingrese una Materia:"))
    nuevaLista = lista.buscarMaterias(materia)
    if len(nuevaLista) != 0:
        for i in range(lista.tamaño()):
            if (
                lista.getAprobacion(i) == "P"
                and lista.getNota(i) >= 7
                and materia == lista.getMateria(i)
            ):  # condicion
                indice = arreglo.BuscarDni(lista.getDni(i))
                print(
                    "{} {} {} {} {} {}".format(
                        lista.getDni(i),
                        arreglo.getApellido(indice),
                        arreglo.getNombre(indice),
                        lista.getFecha(i),
                        lista.getNota(i),
                        arreglo.getAño(indice),
                    )
                )
    else:
        print("No se encontro ese tipo de Nombre de materia.")
