from pasajero import Pasajero
from mi_lista import ListaPasajerosManual
from lista_python import ListaPasajerosPython
from ejercicio import menu_ejercicios


lista1 = ListaPasajerosManual(capacidad=10)
lista2 = ListaPasajerosPython()


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    while True:
        nombre = input("  Nombre: ").strip()
        if nombre:
            break
        print("  El nombre no puede estar vacío")
    while True:
        cedula = input("  Cédula (10 dígitos): ").strip()
        if cedula.isdigit() and len(cedula) == 10:
            break
        print("  Debe ingresar 10 dígitos")
    while True:
        edad = leer_entero("  Edad: ")
        if edad >= 0:
            break
        print("  La edad no puede ser negativa")
    return Pasajero(nombre, cedula, edad)


def cargar_datos_prueba(lista):
    antes = lista.longitud()
    lista.añadir(Pasajero("Diana", "0923456789", 22))
    lista.añadir(Pasajero("Ana",   "0912345678", 28))
    lista.añadir(Pasajero("Luis",  "0987654321", 35))
    lista.añadir(Pasajero("Beto",  "0934567890", 16))
    lista.añadir(Pasajero("Elena", "0901234567", 41))
    print(f"  ✓ {lista.longitud() - antes} pasajeros nuevos cargados")


def mostrar_menu_lista(titulo):
    print(f"\n========== {titulo} ==========")
    print(" 1. Añadir pasajero (al final)")
    print(" 2. Listar pasajeros")
    print(" 3. Insertar en una posición")
    print(" 4. Buscar por cédula (lineal)")
    print(" 5. Buscar por cédula (binaria)")
    print(" 6. Modificar pasajero")
    print(" 7. Eliminar por posición")
    print(" 8. Eliminar por cédula (valor)")
    print(" 9. Ordenar ascendente (por cédula)")
    print("10. Ordenar descendente (por cédula)")
    print("11. Reversar")
    print("12. Copiar lista")
    print("13. Longitud")
    print("14. Filtrar mayores de edad")
    print("15. Nombres en mayúsculas")
    print(" C. Cargar datos de prueba")
    print(" 0. Volver")


def menu_lista1():
    while True:
        mostrar_menu_lista("LISTA 1 · desde cero")
        op = input("Opción: ").strip().upper()
        if op == "1":
            p = leer_pasajero()
            if lista1.añadir(p):
                print("  ✓ Pasajero añadido")
        elif op == "2":
            lista1.listar()
        elif op == "C":
            cargar_datos_prueba(lista1)
        elif op == "3":
            pos = leer_entero("  Posición: ")
            p = leer_pasajero()
            if lista1.insertar(pos, p):
                print("  ✓ Insertado")
        elif op == "4" or op == "5":
            if op == "5":
                print("  Recuerda ordenar primero (opción 9)")
            cedula = input("  Cédula: ").strip()
            pos = lista1.buscar(cedula) if op == "4" else lista1.buscar_binaria(cedula)
            if pos == -1:
                print("  No existe")
            else:
                datos = lista1.datos
                print(f"  Encontrado en [{pos}]: {datos[pos]}")
        elif op == "6":
            cedula = input("  Cédula: ").strip()
            nombre = input("  Nuevo nombre: ").strip()
            edad = leer_entero("  Nueva edad: ")
            if lista1.modificar(cedula, nombre, edad):
                print("  ✓ Modificado")
        elif op == "7":
            pos = leer_entero("  Posición: ")
            quitado = lista1.eliminar_por_posicion(pos)
            if quitado is not None:
                print(f"  ✓ Eliminado: {quitado}")
        elif op == "8":
            cedula = input("  Cédula: ").strip()
            if lista1.eliminar_por_valor(cedula):
                print("  ✓ Eliminado")
            else:
                print("  No existe")
        elif op == "9":
            lista1.ordenar_asc()
            lista1.listar()
        elif op == "10":
            lista1.ordenar_desc()
            lista1.listar()
        elif op == "11":
            lista1.reversar()
            lista1.listar()
        elif op == "12":
            copia = lista1.copiar()
            copia.reversar()
            print("--- COPIA (reversada) ---")
            copia.listar()
            print("--- ORIGINAL ---")
            lista1.listar()
        elif op == "13":
            print(f"  Hay {lista1.longitud()} pasajeros")
        elif op == "14":
            lista1.filtrar_mayores_de_edad().listar()
        elif op == "15":
            print(lista1.nombres_en_mayusculas())
        elif op == "0":
            break
        else:
            print("  Opción no válida")

def menu_lista2():
    while True:
        mostrar_menu_lista("LISTA 2 · list de Python")
        op = input("Opción: ").strip().upper()
        if op == "1":
            p = leer_pasajero()
            if lista2.añadir(p):
                print("  ✓ Pasajero añadido")
        elif op == "2":
            lista2.listar()
        elif op == "C":
            cargar_datos_prueba(lista2)
        elif op == "3":
            pos = leer_entero("  Posición: ")
            p = leer_pasajero()
            if lista2.insertar(pos, p):
                print("  ✓ Insertado")
        elif op == "4" or op == "5":
            if op == "5":
                print("  Recuerda ordenar primero (opción 9)")
            cedula = input("  Cédula: ").strip()
            pos = lista2.buscar(cedula) if op == "4" else lista2.buscar_binaria(cedula)
            if pos == -1:
                print("  No existe")
            else:
                datos = lista2.pasajeros
                print(f"  Encontrado en [{pos}]: {datos[pos]}")
        elif op == "6":
            cedula = input("  Cédula: ").strip()
            nombre = input("  Nuevo nombre: ").strip()
            edad = leer_entero("  Nueva edad: ")
            if lista2.modificar(cedula, nombre, edad):
                print("  ✓ Modificado")
        elif op == "7":
            pos = leer_entero("  Posición: ")
            quitado = lista2.eliminar_por_posicion(pos)
            if quitado is not None:
                print(f"  ✓ Eliminado: {quitado}")
        elif op == "8":
            cedula = input("  Cédula: ").strip()
            if lista2.eliminar_por_valor(cedula):
                print("  ✓ Eliminado")
            else:
                print("  No existe")
        elif op == "9":
            lista2.ordenar_asc()
            lista2.listar()
        elif op == "10":
            lista2.ordenar_desc()
            lista2.listar()
        elif op == "11":
            lista2.reversar()
            lista2.listar()
        elif op == "12":
            copia = lista2.copiar()
            copia.reversar()
            print("--- COPIA (reversada) ---")
            copia.listar()
            print("--- ORIGINAL ---")
            lista2.listar()
        elif op == "13":
            print(f"  Hay {lista2.longitud()} pasajeros")
        elif op == "14":
            lista2.filtrar_mayores_de_edad().listar()
        elif op == "15":
            print(lista2.nombres_en_mayusculas())
        elif op == "0":
            break
        else:
            print("  Opción no válida")


def main():
    while True:
        print("\n╔══════════════════════════════════╗")
        print("║   TAREA LISTAS · PASAJEROS ✈     ║")
        print("╚══════════════════════════════════╝")
        print("1. Lista 1 (construida desde cero)")
        print("2. Lista 2 (list de Python)")
        print("3. Listar ejercicios")
        print("4. Salir")
        op = input("Opción: ").strip()

        if op == "1":
            menu_lista1()
        elif op == "2":
            menu_lista2()
        elif op == "3":
            menu_ejercicios()
        elif op == "4":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()