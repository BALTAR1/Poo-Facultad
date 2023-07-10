class viajerofrecuente:
    __num_viajero = " "
    __dni = " "
    __nombre = " "
    __apellido = " "
    __millasacum = 0

    # objeto.atributo = valor
    def __init__(self, num_viajero, dni, nombre, apellido, millasacum):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasacum = int(millasacum)

    def cantidadTotaldeMillas(self):  # Metodo que retorna solo las millas
        return self.__millasacum

    def acumularMillas(self, cant):  # Metod que devuelve las millas acumuladas
        self.__millasacum += int(cant)  # Entonces que contiene cant
        print(f"La cantidad de millas acumuladas es de: {self.__millasacum}")
        return self.__millasacum

    def canjearMillas(
        self, millasACanjear, acumuladas
    ):  # Como funcionan lo de las variables locales
        if millasACanjear <= acumuladas:
            print(f"millas canjeadas")
            return acumuladas
        else:
            print(
                f"No tienes suficientes millas! elige un monto menor o igual a {acumuladas}."
            )
