n1 = float(input("Ingrese el primer numero : "))
n2 = float(input("Ingrese el segundo numero : "))

print("""Elegir una opción, opción_1: suma de numeros, opción_2, resta de números, opción_3, producto de números""")
elección = str(int("Tu elección es: "))
opción_1 = n1+n2
opción_2 = n1-n2
opción_3 = n1*n2

if elección == opción_1 :
    print(f"la suma de los numeros es: {opción_1}")
elif elección == opción_2 :
    print(f"la resta de los numeros es: {opción_2}")
elif elección == opción_3 : 
    print(f"el producto de los numeros es: {opción_3}")
