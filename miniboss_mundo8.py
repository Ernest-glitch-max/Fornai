print("SISTEMA DE GUARDADO DEL JUGADOR")
print("Iniciando programa...")
print()

while True:
    print("========== MENÚ ==========")
    print("1. Guardar datos del jugador")
    print("2. Leer datos guardados")
    print("3. Salir")
    print("==========================")

    opcion = input("Selecciona una opción: ")

    print()

    if opcion == "1":
        print("GUARDAR DATOS")
        print()

        nombre = input("Ingresa el nombre del jugador: ")
        nivel = int(input("Ingresa el nivel del jugador: "))
        puntos = int(input("Ingresa los puntos de victoria: "))

        with open("guardado_jugador.txt", "w") as archivo:
            archivo.write("DATOS DEL JUGADOR\n")
            archivo.write(f"Nombre: {nombre}\n")
            archivo.write(f"Nivel: {nivel}\n")
            archivo.write(f"Puntos de victoria: {puntos}\n")

        print()
        print("Los datos se guardaron correctamente.")
        print("Archivo creado: guardado_jugador.txt")
        print()

    elif opcion == "2":
        print("LECTURA DE DATOS")
        print()

        try:
            with open("guardado_jugador.txt", "r") as archivo:
                datos_cargados = archivo.read()

            print("Datos guardados:")
            print("--------------------------")
            print(datos_cargados)
            print("--------------------------")

        except FileNotFoundError:
            print("No se encontró el archivo guardado.")
            print("Primero debes guardar los datos del jugador.")

        print()

    elif opcion == "3":
        print("Cerrando el programa...")
        print("Gracias por jugar.")
        break

    else:
        print("Opción no válida.")
        print("Selecciona una opción del 1 al 3.")
        print()

print("Programa finalizado.")