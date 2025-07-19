import requests

url = "https://raw.githubusercontent.com/gdelgador/ProgramacionPython202506/main/Modulo4/src/temperaturas.txt"
response = requests.get(url)

with open("temperaturas.txt", "w") as file:
    file.write(response.text)
with open("temperaturas.txt", "r") as archivo:
    lineas = archivo.readlines()
temperaturas = []
for linea in lineas:
    fecha, temp = linea.strip().split(",")
    temperaturas.append(float(temp))

promedio = sum(temperaturas) / len(temperaturas)
temperatura_max = max(temperaturas)
temperatura_min = min(temperaturas)

with open("resumen_temperaturas.txt", "w") as resumen:
    resumen.write(f"temperatura promedio: {promedio:.2f}°C\n")
    resumen.write(f"temperatura maxima: {temperatura_max:.2f}°C\n")
    resumen.write(f"temperatura minima: {temperatura_min:.2f}°C\n")

with open("resumen_temperaturas.txt", "r") as resumen:
    print("contenido de resumen_temperaturas.txt:\n")
    print(resumen.read())
