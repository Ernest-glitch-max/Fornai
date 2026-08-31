nombre = input("Ingresa el nombre del jugador: ")
nivel = int(input("Ingresa tu nivel: "))
posicion = int(input("Ingresa tu posición final: "))

print(f"Jugador: {nombre}")
print(f"Nivel: {nivel}")
print(f"Posición final: {posicion}")

if posicion == 1:
    print("¡VICTORIA MAGISTRAL!")
elif posicion <= 10:
    print("¡Top 10 alcanzado! Buen trabajo")
elif posicion <= 50:
    print("Llegaste al Top 50")
else:
    print("Eliminado temprano, ¡inténtalo de nuevo!")

print("Partida finalizada.")