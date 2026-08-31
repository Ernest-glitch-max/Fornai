nombre = input("Ingresa el nombre del jugador: ")
nivel = int(input("Ingresa tu nivel: "))
escudo = int(input("Ingresa tu escudo actual: "))

print(f"Jugador: {nombre}")
print(f"Nivel: {nivel}")
print(f"Escudo actual: {escudo}")

if escudo >= 50:
    print("¡Escudo óptimo! Estás listo para el combate.")
    
    if nivel >= 10:
        print("Puedes enfrentarte al miniboss.")
    else:
        print("Necesitas subir de nivel antes de enfrentarte al miniboss.")
else:
    print("¡Peligro! Escudo muy bajo, busca pociones antes de luchar.")
    
    if escudo < 20:
        print("Tu escudo está demasiado bajo.")
    else:
        print("Recupera un poco más de escudo antes de luchar.")