import requests
import sqlite3
from pymongo import MongoClient
from datetime import datetime, timedelta

conn = sqlite3.connect('base.db')
cursor = conn.cursor()
client = MongoClient("mongodb://localhost:27017/")
mongo_db = client["sunat"]
mongo_collection = mongo_db["sunat_info"]

cursor.execute("""
CREATE TABLE IF NOT EXISTS sunat_info (
    fecha TEXT PRIMARY KEY,
    compra REAL,
    venta REAL)""")
def obtener_tipo_cambio(fecha):
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha={fecha}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

inicio = datetime(2023, 1, 1)
fin = datetime(2023, 12, 31)
delta = timedelta(days=1)

while inicio <= fin:
    fecha_str = inicio.strftime("%Y-%m-%d")
    datos = obtener_tipo_cambio(fecha_str)
    if datos and "compra" in datos and "venta" in datos:
        compra = datos["compra"]
        venta = datos["venta"]
        try:
            cursor.execute("INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)",
                           (fecha_str, compra, venta))
        except sqlite3.IntegrityError:
            pass  # ya existe
        mongo_collection.update_one(
            {"fecha": fecha_str},
            {"$set": {"compra": compra, "venta": venta}},
            upsert=True
        )
        print(f"{fecha_str} - Compra: {compra}, Venta: {venta}")
    inicio += delta

conn.commit()
conn.close()

conn = sqlite3.connect('base.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM sunat_info LIMIT 10")
filas = cursor.fetchall()
print("\n--- DATOS EN SQLite ---")
for fila in filas:
    print(fila)
conn.close()
