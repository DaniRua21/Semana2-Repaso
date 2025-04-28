"""Pide una nota (0-10). Muestra si
perdio, aprobado o sobresaliente."""


nota = input("digita la nota")

if nota < 5:
    print("perdio")
elif nota >= 5 and nota < 7:
    print("Aprobado")
elif nota >= 7 and nota  <= 10:
    print("Sobresaliente")
else:
    print("Nota invalida")
    