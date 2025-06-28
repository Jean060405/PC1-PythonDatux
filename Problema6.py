edad = int(input("Edad del usuario: "))
if edad < 4 :
    print("Entada gratis para el usuario")
elif edad >= 4 and edad <= 18 :
    print("Costo de la entrada: $5 ")
elif edad > 18 :
    print("Costo de la entrada: $10")
