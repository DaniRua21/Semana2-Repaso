"""Agregar un número en una posición
específica."""

numeros = [21,54,45,54,54]

agregar = int(input("Que numero quieres agregar?: "))

posicion = int(input("Escoge la posicion que desea agregar (0-4): "))

numeros.insert(posicion,agregar)    
print("Lista actualizada: ", numeros)