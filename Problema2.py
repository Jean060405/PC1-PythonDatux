def crear_tabla():
    try:
        n = int(input("Ingrese un número entre 1 y 10 para generar su tabla: "))
        if not 1 <= n <= 10:
            print("el número debe estar entre 1 y 10.")
            return
        nombre_archivo = f"tabla-{n}.txt"
        with open(nombre_archivo, "w") as archivo:
            for i in range(1, 11):
                archivo.write(f"{n} x {i} = {n * i}\n")
        print(f"tabla del {n} guardada en {nombre_archivo}")
    except ValueError:
        print("entrada inválida. Debes ingresar un número entero.")

def leer_tabla():
    try:
        n = int(input("Ingrese un número entre 1 y 10 para leer su tabla: "))
        if not 1 <= n <= 10:
            print("el número debe estar entre 1 y 10.")
            return
        nombre_archivo = f"tabla-{n}.txt"
        with open(nombre_archivo, "r") as archivo:
            print(f"\ncontenido de {nombre_archivo}:")
            print(archivo.read())
    except FileNotFoundError:
        print(f"el archivo tabla-{n}.txt no existe.")
    except ValueError:
        print("entrada inválida. Debes ingresar un número entero.")

def leer_linea_tabla():
    try:
        n = int(input("ingrese el número n (1 a 10) para elegir la tabla: "))
        m = int(input("ingrese la línea m (1 a 10) a mostrar: "))
        if not (1 <= n <= 10 and 1 <= m <= 10):
            print("ambos números deben estar entre 1 y 10.")
            return
        nombre_archivo = f"tabla-{n}.txt"
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            print(f"línea {m} de la tabla del {n}: {lineas[m-1].strip()}")
    except FileNotFoundError:
        print(f"el archivo tabla-{n}.txt no existe")
    except IndexError:
        print(f"la linea {m} no existe en el archivo")
    except ValueError:
        print("entrada invalida, tienes que ingresar números enteros.")
      
def menu():
    while True:
        print("\menu de ocpiones")
        print("1. Crear tabla de multiplicar")
        print("2. Leer tabla completa")
        print("3. Leer una línea específica de una tabla")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == "1":
            crear_tabla()
        elif opcion == "2":
            leer_tabla()
        elif opcion == "3":
            leer_linea_tabla()
        elif opcion == "4":
            print("fin del programa!")
            break
        else:
            print("opcion no válida, vuelvelo a intentar")
menu()
