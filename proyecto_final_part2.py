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
        print("INICIANDO PARTIDO")
        print("----------------------------")
        print(
            f"{self.equipo_local.nombre} vs "
            f"{self.equipo_visitante.nombre}"
        )
        print()

        self.goles_local = 2
        self.goles_visitante = 1

        self.equipo_local.goles_favor += self.goles_local
        self.equipo_visitante.goles_favor += self.goles_visitante

        print("Resultado del encuentro:")
        print(
            f"{self.equipo_local.nombre}: "
            f"{self.goles_local} goles"
        )
        print(
            f"{self.equipo_visitante.nombre}: "
            f"{self.goles_visitante} goles"
        )
        print()

        if self.goles_local > self.goles_visitante:
            self.equipo_local.puntos += 3
            print(f"Ganador: {self.equipo_local.nombre}")
            print("Se asignaron 3 puntos al equipo local.")

        elif self.goles_visitante > self.goles_local:
            self.equipo_visitante.puntos += 3
            print(f"Ganador: {self.equipo_visitante.nombre}")
            print("Se asignaron 3 puntos al equipo visitante.")

        else:
            self.equipo_local.puntos += 1
            self.equipo_visitante.puntos += 1
            print("El partido terminó en empate.")
            print("Cada equipo recibió 1 punto.")

        print("----------------------------")
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


partido = Partido(equipo1, equipo2)

partido.jugar_partido()


print("TABLA ACTUALIZADA")
print("============================")

equipo1.mostrar_plantilla()
equipo2.mostrar_plantilla()

print("Fin de la simulación.")