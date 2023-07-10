from ClaseHelado import helado


class manejadorHelado:
    def __init__(self):
        self.helados = []

    def agregarHelado(self, helado):
        self.helados.append(helado)

    def obtenerHelados(self):
        return self.helados