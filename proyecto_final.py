class Jugador:

    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion
        self.goles = 0

    def anotar_gol(self):
        self.goles = self.goles + 1
        print(f"{self.nombre} ha anotado un gol.")
        print(f"Total de goles de {self.nombre}: {self.goles}")
        print()


class Equipo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_jugadores = []
        self.puntos = 0
        self.goles_favor = 0

    def agregar_jugador(self, jugador):
        self.lista_jugadores.append(jugador)
        print(f"{jugador.nombre} ha sido agregado al equipo {self.nombre}.")

    def mostrar_plantilla(self):
        print()
        print("PLANTILLA DEL EQUIPO")
        print("----------------------------")
        print(f"Equipo: {self.nombre}")
        print(f"Puntos: {self.puntos}")
        print(f"Goles a favor: {self.goles_favor}")
        print()

        print("Jugadores:")

        for jugador in self.lista_jugadores:
            print(
                f"- Nombre: {jugador.nombre} | "
                f"Posición: {jugador.posicion} | "
                f"Goles: {jugador.goles}"
            )

        print("----------------------------")
        print()


jugador1 = Jugador("Ernesto", "Delantero")
jugador2 = Jugador("Carlos", "Portero")
jugador3 = Jugador("Luis", "Defensa")

equipo1 = Equipo("Equipo Ernesto")

equipo1.agregar_jugador(jugador1)
equipo1.agregar_jugador(jugador2)
equipo1.agregar_jugador(jugador3)

print()
print("Simulando una jugada...")
print()

jugador1.anotar_gol()

equipo1.goles_favor = equipo1.goles_favor + 1

print("Información actualizada del equipo:")
equipo1.mostrar_plantilla()