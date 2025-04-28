"""Un programa pide la edad de una persona. Si es mayor de 18, puede votar."""

edad = (input("Digita tu edad"))

if edad >= 18:
    print("Puede votar")
else:
    print("No puedes votar todavia")