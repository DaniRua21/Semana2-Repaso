"""Un usuario ingresa una contraseña. Verifica si la contraseña es igual a"1234"."""


contra = str(input("Digita una contraseña"))

if contra == "1234":
    print("Acceso permitido")
else:
    print("Acceso denegado.")