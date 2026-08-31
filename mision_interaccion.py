class Jugador:

    def __init__(self, nombre, nivel, puntos_victoria):
        self.nombre = nombre
        self.nivel = nivel
        self.puntos_victoria = puntos_victoria

    def mostrar_status(self):
        print("----------------------------")
        print("ESTADO DEL JUGADOR")
        print("----------------------------")
        print(f"Nombre: {self.nombre}")
        print(f"Nivel: {self.nivel}")
        print(f"Puntos de victoria: {self.puntos_victoria}")
        print("----------------------------")
        print()

    def ganar_victoria(self, puntos_ganados):
        self.puntos_victoria = self.puntos_victoria + puntos_ganados
        print(f"{self.nombre} ha ganado {puntos_ganados} puntos de victoria.")
        print(f"Ahora tiene {self.puntos_victoria} puntos de victoria.")
        print()

    def transferir_puntos(self, objetivo, puntos):
        if self.puntos_victoria >= puntos:
            self.puntos_victoria = self.puntos_victoria - puntos
            objetivo.puntos_victoria = objetivo.puntos_victoria + puntos

            print(
                f"{self.nombre} ha transferido {puntos} puntos "
                f"a {objetivo.nombre}."
            )
            print()

        else:
            print(
                f"{self.nombre} no cuenta con suficientes "
                f"puntos para realizar la transferencia."
            )
            print()


jugador1 = Jugador("Ernesto", 50, 1200)
jugador2 = Jugador("Rival", 40, 800)

print("ESTADO INICIAL DE LOS JUGADORES")
print()

jugador1.mostrar_status()
jugador2.mostrar_status()

print("Realizando transferencia de puntos...")
jugador1.transferir_puntos(jugador2, 300)

print("ESTADO FINAL DE LOS JUGADORES")
print()

jugador1.mostrar_status()
jugador2.mostrar_status()

print("Transferencia finalizada correctamente.")