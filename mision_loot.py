print("SISTEMA DE INVENTARIO")
print("Cargando mochila del jugador...")
print()

mochila = ["Pico", "Botiquín", "Mini Poción", "Lanzacohetes"]

print("Inventario inicial:")
print(mochila)
print()

print("Has encontrado un cofre.")
print("Recogiendo un nuevo objeto...")
mochila.append("Escopeta Mítica")

print("La Escopeta Mítica ha sido añadida a la mochila.")
print()

print("El jugador utiliza la Mini Poción para ganar escudo.")
mochila.remove("Mini Poción")

print("La Mini Poción ha sido eliminada del inventario.")
print()

print("Inventario actualizado:")
print(mochila)
print()

cantidad = len(mochila)

print("Cantidad total de objetos:")
print(cantidad)

print()
print("Inventario actualizado correctamente.")
print("Revisión de mochila finalizada.")