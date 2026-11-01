from pasajero import Pasajero


class ListaPasajerosManual:

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0


    def añadir(self, pasajero):
        if self.buscar(pasajero.cedula) != -1:
            print("La cédula ya existe")
            return False
        if self.cantidad == self.capacidad:
            print("⚠ La lista está llena")
            return False

        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True


    def listar(self):
        if self.cantidad == 0:
            print("(lista vacía)")
            return
        for i in range(self.cantidad):
            print(f"[{i}] {self.datos[i]}")


    def longitud(self):
        return self.cantidad


    def insertar(self, posicion, pasajero):
        if self.cantidad >= self.capacidad:
            print("⚠ La lista está llena")
            return False
        if posicion < 0 or posicion > self.cantidad:
            print("Posición no válida")
            return False
        if self.buscar(pasajero.cedula) != -1:
            print("La cédula ya existe")
            return False
        i = self.cantidad
        while i > posicion:
            self.datos[i] = self.datos[i - 1]
            i -= 1
        self.datos[posicion] = pasajero
        self.cantidad += 1
        return True


    def buscar(self, cedula):
        for i in range(self.cantidad):
            if self.datos[i].cedula == cedula:
                return i
        return -1


    def buscar_binaria(self, cedula):
        izq = 0
        der = self.cantidad - 1
        while izq <= der:
            medio = (izq + der) // 2
            actual = self.datos[medio].cedula
            if actual == cedula:
                return medio
            if actual < cedula:
                izq = medio + 1
            else:
                der = medio - 1
        return -1


    def modificar(self, cedula, nuevo_nombre, nueva_edad):
        pos = self.buscar(cedula)
        if pos == -1:
            print("No existe")
            return False
        self.datos[pos].nombre = nuevo_nombre
        self.datos[pos].edad = nueva_edad
        return True


    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            print("Posición no válida")
            return None
        quitado = self.datos[posicion]
        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad -= 1
        return quitado


    def eliminar_por_valor(self, cedula):
        pos = self.buscar(cedula)
        if pos == -1:
            return False
        self.eliminar_por_posicion(pos)
        return True


    def ordenar_asc(self):
        for vuelta in range(self.cantidad - 1):
            for i in range(self.cantidad - 1 - vuelta):
                if self.datos[i].cedula > self.datos[i + 1].cedula:
                    aux = self.datos[i]
                    self.datos[i] = self.datos[i + 1]
                    self.datos[i + 1] = aux


    def ordenar_desc(self):
        for vuelta in range(self.cantidad - 1):
            for i in range(self.cantidad - 1 - vuelta):
                if self.datos[i].cedula < self.datos[i + 1].cedula:
                    aux = self.datos[i]
                    self.datos[i] = self.datos[i + 1]
                    self.datos[i + 1] = aux


    def reversar(self):
        izq = 0
        der = self.cantidad - 1
        while izq < der:
            aux = self.datos[izq]
            self.datos[izq] = self.datos[der]
            self.datos[der] = aux
            izq += 1
            der -= 1


    def copiar(self):
        nueva = ListaPasajerosManual(self.capacidad)
        for i in range(self.cantidad):
            nueva.añadir(self.datos[i])
        return nueva


    def filtrar_mayores_de_edad(self):
        resultado = ListaPasajerosManual(self.capacidad)
        for i in range(self.cantidad):
            if self.datos[i].es_mayor_de_edad():
                resultado.añadir(self.datos[i])
        return resultado


    def nombres_en_mayusculas(self):
        resultado = [None] * self.cantidad
        for i in range(self.cantidad):
            resultado[i] = self.datos[i].nombre.upper()
        return resultado