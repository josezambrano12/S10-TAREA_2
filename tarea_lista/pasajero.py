class Pasajero:
    """Representa a un pasajero de la aerolínea."""

    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula      # texto de 10 dígitos, no se repite (es la clave)
        self.edad = edad

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def __str__(self):
        return f"{self.nombre:<8} | {self.cedula} | {self.edad:>2} años"
