class Registro:
    def __init__(self, temperatura, humedad, presion):
        self.temperatura = temperatura
        self.humedad = humedad
        self.presion = presion


class Meteorologia:
    def __init__(self, archivo):
        self.datos = []
        with open(archivo) as f:
            for line in f:
                dia, hora, temperatura, humedad, presion = line.strip().split(",")
                registro = Registro(float(temperatura), float(humedad), float(presion))
                dia = int(dia)
                hora = int(hora)
                if len(self.datos) < dia:
                    self.datos.append([])
                if len(self.datos[dia - 1]) < hora:
                    self.datos[dia - 1].append(None)
                self.datos[dia - 1][hora - 1] = registro

    def min_max(self):
        for i in range(3):
            min_registro = None
            max_registro = None
            for dia in range(len(self.datos)):
                for hora in range(len(self.datos[dia])):
                    registro = self.datos[dia][hora]
                    if registro is not None:
                        if min_registro is None or getattr(
                            registro, ["temperatura", "humedad", "presion"][i]
                        ) < getattr(
                            min_registro, ["temperatura", "humedad", "presion"][i]
                        ):
                            min_registro = registro
                            min_dia = dia + 1
                            min_hora = hora + 1
                        if max_registro is None or getattr(
                            registro, ["temperatura", "humedad", "presion"][i]
                        ) > getattr(
                            max_registro, ["temperatura", "humedad", "presion"][i]
                        ):
                            max_registro = registro
                            max_dia = dia + 1
                            max_hora = hora + 1
            print(f"Variable {['Temperatura', 'Humedad', 'Presion'][i]}:")
            print(
                f"  Minimo: Dia {min_dia}, Hora {min_hora}, Valor {getattr(min_registro, ['temperatura', 'humedad', 'presion'][i])}"
            )
            print(
                f"  Maximo: Dia {max_dia}, Hora {max_hora}, Valor {getattr(max_registro, ['temperatura', 'humedad', 'presion'][i])}"
            )

    def promedio_dia(self):
        for i in range(3):
            print(f"Variable {['Temperatura', 'Humedad', 'Presion'][i]}:")
            for dia in range(len(self.datos)):
                suma = 0
                n = 0
                for hora in range(len(self.datos[dia])):
                    registro = self.datos[dia][hora]
                    if registro is not None:
                        suma += getattr(
                            registro, ["temperatura", "humedad", "presion"][i]
                        )
                        n += 1
                if n > 0:
                    promedio = suma / n
                    print(f"  Dia {dia+1}: {promedio}")

    def promedio_hora(self):
        for i in range(3):
            print(f"Variable {['Temperatura', 'Humedad', 'Presion'][i]}:")
            for hora in range(24):
                suma = 0
                n = 0
                for dia in range(len(self.datos)):
                    if hora < len(self.datos[dia]):
                        registro = self.datos[dia][hora]
                        if registro is not None:
                            suma += getattr(
                                registro, ["temperatura", "humedad", "presion"][i]
                            )
                            n += 1
                if n > 0:
                    promedio = suma / n
                    print(f"  Hora {hora+1}: {promedio}")
