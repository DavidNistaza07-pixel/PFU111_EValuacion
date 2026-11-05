import csv
import os
import re

ARCHIVO = "prestamos.csv"
# --------------------------------
# 1. CARGAR LOS PRESTAMOS
# --------------------------------

def cargar_prestamos():
    prestamos = []

    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo)

                for fila in lector:
                    prestamos.append(fila)

        except (OSError, csv.Error) as error:
            print("Error al cargar los prestamos:", error)

    return prestamos


# --------------------------------
# 2. GUARDAR LOS PRESTAMOS
# --------------------------------

def guardar_prestamos(prestamos):
    campos = [
        "codigo",
        "nombre",
        "material",
        "dias"
    ]

    try:
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(
                archivo,
                fieldnames=campos
            )

            escritor.writeheader()
            escritor.writerows(prestamos)

        return True

    except OSError as error:
        print("Error al guardar los datos:", error)
        return False