"""Dada una lista de frutas, pide al usuario
una fruta que quiera eliminar."""

frutas = ["manzana", "mango", "arroz"]

print("Lista de frutas: ", frutas)
eliminar = input("¿Que frutas quieres eliminar? ")

if eliminar in frutas:
    frutas.remove(eliminar)
    print("Fruta eliminada")
else:
    print("La fruta no esta en la lista")

print("Lista actualizada ", frutas)

