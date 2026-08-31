print("Preparando la misión...")
print()

jugador = input("Ingresa el nombre de tu jugador: ")

mochila = [
    "Pico",
    "Botiquín",
    "Mini Poción",
    "Escudo"
]

print()
print(f"Bienvenido, {jugador}.")
print("Tu inventario inicial es:")
print(mochila)
print()

print("Has encontrado un cofre.")
nuevo_objeto = input("Ingresa el nombre del objeto encontrado: ")

mochila.append(nuevo_objeto)

print()
print(f"{nuevo_objeto} ha sido añadido a tu mochila.")
print("Inventario actualizado:")
print(mochila)
print()

print("El jugador ha utilizado el objeto Mini Poción.")
mochila.remove("Mini Poción")

print()
print("La Mini Poción ha sido eliminada del inventario.")
print("Inventario después de utilizar el objeto:")
print(mochila)
print()

print("Objetos actuales de la mochila:")

for objeto in mochila:
    print(f"- {objeto}")

print()
print(f"Cantidad total de objetos: {len(mochila)}")
print()

print("Inventario revisado correctamente.")
print(f"{jugador}, estás listo para continuar la misión.")