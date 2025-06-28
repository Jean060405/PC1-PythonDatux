hora = input("Ingrese la hora en formato 24h (hh:mm): ")
try:
    horas, minutos = hora.split(":")
    horas = int(horas)
    minutos = int(minutos)
    hora_decimal = horas + minutos / 60
    if 7 <= hora_decimal <= 8:
        print("Es hora del desayuno.")
    elif 12 <= hora_decimal <= 13:
        print("Es hora del almuerzo.")
    elif 18 <= hora_decimal <= 19:
        print("Es hora de la cena.")
except ValueError:
    print("Formato inválido, por favor ingrese la hora como hh:mm.")