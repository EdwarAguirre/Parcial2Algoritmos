def Promedio(x, y, z):
    promedio = (x + y + z) / 3
    return promedio
    
Numero1 = int(input("Ingrese el primer número entero: "))
Numero2 = int(input("Ingrese el segundo número entero: "))
Numero3 = int(input("Ingrese el tercer número entero: "))

Promedio_resultante = calcular_promedio(numero1, numero2, numero3)
print("El Promedio De Los Tres Números Es:", promedio_resultante)
