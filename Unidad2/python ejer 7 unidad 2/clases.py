class viajeroFrecuente2:
    __num_viajero: int
    __dni: str
    __nombre: str
    __apellido: str
    __millas_acum: int

    # -----Metodos-----

    def __init__(self, num_viajero, dni, nombre, apellido, millas_acum):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum

    def mostrarDatos(self):
        print("--------------------------")
        print("Numero del viajero: ", self.__num_viajero)
        print("dni del viajero: ", self.__dni)
        print("Nombre del viajero: ", self.__nombre)
        print("Apellido del viajero: ", self.__apellido)
        print("Millas acumuladas: ", self.__millas_acum)

    def __gt__(self, otro):
        return self.__millas_acum > otro.__millas_acum

    def datosMayorMillas(self):
        print("Nombre: ", self.__nombre)
        print("Apellido: ", self.__apellido)

    def __add__(self, otro):
        print("Nombre", self.__nombre)
        print("Millas: ", self.__millas_acum + otro)

    def __sub__(self, valor):
        print("Nombre", self.__nombre)
        print("Millas: ", self.__millas_acum - valor)

    def __eq__(self, value):
        if self.__millas_acum == value:
            print("Las millas coinciden")
        else:
            print("Las millas no coinciden")
