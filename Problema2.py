#En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
#restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
#Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
#porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
#dejar como propina.
consumo=float(input("¿Cuánto fue su consumo en el restaurante?"))
porcentaje_propina = float(input("¿Qué porcentaje (%) de propina desea dejar ?"))
propina = (porcentaje_propina/100)*consumo
print(f"la cantidad de propina que dejará el cliente\ncon un porcentaje de propina de {porcentaje_propina}%\nes {propina} soles")