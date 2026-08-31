print("SISTEMA DE COMBATE")
print("Iniciando batalla...")
print()


def calcular_ataque(ataques, daño_por_ataque):
    daño_total = ataques * daño_por_ataque
    return daño_total


def recibir_danio(vida, daño):
    vida_actual = vida - daño

    if vida_actual < 0:
        vida_actual = 0

    return vida_actual


vida_jugador = 200

ataques = 5
daño_por_ataque = 30

print("Estado inicial del jugador:")
print(f"Vida: {vida_jugador}")
print()

print("Calculando el ataque...")
daño_total = calcular_ataque(ataques, daño_por_ataque)

print(f"Cantidad de ataques: {ataques}")
print(f"Daño por ataque: {daño_por_ataque}")
print(f"Daño total causado: {daño_total}")
print()

print("El jugador enemigo recibe el ataque.")

vida_enemigo = 300
vida_enemigo = recibir_danio(vida_enemigo, daño_total)

print(f"Vida del enemigo después del ataque: {vida_enemigo}")
print()

print("El enemigo contraataca.")
daño_recibido = 80

vida_jugador = recibir_danio(vida_jugador, daño_recibido)

print(f"Daño recibido por el jugador: {daño_recibido}")
print(f"Vida actual del jugador: {vida_jugador}")
print()

if vida_jugador > 0:
    print("El jugador sigue con vida.")
else:
    print("El jugador ha quedado sin vida.")

print()
print("Combate finalizado.")