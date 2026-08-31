print("SISTEMA DE GUARDADO DEL JUGADOR")
print("Iniciando...")
print()

nombre = input("Ingresa el nombre del jugador: ")
nivel = int(input("Ingresa el nivel del jugador: "))
puntos_victoria = int(input("Ingresa los puntos de victoria: "))

print()
print("Guardando información del jugador...")

with open("guardado_jugador.txt", "w") as archivo:
    archivo.write("INFORMACIÓN DEL JUGADOR\n")
    archivo.write(f"Nombre: {nombre}\n")
    archivo.write(f"Nivel: {nivel}\n")
    archivo.write(f"Puntos de victoria: {puntos_victoria}\n")

print()
print("Los datos del jugador se guardaron correctamente.")
print("El archivo guardado_jugador.txt fue creado.")
print("Puedes encontrarlo en la carpeta del proyecto.")
print()
print("Proceso de guardado finalizado.")