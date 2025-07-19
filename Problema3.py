def contar_lineas_codigo(ruta_archivo):
    try:
        if not ruta_archivo.endswith(".py"):
            return
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        lineas_codigo = 0

        for linea in lineas:
            linea_limpia = linea.strip()
            if linea_limpia != "" and not linea_limpia.startswith("#"):
                lineas_codigo += 1
        print(f"Número de líneas de código efectivas: {lineas_codigo}")
    except FileNotFoundError:
        print("La ruta del archivo no es válida o el archivo no existe.")

ruta = input("Ingrese la ruta del archivo .py: ")
contar_lineas_codigo(ruta)
