"""Pregunta si una persona tiene licencia
y si lleva casco. Si no tiene licencia o
no lleva casco, no puede conducir."""

licencia = input("¿Tienes licencia? (Si/No)")
casco = input("¿Tienes casco? (Si/No)")

if licencia != "Si" and casco != "Si":
    print("No puedes conducir, sea responsable")
else:
    print("Dale al tatatata")