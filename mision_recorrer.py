print("SISTEMA DE MOCHILA")
print("Cargando inventario del jugador...")
print()

mochila = [
    "Pico",
    "Botiquín",
    "Mini Poción",
    "Lanzacohetes",
    "Escopeta Mítica"
]

print("Inventario del jugador:")
print()

for objeto in mochila:
    print(f"- Equipado: {objeto}")

print()
print("Revisión del inventario completada.")
print(f"Cantidad total de objetos: {len(mochila)}")
print("Todos los objetos han sido registrados correctamente.")