print("SISTEMA DE CÁLCULO DE DAÑO")
print("Iniciando sistema...")
print()


def calcular_daño_total(disparos, daño_por_disparo):
    total = disparos * daño_por_disparo
    return total


print("Calculando el daño causado...")
print()

disparos = 5
daño_por_disparo = 30

total_daño = calcular_daño_total(disparos, daño_por_disparo)

print(f"Cantidad de disparos: {disparos}")
print(f"Daño por disparo: {daño_por_disparo}")
print(f"El daño total causado es: {total_daño}")

print()
print("Cálculo completado correctamente.")
print("El resultado ha sido guardado en la variable total_daño.")