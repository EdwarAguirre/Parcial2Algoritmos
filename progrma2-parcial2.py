def Calcular_Superficie_Rectangulo(base, altura):
    superficie = base * altura
    return superficie

print("Ingrese los lados del primer rectángulo:")
Base1 = float(input("Base del primer rectángulo: "))
Altura1 = float(input("Altura del primer rectángulo: "))

print("Ingrese los lados del segundo rectángulo:")
Base2 = float(input("Base del segundo rectángulo: "))
Altura2 = float(input("Altura del segundo rectángulo: "))

superficie1 = calcular_superficie_rectangulo(base1, altura1)
superficie2 = calcular_superficie_rectangulo(base2, altura2)

if superficie1 > superficie2:
    print("El primer rectángulo tiene una superficie mayor:", superficie1)
elif superficie2 > superficie1:
    print("El segundo rectángulo tiene una superficie mayor:", superficie2)
else:
    print("Ambos rectángulos tienen la misma superficie:", superficie1)
