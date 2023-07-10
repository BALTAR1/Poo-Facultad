class Email:
    __idcuenta = " "
    __dominio = " "
    __tipodom = " "
    __contraseña = " "

    def __init__(self, idcuenta, dominio, tipodom, contraseña):  # )constructor
        self.__idcuenta = idcuenta
        self.__dominio = dominio
        self.__tipodom = tipodom
        self.__contraseña = contraseña

    def retornaEmail(self):
        return print(f"{self.__idcuenta}@{self.__dominio}.{self.__tipodom}")

    def getdominio(self):
        return print(f"{self.__dominio}")

    def crearcuenta(self, direccion):
        parte1 = direccion.split("@")  # parte1= es un objeto ?
        parte2 = parte1[1].split(".")
        self.__idcuenta = parte1[0]  # [0] es para acceder al elemento 0 de la cadena
        self.__dominio = parte2[0]
        self.__tipodom = parte2[1]

    # def modificarcontrasenia(self, contra):

    # if self__contraseña == contra:
    # self__contraseña ==
