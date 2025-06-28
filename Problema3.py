peso_payaso = 112
peso_muñeca = 75
numero_payaso = int(input("Ingrese la cantidad de payasos que se vende:"))
numero_muñeca = int(input("Ingrese la cantidad de muñecas que se vende:"))
peso_total = numero_muñeca*peso_muñeca+numero_payaso*peso_payaso
print(f"El peso total del paquete es {peso_total} gramos\ncompuesto de {numero_muñeca} unidades de muñecas y \n{numero_payaso} unidades de payaso")