class Personaje:

    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def esta_vivo(self):
        if self.vida > 0:
            return True
        else:
            return False

    def atacar(self, objetivo):
        objetivo.vida = objetivo.vida - self.ataque

        print(f"{self.nombre} atacó a {objetivo.nombre}.")
        print(f"{self.nombre} causó {self.ataque} de daño.")
        
        if objetivo.vida < 0:
            objetivo.vida = 0

        print(f"A {objetivo.nombre} le quedan {objetivo.vida} puntos de vida.")
        print()


p1 = Personaje("Guerrero", 100, 25)
p2 = Personaje("Monstruo", 80, 20)

print("Estado inicial:")
print(f"{p1.nombre}: {p1.vida} de vida y {p1.ataque} de ataque")
print(f"{p2.nombre}: {p2.vida} de vida y {p2.ataque} de ataque")
print()

turno = 1

while p1.esta_vivo() and p2.esta_vivo():

    print(f"Turno {turno}")
    print()

    p1.atacar(p2)

    if p2.esta_vivo():
        p2.atacar(p1)

    turno = turno + 1


print("Batalla finalizada.")
print()

if p1.esta_vivo():
    print(f"El ganador es {p1.nombre}.")
    print(f"Vida restante: {p1.vida}")
else:
    print(f"El ganador es {p2.nombre}.")
    print(f"Vida restante: {p2.vida}")