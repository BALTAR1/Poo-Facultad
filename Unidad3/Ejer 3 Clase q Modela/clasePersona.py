class Persona:
    __nombre = "string"
    __direccion = "string"
    __dni = "int"
    __listIns = list

    def __init__(self, nombre, direccion, dni):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni

    def listPersona(self, listIns):
        self.__listIns.append(listIns)

    def getNombreP(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def getDniP(self):
        return self.__dni

    # def mostrarDatos(self):
    # return f"Nombre: {self.getNombreP()} (DNI: {self.getDniP()}) - Direccion: {self.getDireccion()}"
