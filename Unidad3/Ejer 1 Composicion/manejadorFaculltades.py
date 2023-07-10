from claseCarrera import Carrera
from claseFacultad import Facultad
import csv


class manejadorFacultades:
    __listaFacu = []

    def __init__(self):
        self.__listaFacu = []

    def test(self):
        archivo = open("facultades.csv")
        reader = csv.reader(archivo, delimiter=",")
        numFacultad = 0
        for fila in reader:
            if (fila[0]) == numFacultad:
                codigo = fila[1]
                nombreF = fila[2]
                fecha = fila[3]
                duracion = fila[4]
                titulo = fila[5]
                unaCarrera = Carrera(codigo, nombreF, fecha, duracion, titulo)
                self.__listaFacu[fila - 1].agregarCarrera(unaCarrera)

            else:
                numFacultad += 1
                codigo = fila[0]
                nombre = fila[1]
                direccion = fila[2]
                localidad = fila[3]
                telefono = fila[4]
                unaFac = Facultad(codigo, nombre, direccion, localidad, telefono)
                self.agregarFac(unaFac)

        archivo.close()

    def agregarFac(self, unaFac):
        if isinstance(unaFac, Facultad):
            self.__listaFacu.append(unaFac)
        else:
            print("Tipo de carga incorrecta")

    def mostrarDatos(self):
        for facultad in self.__listaFacu:
            print(
                f"{facultad.getCodigoF()}-{facultad.getNombreF()}-{facultad.getDireccion()}-{facultad.getLocalidad()}-{facultad.getTelefono()}"
            )
            for carrera in facultad.getCarrera():
                print(
                    f"{carrera.getCodigo()}-{carrera.getNombre()}-{carrera.getFecha()}-{carrera.getDuracion()}-{carrera.getTitulo()}"
                )

    def BuscarCod(self, codFac):
        for facultad in self.__listaFacu:
            if facultad.getCodigoF() == codFac:
                print(f"{facultad.getNombreF()}")
                for carrera in facultad.getCarrera():
                    print(
                        "Carrera:",
                        carrera.getNombre(),
                        "Duracion:",
                        carrera.getDuracion(),
                    )

    def BuscaNom(self, nomCarre):
        for facultad in self.__listaFacu:
            for carrera in facultad.getCarrera():
                if nomCarre == carrera.getNombre():
                    print("Código:", facultad.getCodigof(), ".", carrera.getCodigo())
                    print("Facultad: ", facultad.getNombreF())
                    print("Duracion: ", carrera.getDuracion())
