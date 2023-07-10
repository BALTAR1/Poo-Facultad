import numpy as np


class conjunto:
    def __init__(self, datos):
        self.datos = np.array(datos, dtype=int)  # pal conjunto de solo enteros

    def __add__(self, other):
        return conjunto(np.union1d(self.datos, other.datos))  # suma de conjuntos

    def __sub__(self, otro):
        return conjunto(np.setdiff(self.datos, otro.datos))  # resta de conjuntos

    def __eq__(self, valor):
        return np.array_equal(self.datos, valor.datos)  # comparar conjuntos
