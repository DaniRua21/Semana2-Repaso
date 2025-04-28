"""Contar cuántas veces aparece un nombre
en la lista."""

nombres = ["Daniel", "Daniel", "Sara", "Johan"]

Contar = nombres.count("Daniel")

print(f"El nombre Daniel aparece {Contar} veces.")

#----------------------------------------------------------------------------------
nombres1 = ["Daniel", "Daniel", "Sara", "Johan"]

nombre_buscado = input("Ingresa un nombre para contar: ")

cantidad = nombres1.count(nombre_buscado)

print(f"El nombre {nombre_buscado} aparece {cantidad} veces.")



