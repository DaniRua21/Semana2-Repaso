"""Buscar si un número existe en una lista y
encontrar su posición."""

numeros = [3,6,45,15,24]

buscado = int(input("Ingresa un número para buscar: "))

if buscado in numeros:
    posicion = numeros.index(buscado)
    print(f"El número {buscado} esta en la posicion {posicion}")
else:
    print("El numero {buscado} no se encuetra en la lista")
    