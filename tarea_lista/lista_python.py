from bisect import bisect_left
from pasajero import Pasajero


class ListaPasajerosPython:
    """Lo mismo que la lista manual, pero con los métodos de list de Python."""

    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):
        if self.buscar(pasajero.cedula) != -1:
            print("La cédula ya existe")
            return False
        self.pasajeros.append(pasajero)
        return True

    def listar(self):
        if not self.pasajeros:
            print("(lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"[{i}] {p}")

    def longitud(self):
        return len(self.pasajeros)

    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > len(self.pasajeros):
            print("Posición no válida")
            return False
        if self.buscar(pasajero.cedula) != -1:
            print("La cédula ya existe")
            return False
        self.pasajeros.insert(posicion, pasajero)
        return True

    def buscar(self, cedula):
        posiciones = [i for i, p in enumerate(self.pasajeros) if p.cedula == cedula]
        return posiciones[0] if posiciones else -1

    def buscar_binaria(self, cedula):
        # la lista tiene que estar ordenada por cédula
        cedulas = [p.cedula for p in self.pasajeros]
        i = bisect_left(cedulas, cedula)
        if i < len(cedulas) and cedulas[i] == cedula:
            return i
        return -1

    def modificar(self, cedula, nuevo_nombre, nueva_edad):
        pos = self.buscar(cedula)
        if pos == -1:
            print("No existe")
            return False
        self.pasajeros[pos].nombre = nuevo_nombre
        self.pasajeros[pos].edad = nueva_edad
        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= len(self.pasajeros):
            print("Posición no válida")
            return None
        return self.pasajeros.pop(posicion)

    def eliminar_por_valor(self, cedula):
        # armo una lista nueva sin esa cédula (no se borra mientras se recorre)
        antes = len(self.pasajeros)
        self.pasajeros = [p for p in self.pasajeros if p.cedula != cedula]
        return len(self.pasajeros) < antes

    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.cedula)

    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.cedula, reverse=True)

    def reversar(self):
        self.pasajeros.reverse()

    def copiar(self):
        nueva = ListaPasajerosPython()
        nueva.pasajeros = self.pasajeros.copy()
        return nueva

    def filtrar_mayores_de_edad(self):
        nueva = ListaPasajerosPython()
        nueva.pasajeros = [p for p in self.pasajeros if p.es_mayor_de_edad()]
        return nueva

    def nombres_en_mayusculas(self):
        return [p.nombre.upper() for p in self.pasajeros]