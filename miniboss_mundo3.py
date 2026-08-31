print("EVENTO! El jugador encuentra un miniboss")

respuesta = input("El jugador encuentra un miniboss, ¿desea enfrentarlo? (si/no): ")

if respuesta.lower() == "si":
    print("El jugador enfrentará al miniboss")
    print("¡La batalla comienza!")
    print("+50 XP por enfrentarlo")
else:
    print("El jugador decidió no enfrentarlo")
    print("El jugador continúa su aventura.")

    nombre = input("Ingresa tu nombre de usuario: ")
nivel = int(input("Ingresa tu nivel actual: "))
costo = int(input("Ingresa el costo del pase de batalla: "))
pavos = int(input("Ingresa los pavos u oro que posees: "))

nivel_suficiente = nivel >= 10
pavos_restantes = pavos - costo
pavos_suficientes = pavos >= costo

print(f"Jugador: {nombre}")
print(f"¿Tiene nivel suficiente?: {nivel_suficiente}")
print(f"Pavos/oro restantes: {pavos_restantes}")
print(f"¿Tiene suficientes pavos/oro?: {pavos_suficientes}")

