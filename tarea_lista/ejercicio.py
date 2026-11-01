def ejercicio_t1():
    from lista_python import ListaPasajerosPython
    from pasajero import Pasajero
    print("T1 — CRUD de pasajeros")
    lista = ListaPasajerosPython()
    for p in (Pasajero("Ana", "0912345678", 28), Pasajero("Luis", "0987654321", 35), Pasajero("Diana", "0923456789", 22)):
        lista.añadir(p)
    print("Inicial:")
    lista.listar()
    print("Buscar Luis:", lista.buscar("0987654321"))
    lista.modificar("0987654321", "Luis Alberto", 36)
    lista.eliminar_por_valor("0912345678")
    print("Tras modificar y eliminar:")
    lista.listar()
    lista.pasajeros.sort(key=lambda p: p.nombre)
    print("Ordenados por nombre:")
    lista.listar()


def ejercicio_t2():
    nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
    notas = [8, 6, 10, 7, 5]
    suma = 0
    maximo = notas[0]
    minimo = notas[0]
    mejor = nombres[0]
    aprobados = 0
    for i in range(len(notas)):
        n = notas[i]
        suma += n
        if n > maximo:
            maximo, mejor = n, nombres[i]
        if n < minimo:
            minimo = n
        if n >= 7:
            aprobados += 1
    print(f"T2 — Estadísticas\n✋ Promedio {suma/len(notas):.2f} · Máx {maximo} ({mejor}) · Mín {minimo} · Aprobados {aprobados} de {len(notas)}")
    promedio = sum(notas) / len(notas)
    mayor = max(notas)
    menor = min(notas)
    aprobados_py = len([n for n in notas if n >= 7])
    print(f"🐍 Promedio {promedio:.2f} · Máx {mayor} ({nombres[notas.index(mayor)]}) · Mín {menor} · Aprobados {aprobados_py} de {len(notas)}")


def ejercicio_t3():
    lista = [5, 2, 8, 1, 9, 3, 7]
    manual = lista[:]
    for vuelta in range(len(manual)-1):
        hubo_swap = False
        for i in range(len(manual)-1-vuelta):
            if manual[i] > manual[i+1]:
                manual[i], manual[i+1] = manual[i+1], manual[i]
                hubo_swap = True
        if not hubo_swap:
            break
    print("T3 — Ordenamiento\n✋", manual)
    print("🐍", sorted(lista))
    copia = lista[:]
    copia.sort(reverse=True)
    print("Descendente:", copia)
    print("Palabras por longitud:", sorted(["python", "a", "código", "el"], key=len))


def ejercicio_p1():
    lista = [1, 3, 2, 3, 4, 3, 5]
    v = 3
    contador = 0
    for x in lista:
        if x == v:
            contador += 1
    print(f"P1 — ✋ {v} aparece {contador} veces")
    print(f"🐍 count={lista.count(v)} · comprensión={len([x for x in lista if x == v])}")


def ejercicio_p2():
    lista = [1, 2, 3, 4, 5]
    manual = []
    for i in range(len(lista)-1, -1, -1):
        manual.append(lista[i])
    print("P2 — ✋", manual)
    print("🐍 slicing:", lista[::-1], "· reversed:", list(reversed(lista)))
    print("Comprensión:", [lista[i] for i in range(len(lista)-1, -1, -1)])


def ejercicio_p3():
    nums = [1, 3, 2, 3, 4, 1, 5, 2]
    unicos = []
    for n in nums:
        if n not in unicos:
            unicos.append(n)
    print("P3 — ✋", unicos)
    print("🐍", list(dict.fromkeys(nums)))
    print("set elimina duplicados, pero no garantiza conservar el orden original")


def ejercicio_p4():
    nums = [5, 2, 9, 7, 9, 3, 8]
    mayor = None
    segundo = None
    for n in nums:
        if mayor is None or n > mayor:
            segundo = mayor
            mayor = n
        elif n != mayor and (segundo is None or n > segundo):
            segundo = n
    print(f"P4 — ✋ Mayor {mayor} · Segundo {segundo}")
    ordenados = sorted(set(nums))
    print(f"🐍 Mayor {ordenados[-1]} · Segundo {ordenados[-2]}")


def ejercicio_p5():
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 10]
    i = j = 0
    resultado = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1
    resultado.extend(a[i:])
    resultado.extend(b[j:])
    print("P5 — ✋", resultado)
    print("🐍", sorted(a+b))


EJERCICIOS = [
    ("T1", "CRUD de pasajeros con clase Pasajero + list", "taller", ejercicio_t1),
    ("T2", "Estadísticas de una lista de notas",          "taller", ejercicio_t2),
    ("T3", "Ordenar una lista (bubble sort)",             "taller", ejercicio_t3),
    ("P1", "Contar apariciones de un valor",              "propuesto", ejercicio_p1),
    ("P2", "Invertir una lista",                          "propuesto", ejercicio_p2),
    ("P3", "Números únicos",                              "propuesto", ejercicio_p3),
    ("P4", "Segundo mayor",                               "propuesto", ejercicio_p4),
    ("P5", "Fusionar dos listas ordenadas",               "propuesto", ejercicio_p5),
]


def menu_ejercicios():
    while True:
        taller = [e for e in EJERCICIOS if e[2] == "taller"]
        propuestos = [e for e in EJERCICIOS if e[2] == "propuesto"]
        print("\n--- DESARROLLADOS (taller) ---")
        for codigo, titulo, _, _ in taller:
            print(f"  {codigo}. {titulo}")
        print("--- PROPUESTOS ---")
        for codigo, titulo, _, _ in propuestos:
            print(f"  {codigo}. {titulo}")
        print("  0. Volver")
        codigo = input("Código: ").strip().upper()
        if codigo == "0":
            break
        encontrados = [e for e in EJERCICIOS if e[0] == codigo]
        if encontrados:
            print()
            encontrados[0][3]()
        else:
            print("Código no válido")