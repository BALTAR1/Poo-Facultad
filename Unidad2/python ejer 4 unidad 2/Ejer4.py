class Ventana:
    __titulo = " "
    __y1 = " "
    __x1 = " "
    __y2 = " "
    __x2 = " "

    def __init__(self, titulo="", y1=0, x1=0, y2=500, x2=500):
        self.__titulo = titulo
        self.__y1 = int(y1)
        self.__x1 = int(x1)
        self.__y2 = int(y2)
        self.__x2 = int(x2)

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return {self.__y1} - {self.__x1}

    def ancho(self):
        return {self.__y2} - {self.__x2}

    def mostrar(self):
        print(
            "ventana en :",
            {self.__titulo},
            {self.__y1},
            {self.__x1},
            {self.__y2},
            {self.__x2},
        )

    def moverDerecha(self, valor=1):
        self.__x1 += valor
        self.__x2 += valor

    def moverIzquierda(self, valor):
        self.__y1 -= valor
        self.__y2 -= valor

    def bajar(self, y1=1, y2=1):
        self.__y1 -= y1
        self.__y2 -= y2

    def subir(self, y1=1, y2=1):
        self.__y1 += y1
        self.__y2 += y2
