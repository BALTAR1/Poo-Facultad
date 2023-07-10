class Carrera:
    __codigo = " "
    __nombre = " "
    __fecha = " "
    __duracion = " "
    __titulo = " "

    def __init__(self, codigo, nombre, fecha, duracion, titulo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__fecha = fecha
        self.__duracion = duracion
        self.__titulo = titulo

    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre

    def getFecha(self):
        return self.__fecha

    def getDuracion(self):
        return self.__duracion

    def getTitulo(self):
        return self.__titulo

    def mostrarDatos(self):
        print(self.__codigo)
        print(self.__nombre)
        print(self.__fecha)
        print(self.__duracion)
        print(self.__titulo)
