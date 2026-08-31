print("SISTEMA DE RONDAS INICIADO")
print("Preparando la partida...")
print("El jugador comenzará las rondas.")

rondas = int(input("Ingresa el número de rondas que deseas jugar: "))

print()
print("Comenzando la partida...")
print()

for ronda in range(1, rondas + 1):

    print(f"Ronda {ronda} iniciada.")

    if ronda == 3:
        print("Ronda 3: evento especial detectado.")
        print("Se utilizará continue para pasar a la siguiente ronda.")
        print()
        continue

    elif ronda == 5:
        print("Ronda 5: se alcanzó el límite de seguridad.")
        print("Se utilizará break para detener las rondas.")
        print()
        break

    else:
        print(f"Ronda {ronda}: todo está funcionando correctamente.")
        print("La ronda continúa normalmente.")
        print()

print("Partida finalizada.")
print("El sistema ha terminado de procesar las rondas.")