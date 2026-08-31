print("SISTEMA DE JUGADORES")
print("Iniciando programa...")
print()


class Jugador:

    def __init__(self, nombre, nivel, puntos_victoria):
        self.nombre = nombre
        self.nivel = nivel
        self.puntos_victoria = puntos_victoria


print("Creando jugador...")
print()

jugador1 = Jugador("Ernesto", 50, 1200)

print("Datos del jugador:")
print("----------------------------")
print(f"Nombre: {jugador1.nombre}")
print(f"Nivel: {jugador1.nivel}")
print(f"Puntos de victoria: {jugador1.puntos_victoria}")
print("----------------------------")

print()
print("El jugador fue creado correctamente.")
print("Todos sus atributos están disponibles.")
print()
print("Programa finalizado.")