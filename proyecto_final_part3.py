class Jugador:

    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion
        self.goles = 0

    def anotar_gol(self):
        self.goles = self.goles + 1
        print(f"{self.nombre} ha anotado un gol.")


class Equipo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_jugadores = []
        self.puntos = 0
        self.goles_favor = 0

    def agregar_jugador(self, jugador):
        self.lista_jugadores.append(jugador)

    def mostrar_plantilla(self):
        print()
        print(f"Equipo: {self.nombre}")
        print(f"Puntos: {self.puntos}")
        print(f"Goles a favor: {self.goles_favor}")
        print("Jugadores:")

        for jugador in self.lista_jugadores:
            print(
                f"- {jugador.nombre} | "
                f"Posición: {jugador.posicion} | "
                f"Goles: {jugador.goles}"
            )

        print()


class Partido:

    def __init__(self, equipo_local, equipo_visitante):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.goles_local = 0
        self.goles_visitante = 0

    def jugar_partido(self):
        print()
        print("SIMULACIÓN DEL PARTIDO")
        print("----------------------------")

        self.goles_local = int(
            input(f"Goles de {self.equipo_local.nombre}: ")
        )

        self.goles_visitante = int(
            input(f"Goles de {self.equipo_visitante.nombre}: ")
        )

        self.equipo_local.goles_favor += self.goles_local
        self.equipo_visitante.goles_favor += self.goles_visitante

        print()
        print("Resultado del partido:")
        print(
            f"{self.equipo_local.nombre}: "
            f"{self.goles_local} goles"
        )
        print(
            f"{self.equipo_visitante.nombre}: "
            f"{self.goles_visitante} goles"
        )

        if self.goles_local > self.goles_visitante:
            self.equipo_local.puntos += 3
            print(f"Ganador: {self.equipo_local.nombre}")
            print("El ganador recibe 3 puntos.")

        elif self.goles_visitante > self.goles_local:
            self.equipo_visitante.puntos += 3
            print(f"Ganador: {self.equipo_visitante.nombre}")
            print("El ganador recibe 3 puntos.")

        else:
            self.equipo_local.puntos += 1
            self.equipo_visitante.puntos += 1
            print("El partido terminó en empate.")
            print("Cada equipo recibe 1 punto.")

        print("----------------------------")
        print()


class Liga:

    def __init__(self):
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def mostrar_tabla_posiciones(self):
        print()
        print("TABLA DE POSICIONES")
        print("============================")

        equipos_ordenados = sorted(
            self.equipos,
            key=lambda equipo: equipo.puntos,
            reverse=True
        )

        posicion = 1

        for equipo in equipos_ordenados:
            print(
                f"{posicion}. {equipo.nombre} | "
                f"Puntos: {equipo.puntos} | "
                f"Goles a favor: {equipo.goles_favor}"
            )
            posicion += 1

        print("============================")
        print()

    def guardar_liga(self, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            archivo.write("TABLA DE POSICIONES\n")
            archivo.write("============================\n")

            for equipo in self.equipos:
                archivo.write(
                    f"Nombre: {equipo.nombre} | "
                    f"Puntos: {equipo.puntos} | "
                    f"Goles a favor: {equipo.goles_favor}\n"
                )

        print()
        print("Los datos de la liga se guardaron correctamente.")
        print(f"Archivo creado: {nombre_archivo}")
        print()


jugador1 = Jugador("Ernesto", "Delantero")
jugador2 = Jugador("Carlos", "Portero")
jugador3 = Jugador("Luis", "Defensa")

jugador4 = Jugador("Rival", "Delantero")
jugador5 = Jugador("Pedro", "Portero")
jugador6 = Jugador("Miguel", "Defensa")


equipo1 = Equipo("Equipo Ernesto")
equipo2 = Equipo("Equipo Rival")


equipo1.agregar_jugador(jugador1)
equipo1.agregar_jugador(jugador2)
equipo1.agregar_jugador(jugador3)

equipo2.agregar_jugador(jugador4)
equipo2.agregar_jugador(jugador5)
equipo2.agregar_jugador(jugador6)


liga = Liga()

liga.agregar_equipo(equipo1)
liga.agregar_equipo(equipo2)


while True:

    print("MENÚ PRINCIPAL")
    print("============================")
    print("1. Ver tabla de posiciones")
    print("2. Simular un partido")
    print("3. Guardar datos de la liga")
    print("4. Salir")
    print("============================")

    try:
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:

            liga.mostrar_tabla_posiciones()

        elif opcion == 2:

            partido = Partido(equipo1, equipo2)
            partido.jugar_partido()

        elif opcion == 3:

            liga.guardar_liga("liga_datos.txt")

        elif opcion == 4:

            print("Saliendo del programa...")
            break

        else:

            print("Opción no válida.")
            print("Selecciona una opción del 1 al 4.")
            print()

    except ValueError:

        print()
        print("Error: debes ingresar un número.")
        print("Selecciona una opción del 1 al 4.")
        print()