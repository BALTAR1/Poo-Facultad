class sabor:
    __idSabor = None
    __nombreSabor = None
    __ingredientes = None
    
    
    def __init__(self, idSabor, nombreSabor,ingredientes ):
        self.__idSabor = idSabor
        self.__nombreSabor = nombreSabor
        self.__ingredientes = ingredientes
       
    def getIdSabor(self):
        return self.__idSabor
    def getIngredientes(self):
        return self.__ingredientes
    def getNombreSabor(self):
        return self.__nombreSabor
    def mostrarDatos(self):
        print("Id del sabor: ",self.getIdSabor())
        print("Nombre del Sabor: ",self.getNombreSabor())
        print("Ingredientes: ",self.getIngredientes())
        print("-------------------------------------")
