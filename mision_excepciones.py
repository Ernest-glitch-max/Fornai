print("SISTEMA DE LECTURA DE ARCHIVOS")
print("Iniciando el programa...")
print()

nombre_archivo = input("Ingresa el nombre del archivo que deseas abrir: ")

print()
print(f"Intentando abrir el archivo: {nombre_archivo}")
print()

try:
    with open(nombre_archivo, "r") as archivo:
        datos = archivo.read()

    print("Archivo abierto correctamente.")
    print()
    print("Contenido del archivo:")
    print("-----------------------------------")
    print(datos)
    print("-----------------------------------")
    print()
    print("La información fue leída correctamente.")

except FileNotFoundError:
    print("No se pudo encontrar el archivo.")
    print(f"El archivo '{nombre_archivo}' no existe o el nombre fue escrito incorrectamente.")
    print("Verifica el nombre del archivo e inténtalo nuevamente.")

print()
print("Programa finalizado.")