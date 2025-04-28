"""Pide la edad y clasifica: niño,
adolescente, adulto, anciano."""

edad = input("digita la edad")

if edad < 13:
    print("niño")
elif edad >= 13 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad <68:
    print("Eres un adulto")
else:
    print("Eres un anciano")


    
    