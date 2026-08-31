print("SISTEMA DE JUGADORES")
print("Iniciando programa...")
print()


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


print("Creando jugador...")
jugador1 = Jugador("Ernesto", 50, 1200)

print()
print("Estado inicial:")
jugador1.mostrar_status()

print("El jugador ha conseguido una nueva victoria.")
jugador1.ganar_victoria(150)

print("Estado actualizado:")
jugador1.mostrar_status()

print("Programa finalizado.")