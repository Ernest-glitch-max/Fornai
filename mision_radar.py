print("Sistema de radar iniciado")
print("Preparando escaneo de la zona...")
print("Iniciando búsqueda de amenazas...")
print()

for km in range(1, 6):
    if km == 3:
        print("¡AMENAZA CRÍTICA DETECTADA en el km 3! Deteniendo radar...")
        break
    else:
        print(f"Escaneando km {km}... Zona despejada.")

print()
print("El radar ha detenido la búsqueda.")
print("Se ha detectado una amenaza crítica.")
print("No se continuará con el escaneo de los siguientes kilómetros.")
print("Escaneo finalizado.")