"""Pregunta si una persona terminó su
tarea. Si no terminó, mostrar "Debes
terminar la tarea"."""

deberes = input("terminaste tus deberes (Si/No)")

if not deberes == "Si":
    print("Debes terminar la tarea")
else:
    print("¡Buen trabajo!")