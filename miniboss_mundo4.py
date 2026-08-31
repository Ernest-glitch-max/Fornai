nivel = int(input("Ingresa tu nivel: "))
oro = int(input("Ingresa la cantidad de oro que tienes: "))

if nivel >= 15 and oro >= 100:
    print("Portal activado. Teletransportando...")
elif nivel >= 10 or oro >= 50:
    print("Casi cumples los requisitos para activar el portal.")
else:
    print("No cumples con los requisitos para activar el portal.")