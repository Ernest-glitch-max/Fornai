nivel = int(input("Ingresa tu nivel: "))
oro = int(input("Ingresa la cantidad de oro que posees: "))

if nivel >= 15 and oro >= 100:
    print("¡Portal activado! Teletransportando...")
else:
    print("No cumples con los requisitos para activar el portal.")