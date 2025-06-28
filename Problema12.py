tipos_mime = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}
archivo = str(input("Nombre del archivo: ")).strip().lower()
if "." in archivo:
    extension = "." + archivo.split(".")[-1]
else:
    extension = ""
tipo_mime = tipos_mime.get(extension, "application/octet-stream")
print(f"Tipo MIME: {tipo_mime} ")
