class helado:
    __gramos = None
    __precio = None
    __sabores = []

    def __init__(self, gramos, precio, sabores):
        self.__gramos = gramos
        self.__precio = precio
        self.__sabores = sabores

    def getPeso(self):
        return self.__gramos

    def getPrecio(self):
        return self.__precio

    def getSabores(self):
        return self.__sabores
    
    