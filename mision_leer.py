print("SISTEMA DE CARGA DE DATOS")
print("Iniciando el sistema...")
print()

print("Buscando el archivo guardado_jugador.txt...")

with open("guardado_jugador.txt", "r") as archivo:
    datos_cargados = archivo.read()

print("Archivo encontrado correctamente.")
print()
print("Contenido de los datos guardados:")
print("-----------------------------------")
print(datos_cargados)
print("-----------------------------------")
print()
print("Los datos del jugador fueron cargados correctamente.")
print("Proceso de carga finalizado.")